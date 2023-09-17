# changeList item
thisList = ["apple", "banana", "cherry"]
thisList[1] = "blackCurrant"
# ['apple', 'blackCurrant', 'cherry']
print(thisList)

newThisList = ["apple", "banana", "cherry", "orange", 
               "kiwi", "mango"]
print("newThisList", newThisList)
newThisList[1:3] = ["blackCurrant", "waterMelon"]
# ["apple", "blackCurrant", "watherMelon", "orange", "kiwi", "mango"]
print("same number of items", newThisList)
newThisList[1:3] = ["redCurrant", "whiteCurrant", "yellowCurrant", "blueCurrant" ]
print("more items",newThisList)
newThisList[1:3] = ["****"]
print("less items", newThisList)
# change the value in a specific range, and insert new values
# in you insert more items than your replacement, 
# the new items will be inserted where your specified, and the 
# remaining items move acorrdingly.
# insert()
print("INSERT(), insert() 'wateMelon as teh third")
print("thisList", thisList)
thisList.insert(2, "waterMelon")
print("thisList, inserted", thisList)

#python add List items
# https://www.w3schools.com/python/python_lists_add.asp
# APPEND()
thisList.append("ORANGE")
print("thisList appended ORANGE", thisList)
tropical = ["mango", "pineApple", "papaya"]
thisList.extend(tropical)
print("thisList extended with tropical", thisList)
# the extend() method -> you can add any iterable obj
# (tuples, sets, dictionaries, etc)

# remove List items
# https://www.w3schools.com/python/python_lists_remove.asp
thisList.remove("mango")
print("removed mango", thisList)
# pop() method -> specified indexs
thisList.pop(1)
print("remove index 1 by pop(1)", thisList)
thisList.pop()
print("remove last item with pop()", thisList)
del thisList[0]
print(thisList)
# del and clear -> del thisList -> delete list
# thisList.clear() -> make empty list
thisList.clear()
print("clear list", thisList)
del thisList
# print(thisList) error message -> not defined. 






