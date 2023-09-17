"""
https://www.w3schools.com/python/numpy/numpy_data_types.asp

strings: ABCD

integer: 1, 2, 3, 4 ... -1, -2, -3, ...

float: 1.23, 42.42 ......

boolean: True or False

complex: 1.0 + 2.0j, 1.5 + 2.5j
"""
"""
i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - Object
S - string
U - Unicode string
V - fixed chunk of memory for other type. 
"""
# checking the data type of an array
# dtype
import numpy as np

arrInteger = np.array([1, 2, 3, 4])
print(arrInteger.dtype)

arrString = np.array(['apple', 'banana', 'cherry'])
print(arrString.dtype)

# Creating arrays with a defined data type. 
# array() function to create arrays, this function can take
# an optional argument. 
# dtype that allows us to define the expected data type of 
# the array elements

# creating an array with data type string
arr2String = np.array([1, 2, 3, 4], dtype='S')
print(arr2String)
print(arr2String.dtype)
# for i, u, f, S and U we can define size as well

# create an array with data type 4 bytes integer
arri4 = np.array([1, 2, 3, 4], dtype='i4')
print(arri4)
print(arri4.dtype)

# what if a value can Not Be converted?
# why do we need to make conversion?
"""
arr = np.array(['a', '2', '3'], dtype = 'i')
a non integer string like 'a' can not be conveted to intger
(will raise an error)
"""

# converting data type on existing arrays
# the best way to change the data type of an existing array, 
# making a copy of the array with the astype() method
# astype() function creates a copy of the array, and allows you 
# to specify the data type as a parameter. 
# newArr = arr.astype('i') # 'i' for integer

arr = np.array([1.1, 1.2, 3.1]) # type is float
newArr =arr.astype('i') # type is integer
newArr = arr.astype(int)

# example. 
arr = np.array([1, 0, 3])
newArr = arr.astype(bool)
print(newArr)
print(newArr.dtype)



