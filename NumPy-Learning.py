#!/usr/bin/env python3
# numpy-learning
import os
import sys
import numpy as np

# a = np.array([1, 2, 3], dtype = "int16")
# print("a array: {}".format(a))
# b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print("b array:\n{}\n".format(b))

# basics
def basics():

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

    # replacing
    b[:,1,:] = [[1,3],[3,7]]
    print("replaced 2nd and 4th row in b:\n{}\n".format(b[:,1,:]))

def initializing():
    # all 0s matrix
    print("matrix full of zeros:\n{}\n".format(np.zeros((2,3))))

    # all 1s matrix
    print("matrix full of ones:\n{}\n".format(np.ones((3,2))))

    # any other number
    print("matrix full of custom numbers:\n{}\n".format(np.full((2,2), 69)))

    # any other number (full_like)
    print("replaces array with certain number:\n{}\n".format(np.full_like(a, 4)))

    # random decimal numbers
    print("matrix filled with random numbers:\n{}\n".format(np.random.rand(4,2)))

    # random integer values
    print("matrix filled with random integers:\n{}\n".format(np.random.randint(7, size=(3,3))))

    # the identity matrix
    print("the identity matrix:\n{}\n".format(np.identity(5)))

    #repeat an array
    arr = np.array([[1,2,3]])
    r1 = np.repeat(arr,3, axis=0)
    print("repeat an array:\n{}\n".format(r1))

    #matrix task #1
def matrixTask1():
    t = np.full((5,5), 0)
    t[:,0:5:4] = [[1]]
    t[0:5:4] = [[1]]
    t[[2],[2]] = [9]
    print(t)

def mathematics():
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 0, 1, 0])
    print("a array:\n{}\n".format(a))
    print("b array:\n{}\n".format(b))

    # Basics

    #addition
    print("a addition:\n{}\n".format(a + 2))

    #subtraction
    print("a subtraction:\n{}\n".format(a - 1))

    #multiplication
    print("a multiplication:\n{}\n".format(a * 2))

    #division
    print("a division:\n{}\n".format(a / 2))

    #sin
    print("sin(a):\n{}\n".format(np.sin(a)))

    #cos
    print("cos(a):\n{}\n".format(np.cos(a)))

    # Linear Algebra

    c = np.ones((2,3))
    d = np.full((3,2),2)
    print("c matrix:\n{}\n".format(c))
    print("d matrix:\n{}\n".format(d))

    #multiply matrixes
    print("c matrix multiplied by d matrix:\n{}\n".format(np.matmul(c,d)))

    #find the determinant
    e = np.identity(3)
    print("determinant of e matrix of identity 3:\n{}\n".format(np.linalg.det(e)))

    # Statistics

    stats = np.array([[1, 2, 3], [4, 5, 6]])

    #min value in stats
    print("minimum value in stats array, axis 0:\n{}\n".format(np.min(stats,axis=0)))

    #max value in stats
    print("maximum value in stats array:\n{}\n".format(np.max(stats)))

    #sum of all values in stats
    print("summed values in stats array:\n{}\n".format(np.sum(stats)))
    
