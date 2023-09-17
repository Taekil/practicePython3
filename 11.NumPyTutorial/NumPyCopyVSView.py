"""
NumPy Array Copy vs View

the difference between copy and view

the copy is a new array
the view is a view of the original array. 

the copy owns the data and any changes made to the copy, 
not affect orignial array, and any changes made to the original
array will not affect the copy 

the view does not own the data and any changes made to the view
will affect the original array, and any changes made to the 
original will affect the view. 
"""

"""
copy. 
make a copy, change the original array, and display both arrays
"""
import numpy as np

arr = np.array([1, 2, 3, 4])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

"""
copy should not be affected by the changes made to the original
"""

"""
view.

make a view, change the original array, and display both arrays, 
"""
y = arr.view()
arr[0] = 52

print(arr)
print(y) # same as arr
"""
the view should be affected by the changes made tot he original array. 
"""

"""
check if array owns its data
as metioned above, copies owns the data, and views does not own the data, 
but how can we check this?

every NumPy array ahs the attribute base returning None if the array owns
the data

otherwise, the base attribute refers to the original object.
"""
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()

print(x.base) # x is copy, own the data, so None-base
print(y.base)



