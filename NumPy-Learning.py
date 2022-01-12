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
    print("b array:\n{}\n".format(b))

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

def basic_modifing():
    a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
    print(a.shape)

    # get a specific element [row, column]
    print("specific element: {}\n".format(a[1,-2]))

    # get a specific row
    print("specific row: {}\n".format(a[0, :]))

    # get a specific column
    print("specific column: {}\n".format(a[:, 2]))

    # more advanced version [startindex:endindex:stepsize]
    print("custom range: {}\n".format(a[0, 1:6:2]))

    #replacing
    a[1,5] = 20
    print("a with one replaced element:\n{}\n".format(a))

    a[:,2] = [1,2]
    print("a with replaced elements range:\n{}\n".format(a))

    b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
    print("3 dimensions b array:\n{}\n".format(b))

    # get specific element (work outside in)
    print("second row in 3d array b: {}\n".format(b[0,1,0:2:1]))

    # ^ but this time it's column
    print("first column in 3d array b:\n{}\n".format(b[:,:,0:1:1]))

basic_modifing()
