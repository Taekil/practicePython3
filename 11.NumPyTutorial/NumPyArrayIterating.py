"""
NumPy Array Iterating
Iterating Arrays. 
Iterating means going through elements one by one. 
as we deal with multi-dimensional arrays in numpy, 
we can this using basic for loop of python. 
if we iterate on a 1-D array it will go through each element
one by one. 
"""
import numpy as np
# iterating 1-D array
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# iterating 2-D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)





