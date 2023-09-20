import sys
from functools import wraps

cache_dict_module = sys.modules[__name__]
cache_dict_module.cache_dict = {}
cache_dict_module.maxsize = 1048
cache_dict_module.del_min_used = True


def cache_everything(f_py=None):
    r"""
    Cache Everything Decorator

    This module provides a decorator `cache_everything` that can be used to cache the results of function calls.
    It uses a dictionary to store cached results and allows customization of cache size and eviction strategy.
    Unlike some caching mechanisms that rely on hashable arguments,
    the "cache_everything" decorator accepts a wide range
    of argument types, including non-hashable objects,
    complex data structures, and even functions as arguments.
    This means you can cache the results of functions that
    operate on mutable or unhashable input data,
    making it suitable for a broader set of use cases.
    For example, if your function operates on lists,
    dictionaries, or custom objects, you can still
    apply the decorator without the need to convert
    these inputs into hashable forms. This flexibility simplifies
    the caching process and allows you to cache results
    efficiently for functions that work with diverse and
    potentially non-hashable data.

    Overall, the ability to cache results with non-hashable arguments enhances the versatility of the decorator and makes
    it accessible for a wider range of applications,
    where data may not always conform to the hashable requirements of
    traditional caching mechanisms.
    Usage:
        To cache the results of a function, decorate it with `@cache_everything`.

    Example:
        import numpy as np
        import random
        from allescacher import cache_everything, cache_dict_module

        cache_dict_module.maxsize = None
        cache_dict_module.del_min_used = True

        @cache_everything
        def getnparray(l):
            return np.array(l) / 10 * 3

        done = []
        for _ in range(1000):
            done.append(
                getnparray([random.randint(0, 10) for x in range(random.randint(1, 5))])
            )

        # Clear the cache for the 'getnparray' function
        cache_dict_module.cache_dict[getnparray.__qualname__].clear()

    Module Variables:
        - `cache_dict_module`: A module-level variable used to store the cache dictionary.
        - `cache_dict_module.cache_dict`: The cache dictionary where cached results are stored.
        - `cache_dict_module.maxsize`: The maximum size of the cache (None for unlimited).
        - `cache_dict_module.del_min_used`: A flag to determine whether to evict the least-used cache entry.

    Decorator:
        - `@cache_everything`: Decorates a function to enable caching of its results.

    Functions:
        - `cache_everything(f_py=None)`: The decorator function that can be used to cache function results.

    This module provides a flexible caching mechanism that can be applied to functions to improve performance by
    retrieving cached results for known input arguments, reducing the need for redundant computations.
    """
    assert callable(f_py) or f_py is None
    if f_py is not None:
        cache_dict_module.cache_dict[f_py.__qualname__] = {}

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            keydi = f"{repr(args)}{repr(kwargs)}{args}{kwargs}"
            if keydi in cache_dict_module.cache_dict[f_py.__qualname__]:
                cache_dict_module.cache_dict[f_py.__qualname__][keydi]["count"] += 1
                return cache_dict_module.cache_dict[f_py.__qualname__][keydi]["value"]
            vala = func(*args, **kwargs)
            if cache_dict_module.maxsize:
                if (
                    len(cache_dict_module.cache_dict[f_py.__qualname__])
                    > cache_dict_module.maxsize
                ):
                    if cache_dict_module.del_min_used:
                        soa = sorted(
                            cache_dict_module.cache_dict[f_py.__qualname__],
                            key=lambda x: cache_dict_module.cache_dict[
                                f_py.__qualname__
                            ][x]["count"],
                            reverse=True,
                        )
                        _ = cache_dict_module.cache_dict[f_py.__qualname__].pop(soa[-1])
                    else:
                        _ = cache_dict_module.cache_dict[f_py.__qualname__].popitem()
            cache_dict_module.cache_dict[f_py.__qualname__][keydi] = {
                "value": vala,
                "count": 0,
            }
            return vala

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator
