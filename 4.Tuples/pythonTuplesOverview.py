mytuple = ("apple", "banana", "cherry")
# tuple : store multiple items in a sigle variables
# tuple: a collection ordered and unchangeable. 
# round brackets.
thisTuple = ("apple" , "banana", "cherry")
print("thisTuple", thisTuple)
# tuple items are indexed. 
# ordered, unchangeable, allow duplicates. 
# tuple length
# create tuple with one item
print(len(thisTuple))
print(len(mytuple))
# create tuple with one item
# to create tuple with only one item, 
# we have to add a comma after the item. 
thisTuple2 = ("apple",)
#tuple
print(type(thisTuple2))
thisTuple3 = ("apple")
# string
print(type(thisTuple3))
tuple2 = (1, 2, 3, 4, 5)
# string int and boolean data types
tuple3 = (True, False, True)
# a tuple can contain different data types
tuple4 = ("abc", 34, True, 40, "male")
print(type(tuple4))
# the tuple constructor
thisTuple = tuple(("apple", "banana", "cherry"))
print(thisTuple)
my_List = [1, 2, 3, 4, 5]
my_tuple = tuple(my_List)
print(my_tuple)