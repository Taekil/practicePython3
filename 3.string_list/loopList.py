#python_loopingList
# forLoop
thisList = ["apple", "banana", "cherry"]
for x in thisList:
    print(x)

# through index number
for i in range(len(thisList)):
    print(thisList[i])

#using a whileLoop
i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1

# looping using list comprehension
[print(x) for x in thisList]

# what is list comprehension
# list comprehension -> shorter syntax -> create new list
# based on the values of an existing list. 
fruits = ["apple", "banana", "cherry", "dia", "fruit"]
newList = []
for x in fruits:
    if "a" in x:
        newList.append(x)
print(newList)
# with list comprehension
newList2 = [x for x in fruits if "a" in x]
print(newList2)

#syntax = [expression for item in iterable if condition == True]
# for example, newList = [x for x in fruints if x != "apple"]
# only accept items that are not "apple"

# literable
# the iteralbe can be any iterable objects, like a liskt, tuple, set etc. 
newList3 = [x for x in range(10)]
print(newList3)

#accepting only numbers lower than 5:
newList4 = [x for x in range(10) if x < 5]
print(newList4)

# the expression is the current item in the iteration, 
# but it is also outcome, which you can manipulate
# before it ends up like a list item in the new list. 
# set the value in the new list for upper case. 
newList5 = [x.upper() for x in fruits]
print(newList5)
# ['APPLE', 'BANANA', 'CHERRY', 'DIA', 'FRUIT']
newList6 = ['hello' for x in fruits]
print(newList6)
# ['hello', 'hello', 'hello', 'hello', 'hello']
newlist7 = [x if x != "banana" else "orange" for x in fruits]
print(newlist7)

