# https://www.w3schools.com/python/python_lists.asp

myList = ["apple", "banana", "cherry"]
print(myList)
# we can add duplicated values ex) apple
myList = ["apple","apple", "banana", "cherry"]
# list length
print(len(myList))
# list item -> data types -> any data types
list1 = ["apple","apple", "banana", "cherry"]
list2 = [1, 2, 3]
list3 = [True, False, True]
# a list can contain different data types. 
list4 = ["abc", 34, True, 40, "male"]
# lists are defined as objects with the data type 'list'
print(type(myList))
# the list() cosntructor
# using the list() constructor when createing a new list
thisList = list(("apple", "banana"))
print(thisList)

"""
constructor
class Person:
    def __init__(self, name, age):
    self.name = name
    self.age = age
"""
# access list items
# https://www.w3schools.com/python/python_lists_access.asp
print(f"myList: {myList[1]}")
# negative indexing
# -1 refers to the last item
# -2 refers to the second last item etc. 
print(f"index -1: {myList[-1]}")
print(f"index -2: {myList[-2]}")
print(f"myList[:3]: {myList[:3]}")
print(f"myList[2:]: {myList[2:]}")
print(f"myList[-4:-1]:{myList[-4:-1]}")
print("Check if item exists")
if"apple" in myList:
    print("Yes, 'apple' is in the myList")
