#!/usr/bin/env python3
# numpy-learning
import os
import sys
import numpy as np

# basics
def basics():
    a = np.array([1, 2, 3], dtype = "int16")
    print("a array: {}".format(a))
    b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
    print("b array: {}\n".format(b))

    # get dimensions
    print("number of dimensions of a: {}".format(a.ndim))
    print("number of dimensions of b: {}\n".format(b.ndim))

    # get shape
    print("shape of a: {}".format(a.shape))
    print("shape of b: {}\n".format(b.shape))

    # get type
    print("type of a: {}".format(a.dtype)) # data type
    print("type of b: {}\n".format(b.dtype))

    # get size
    print("bytes in a: {}".format(a.itemsize)) # number of bytes
    print("bytes in b: {}\n".format(b.itemsize))

    # get total size
    print("total size of a: {}".format(a.size * a.itemsize))
    print("total size of b: {}\n".format(b.nbytes))
