import functools as _functools


def keymemo(key):
    """memoize decorator that applies the function key to the arguments
    in order to retrieve the key to use in the cache dictionary."""

    def _memo(fn):
        """the memoize decorator itself."""

        cache = {}

        @_functools.wraps(fn)
        def _fn(*args):
            if key: args = key(*args)
            try: ret = cache[args]
            except KeyError: ret = cache[args] = fn(*args)
            return ret

        _fn._cache = cache
        return _fn

    return _memo


def instancekeymemo(key):
    """memoize decorator that applies the function key to the arguments.
    This decorator can be used for class methods, and each instance keeps its
    own cache."""

    def _instancememo(fn):
        """the instancememoize decorator itself."""

        cache_name = '_cache_' + fn.__name__

        def _get_cache(self, fn):
            """cache is stored in the self namespace, retrieved at runtime."""
            try:
                return getattr(self, cache_name)
            except AttributeError:
                setattr(self, cache_name, {})
                return getattr(self, cache_name)

        @_functools.wraps(fn)
        def _fn(self, *args):
            cache = _get_cache(self, fn)
            if key: args = key(*args)
            try: ret = cache[args]
            except: ret = cache[args] = fn(self, *args)
            return ret

        return _fn

    return _instancememo


# the classical memoize decorator (without a key function)
memo = keymemo(key=None)

# the instancememo decorator (without a key function)
instancememo = instancekeymemo(key=None)
