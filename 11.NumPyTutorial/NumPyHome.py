"""
https://www.w3schools.com/python/numpy/default.asp

NumPy is a python library
NumPy is used for working with arrays
NumPy is short for "numerical python"
"""
# NumPy Home
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
# type(): Built-in python function tells us the type of the object 
# passed to it. Like in above code it shows hat arr is numpy.ndarray type. 
print(type(arr))

# NumPy Introduction. 
"""
what is NumPy? 
1) wowrking with arrays
2) functions for working in domain of Linear algebra, fourier transform, and
    matrices
3) Numerical Python

Why Using NumPy?
1) aim to provide an array object that is up to 50X faster than traditional python 
    Lists
2) the array object in NumPy is called ndarray, it provides a lot of supporting
    functions that make working with ndarray very easy. 

Why NumPy Faster than Lists?
NumPy array are stored at one continuous place in memory unlike lists, 
so processes can access and manipulate them very efficiently. 

This behavior is called locality of reference in computer science. 

This is the main reason why NumPy is fasgter than lists. 
Also it is optimized to work with lastet CPU architectures. 

NumPy is usually imported uder the np alias
(alias: an alternate name for referrring to the same thing)
"""

# checking NumPy version
print(np.__version__)

# To create an ndarray, we can pass a list
# arr = np.array([1, 2, 3, 4, 5s])

# using a tuple to create a numPy array
arr2 = np.array((1, 2, 3, 4, 5))
print(arr2)

# Dimensions in Arrays
# 0-D arrays, or Scalars, the elements in an array
# each value in an array is a 0-D array
arr0D = np.array(42)
print(arr0D)

# 1-D array, its elements is called uni-Dimensional or 1-D array
# These are the most common and basic arrays.  

# 2-D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2D)

# 3-D array: A array having 2-D arrays (matrices) as its elements is called
# 3-D array
# These are often used to represent 3rd order tensor
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3D)

# check Number of Dimensions?
print(arr0D.ndim)
print(arr2D.ndim)
print(arr3D.ndim)

# Higher Dimensional Arrays
# an array can have any number of dimensions, 
# when the array is created, you can defined the number of dimensions by using
# the ndmin argument. 
# create an array with 5 dimensions and verify that it has 5 dimensions
arr5D = np.array([1, 2, 3, 4], ndmin=5)

print(arr5D)
print("number of dimensions: ", arr5D.ndim)



