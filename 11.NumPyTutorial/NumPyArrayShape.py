"""
Shape of an Array: the shape of an array is the number of 
elements in each dimension. 

Get the Shap of an Array

NumPy arrays have an attribute called shape that returns a tuple
with each index having the number of corresponding elements. 

Print the shape of a 2-D array. 
"""

import numpy as np
arr = np.array([
                [1, 2, 3, 4], 
                [5, 6, 7, 8]
                ])
print(arr.shape) # the returns (2, 4) 2 dimensions, 
                 # where the first dimensions has 2 elements
                 # and the second has 4. 

# ndim = 5 using a vector with values 1, 2, 3, 4 and verify
# that last dimension has value 4
arr = np.array([1, 2, 3, 4], ndmin=5) # create with 5 dimensions
print(arr)
print("shape of array: ", arr.shape) # (1, 1, 1, 1, 4)

# What does the shape tuple represent?
# the integers at every index tells about the number of elements
# the corresponding dimension has. 
# in the example above at index-4 we have have 4, so we can say
# that 5th(4+1th) dimension has 4 elements. 

"""
https://www.w3schools.com/python/numpy/numpy_array_reshape.asp

NumPy Array Reshaping. 
what is reshaping -> changing the shape of an array. 
the shape of an array is the number of elements in each dimension. 
by reshaping we can add or remove dimensions or change number of elements
in each dimension. 
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newArr = arr.reshape(4, 3) # converting the 1-D array with 12 elements into 
                           # a 2-D array. 
                           # The outermost dimension will have 4 arrays, 
                           # each with 3 elements.  
print(newArr)

# Reshape From 1-D to 3-D
newArr = arr.reshape(2, 3, 2) # 2 arrays containing 3 arrays with 2 elements. 
print(newArr)

"""
can we reshape into any shape?
Yes, as long as the elements required for reshaping are equal in both shapes. 

8 elements 1-D array -> 4 elements 2 rows 2D 
but, 3 elements 3 Rows 2D not, because 3x3 = 9 elements. 
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base) # the example returns the original array, so
# it is a view. 

"""
unknown Dimension? you do not have to sepecify an exact number for one of the 
Dimensions in the reshape method. 
pass -1 as the value, and NumPy will calculate this number for you. 
"""
newArr = arr.reshape(2, 2, -1)
print(newArr)

"""
Flattening the arrays. 
coverting into a 1-D array
"""
newArr = arr.reshape(-1) 

