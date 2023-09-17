"""
https://www.w3schools.com/python/python_arrays.asp

Python does not have built-in arrays
but Python Lists can be used instead.
"""

# accessing the elements of an array
cars = ["ford", "volvo", "bmw"]
x = cars[0] # get the value of the first array item. 
cars[0] = "toyota" # modify the value of the first array item. 

# The length of an array
# use the len()s method to return the legnth of an array. 
x = len(cars)

# looping array elements. 
for x in cars:
    print(x)

# adding array elements
# append()
cars.append("Honda")

# removing array elements
# you can use the pop() method to remove
# an element from the array. 
cars.pop(1) # delete teh second element of the car array. 
cars.remove("volvo") # delete the element that has the value
# the list's remove() method only removes the first occurence
# of the specified value. 

"""
Array methods. 
append()
clear()
copy(): returns a copy of the list
count(): the number of elements with the sepecified value
extend(): add to the end of the current list
index(): the index of the first element with the specified value. 
insert(): adds an element at the specified position. 
    list_name.insert(index, element)
pop()
remove()
reverse()
sort(): sorts the list.
    By default, sort() method uses an algorithm called Timsort. 
    python does not provide a built-in way to select a sorting algorithm. 

so, we should use sorted()
    sorted_fruits = sorted(fruits, key=len)
    sorted_fruits = sorted(fruits, key=custom_sorting_algorithm)
"""









