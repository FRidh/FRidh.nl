Title: Sparse arrays in Python
Date: 2014-04-07
Tags: python

Numpy offers dense arrays and both [Numpy](http://www.numpy.org/) and
[Scipy](http://scipy.org/) offer sparse matrices. However, they don't
offer any sparse array solution. On the web I found some implementations
of sparse arrays but they were generally quite limited:

-   [ndsparse](https://launchpad.net/ndsparse) operators only support
    scalars
-   [sparray](http://www.maths.lth.se/matematiklth/personal/solem/downloads/sparray.py)
    operators only support other sparse arrays

What I would like to do is replace in some of my calculations certain
dense arrays with sparse arrays. Numpy compatibility is therefore
important. A first version can be found
[here](https://github.com/FRidh/sparse).

What works?

-   The basic operators work with scalars, sparse arrays and dense
    arrays.
-   Basic slicing is partially supported. newaxis, None, slice and
    Ellipsis aren't really supported yet.
-   Converting from dense to sparse and vice versa

What's left to do?

-   Finish basic slicing
-   In-place operators
-   Advanced slicing
-   Enforcing dtype
-   Cythonize

Because I was curious I Cythonized it quickly. While it is much much
faster than the plain Python implementation it still is about a factor
1000 slower than dense arrays when operatoring with a dense array.
Unfortunately this is too slow for my use case, so for now I reverted to
using dense arrays but with a reduced model size. Nevertheless I am sure
there is a significant performance increase possible.
