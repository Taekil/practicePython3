# https://www.w3schools.com/python/numpy/numpy_array_join.asp
"""
NumPy Joining Array. 
"""
import numpy as np

# 2-D array
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6], [7,8]])
arr3 = np.array([[9, 10],[11, 12]])
arr12 = np.concatenate((arr1,arr2), axis=0)
arr23 = np.concatenate((arr2, arr3), axis=1)
arr123 = np.concatenate((arr1, arr2, arr3), axis=None)
print(arr12)
print(arr23)
print(arr123)
'''
arr12= [[1 2]
        [3 4]
        [5 6]
        [7 8]]
arr23= [[ 5  6  9 10]
        [ 7  8 11 12]]
arr123= [ 1  2  3  4  5  6  7  8  9 10 11 12]

axis=0 (default): along the veritcal axis (stacked on top of each other) 
axis=1: to concatenate the arrays along the horizontal axis. side by side
axis=None: into a 1-D array. 
'''
# join arrays using stack Functions.
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
# same as concatenation, but stacking is done along a new axis. 
print(arr)
'''
arr= [[1 4]
      [2 5]
      [3 6]]
'''
arr = np.hstack((arr1, arr2)) # to stack along rows. 
print(arr)
arr = np.vstack((arr1, arr2)) # to stack along columns. 
print(arr)
arr = np.dstack((arr1, arr2)) # stack along height, same as depth. 
print(arr)

"""
Split: reverse operation of joining. 
Joining merges multiple arrays into one and splitting breaks one array into
multiple. 
we use array_split() for splitting arrays, we pass it the array we want to split
and the number of splits. 
"""

arr = np.array([1, 2, 3, 4, 5, 6])
newArr = np.array_split(arr, 3) # [array([1, 2]), array([3, 4]), array([5, 6])]
subarray1 = newArr[0]
subarray2 = newArr[1]
subarray3 = newArr[2]
print(subarray1, subarray2, subarray3)

newArr= np.array_split(arr, 4) # [1, 2], [3, 4], [5], [6]
print(newArr)

# splitting 2-D array
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newArr = np.array_split(arr, 3)
print(newArr)
# we can sepecify which axis you want to do the split around. 
newArr = np.array_split(arr, 2, axis=1) # axis=1 -> along the row. 
print(newArr)
# hsplit(), vsplit(), dsplit()
"""
Search
where() method
"""
arr = np.array([1, 2, 3, 4, 5, 6])
x = np.where(arr == 4)
print(x) # array([3, 5, 6],) index number of the target. 
# return a tuple

# x = np.where(arr%2 == 0) find the indices where the values are even
# x = np.where(arr%2 == 1) find the indices where the valvues are odd

# searchsorted() performs a binary search in  the array. 
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
# the number 7 should be inserted on index 1 to remain the sort order. 

# multiple value
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6]) # find the indices where the values 2, 4, 6
# should be inserted. 
print(x) # [1 2 3] the three indices where 2 4 5 would be inserted in the original
# array to maintain the order. 

"""
Sort
fucntion sort()
the method returns a copy of the array. 
leaving the original array unchanged. 
alphabetically. 

"""

"""
Filter
gettinig some elements out of an existing array and
creating a new array
"""
# create an array from the elemtns on index 0 and 2
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newArr= arr[x]
print(newArr) # the new array contains only the values where
# the filter array ahd the value True, in this case, index 0 and 2. 

# Creating the Filter Array
# create a filter array that will return only value higher than 42. 

filter_arr = []

# go through each element in arr
for element in arr:
    # if the element is higher than 42, set the value to True, otherwise False. 
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newArr = arr[filter_arr]

print(filter_arr)
print(newArr)

# Creating Filter Directly From Array
# we can directily substitute the array instead of the iterable
# variable in our condiiton and it will work just asd we
# expect it to
filter_arr = arr > 42
newArr = arr[filter_arr]
print(filter_arr)
print(newArr)


