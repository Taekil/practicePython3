# https://www.w3schools.com/python/python_lists_sort.asp

#python_sortLists
# sort(): ssort the lsit aphanumerically, ascending, by default
print("ascending and descending of sort()")
thisList = ["orange", "mango", "kiwi", "pineapple", "banana"]
thisList.sort()
print("fruitList: ", thisList)
thisList.sort(reverse=True)
print("fruitList: ", thisList)
thisList = [100, 50, 65, 823, 23]
thisList.sort()
print("numberList: ",thisList)
thisList.sort(reverse=True)
print("numberList: ",thisList)

# customize sort function
# sorting based on how close the number is to 50
# by using the keyword arguement key = function
print("custom sorting function")
def myfunc(n):
    return abs(n - 50)
thisList = [100, 50, 65, 82, 23]
thisList.sort(key = myfunc)
print("customed List: ", thisList)

# case insensitive sort
# by default, the sort() method is case sensitive, 
# resulting in all capital letters being sorted before
# lower case letters. 
thisList = ["banana", "Orange", "kiwi", "cherry"]
thisList.sort()
print(thisList)
# use str.lower as a key function
thisList.sort(key=str.lower)
print(thisList)
# reverseOrder
# thisList.reverse()

# CopyList
# list2 = list (X)
# using copy()
thisList = ["apple", "banana", "cherry"]
myList = thisList.copy()
myList2 = list(thisList)
print("myList:", myList)
print("myList2:", myList2)
# another way to make a copy is to use the built-in 
# list()

# joinList -> what is join List?
# several ways to join or concatenate, two or more
# lists in python
# using +
print("Using + operator")
list3 = myList + myList2
print("list3: ",list3)
# append()
for x in myList2:
    list3.append(x)
print("list3 appended:", list3)
# use extend() method, add elements from one list 
# to another list. 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# append, clear, copy, count, extend, index
# insert, pop, remove, reverse, sort


