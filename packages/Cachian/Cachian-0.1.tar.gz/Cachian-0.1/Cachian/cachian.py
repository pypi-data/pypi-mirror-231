#from copyreg import pickle
from pickle import dumps, HIGHEST_PROTOCOL
import os
from threading import Lock
from time import time
from hashlib import sha3_256 as hashfunc # Fastest hash as per Python 3.9, next best is blake2b
from functools import lru_cache
# from collections import OrderedDict


NUM_PARAM_HASH_CACHED:int = 10000
CACHIAN_ENABLE:bool = int(os.environ.get('CACHIAN_ENABLE', 1)) == 1

if not CACHIAN_ENABLE:
    print('---Cachian DISABLED---')


@lru_cache(NUM_PARAM_HASH_CACHED)
def get_param_hash(*args, **kwargs):

    key1 = dumps(args, HIGHEST_PROTOCOL)
    key2 = dumps(kwargs, HIGHEST_PROTOCOL)

    m = hashfunc()  
    m.update(key1+key2)

    return m.hexdigest()



class Cachian():

    ttl:int = -1  # Seconds
    cache_lib = {}
    maxsize:int = -1
    lock:Lock = Lock()
    obj_self = None#Used for holding self for cached class methods

    def __init__(self, *args, **kwargs) -> None:

        self.ttl = kwargs.get('ttl', -1)
        self.maxsize = kwargs.get('maxsize', -1)
        self.test_mode = kwargs.get('test_mode', False)
        self.cache_lib = kwargs.get('cache_lib', {})

        self.clear_all()

    def __call__(self, func, *args, **kwargs):
        parent = self
        if self.obj_self is None:
            return _CachianWrapper(func, parent)
        else:
            return _CachianWrapper(self.obj_self, func, parent)
        

    def clear_all(self):
        with self.lock:
            self.cache_lib = {}

    def _length(self):
        return len(self.cache_lib)

    def _full(self):
        if self.maxsize <= 0:
            return False

        return len(self.cache_lib) >= self.maxsize

    # Remove item by FIFO
    def _pop(self):
        return self.cache_lib.popitem(False)

    def add(self, key, item):
        if not CACHIAN_ENABLE:
            return

        with self.lock:
            if self._full():
                self._pop()

            self.cache_lib[key] = item

            pass

    # Must be called after checking with has().
    # get() doesn't check for TTL
    def get(self, key):
        with self.lock:
            return self.cache_lib[key]

    # Must be called after checking with has().
    # remove() doesn't check for TTL
    def remove(self, key):
        with self.lock:
            if key in self.cache_lib.keys():
                del self.cache_lib[key]

    
    def set_object_self(self,obj_self):
        self.obj_self = obj_self


    def has2(self, key):
        with self.lock:
            r = self.cache_lib.get(key)
            if r is not None:
                if self.ttl > 0:
                    result, ts = r
                    if time() - ts > self.ttl:
                        del self.cache_lib[key] #Remove so future checks are faster
                        return None, None #Key expired based on TTL
                    else:
                        return result, ts #Key is within TTL
                else:
                    return r #TTL is not used
            else:
                return None, None #Key doesn't exist


# Uses InnerClass so both Cachian() and Cachian(ttl=1) format is supported
class _CachianWrapper(object):

    func = None
    parent:Cachian = None
    hit:int =0
    miss:int =0

    def __init__(self, func, parent) -> None:
        self.func = func
        self.parent = parent

    def __call__(self, *args, **kwargs):

        key = get_param_hash(*args, **kwargs)
        
        result, ts = self.parent.has2(key)

        if result is not None:
            self.hit += 1

            if self.parent.test_mode:
                return 'hit'
        else:
            result = self.func(*args, **kwargs)
            self._add(key,result)
            self.miss += 1

            if self.parent.test_mode:
                return 'miss'

        return result


    def __len__(self):
        return self.parent._length()

    def _add(self,key,result):
        self.parent.add(key, (result, time()))
    
    def fresh(self, *args, **kwargs):
        key = get_param_hash(*args, **kwargs)
        self.parent.remove(key)
        result = self.func(*args, **kwargs)
        self._add(key,result)

        if self.parent.test_mode:
            return 'fresh'

    def clear_all(self):
        self.parent.clear_all()
        get_param_hash.cache_clear()

    def reset(self):
        self.hit=0
        self.miss=0
        self.clear_all()

    def clear(self, *args, **kwargs):
        key = get_param_hash(*args, **kwargs)

        self.parent.remove(key)

        if self.parent.test_mode:
            return 'cleared'

    def cache_info(self):
        return {'hit':self.hit,'miss':self.miss,'size':len(self)}

    def function_name(self):
        return self.func.__name__

def global_cache_reset():

    import gc

    wrappers = [
        a for a in gc.get_objects() 
        if isinstance(a, _CachianWrapper)]

    reset_functions = []

    for wrapper in wrappers:
        try:
            wrapper.clear_all()
            reset_functions.append(wrapper.function_name())
        except:
            pass