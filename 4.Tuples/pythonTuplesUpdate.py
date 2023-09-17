# How update a tuple 
# change tuple values
# once a tuple is create -> not changeable. 
# covert the tuple into a list -> change the list -> 
# convert the list back into the tuple
x = ("apple", "banana", "cherry")
print("tuple x: ", x)
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print("updated tuple x: ", x)

# adding items
# tuples are imuttable -> not a built-in append() method
# 1. coverting into list
y = list(x)
y.append("orange")
x = tuple(y)
print("appended x: ", x)
# 2. add tuple to tuple
# tuple allows to add tuples to tuples. 
# create a new tuple with the item and add it. 
y = ("pine",) # comma as a tuple with a single item
x += y
print("added x: ", x)
# remove item-> also using coversion to list
# list = list(tuple)
# list.remove("value")
# tuple = tuple(list)

del x
# print(x) 
# this will raise an error because the tuple
# not defined x

# unpack tuples?
# packing -> assign values to it. 
fruit = ("apple", "banana", "kiwi", "cherry", "pine")

# in python, we are allowed to extract the values
# back with variables. -> unpacking
(green, yellow, *red) = fruit
print("green: ", green)
print("yellow: ", yellow)
print("red: ", red)
# if the number of variables is less than the number of 
# values, we can add an * to the varible name(*red) 
# and the values will be assigned to the variable as
# a list. 
print("type of green: ", type(green))
print("type of yellow: ", type(yellow))
print("type of red: ", type(red))

# at the middle of the variable list, the * 
# will assigned values to the variable until
# the number of values left matched the number of variables 
# left. 
tester = ("apple", "mango", "papay", "pine", "orange", "cherry")
(green, *tropical, yellow, red) = tester
print("green", green)
print("topic", tropical)
print("yellow", yellow)
print("red", red)

