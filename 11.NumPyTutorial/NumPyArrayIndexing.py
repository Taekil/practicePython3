"""
https://www.w3schools.com/python/numpy/numpy_array_indexing.asp

NumPy Array Indexing
"""
import numpy as np

# we can access an array element by referring to itis index number. 
arr = np.array([1, 2, 3, 4])
# get the first element from the following array
print("arr[0]:", arr[0])
# get the second element
print("arr[1]:", arr[1])
# get the elements and adding them. 
print("arr[2]+arr[3]:", arr[2]+arr[3])

# accessing 2-D arrays
# to access elements from 2-D arrays we can use comma separated integers
# representing the dimension and the index of the element. 

# Table with rows and columns
arr2D = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element on 1st row:", arr2D[0, 1])
print("5th element on 2nd row:", arr2D[1, 4])

# accessing 3-D arrays
# using comma 
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("arr3D[0, 1, 2]: ", arr3D[0, 1, 2])

# the first number represents the first dimentsion containing two arrays, 
# [1, 2, 3], [4, 5, 6] -> the is for the "0"
# then , the second number "1" -> represent [4, 5, 6]
# then, the third number "2" -> reparesent 6
# so, return "6"

# negative indexing
# using negative indexing to access an array from the end. 

arrNG = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("last element from 2nd dim:", arrNG[1, -1])

# NumPy Array Slicing
"""
https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
"""
# slicing arrays. 
# we pass slice instead of index like this: [start:end]
# we can also define the step, like this: [start:end:step]

# if we do not pass start its considered 0.
# if we do not pass end its considered length of array in that dimension. 
# if we do not pass step its considered 1. 

"""
Example: slicing elements from index 1 to index 5 from the following array, 

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

print(arr[4:]) # slice elements from index 4 to the end of the array

print(arr[:4]) # slice elements from the beginning to index 4 (index 4 not included)

print(arr[-3:-1]) # slice from the index 3 from the end to index 1 from the end

STEP 
use the step value to determine the step of the slicing
print(arr[1:5:2]) return every other element from index 1 to index 5
pirnt(arr[::2]) return every other element from the entire arrays

slicing 2-D arrays
from the second element, slice elements from index 1 to index 4 (not included)
arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(arr[1, 1:4])

print(arr[0:2, 2]) from both elements, return index 2
print(arr[0:2, 1:4]) from both elements, slice index 1 to index 4 (not included)
"""



