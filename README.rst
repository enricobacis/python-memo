python-memo
===========

*python memoize decorators that cache the results of functions.*

Description
-----------

*memoize* and *keyed-memoize* decorators.

- ``memo``: The classical *memoize* decorator. It keeps a cache
  ``args -> result`` so you don't continue to perform the same computations.

- ``keymemo(key)``: This decorator factory act as ``memo`` but it permits to
  specify a ``key`` function that takes the ``args`` of the decorated function
  and computes a ``key`` value to use as key in the cache dictionary. This way
  you can for example use a single value of a dictionary as key of the cache,
  or apply a function before passing something to the cache.

- ``instancememo``: The classical *memoize* decorator that can be applied to
  class functions. It keeps a cache ``args -> result`` so you don't continue
  to perform the same computations. The cache is kept in the class namespace.

- ``instancekeymemo(key)``: This decorator factory works like a combination of
  ``instancememo`` and ``keymemo``, so it allows to specify a function that
  generate the cache key based on the function arguments and can be applied
  to class functions.


Usage
-----

.. code:: python

    from memo import memo

    @memo
    def fibonacci(n):
        if n <= 2:
            return 1
        return fibonacci(n-1) + fibonacci(n-2)

.. code:: python

    from memo import keymemo

    @keymemo(lambda tup: tup[0])
    def function(tup):
        # build a cache based on the first value of a tuple
        ...

Installation
------------

The package has been uploaded to `PyPI`_, so you can install it with pip:

    pip install python-memo


.. _PyPI: https://pypi.python.org/pypi/python-memo
