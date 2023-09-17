# https://www.w3schools.com/python/python_dictionaries_change.asp
# python change dictionary items

# change values
# thisDict["year"] = 2018

# update dictionary
thisDict ={
    "brand": "K",
    "model": "EV9",
    "year": 2023
}
print(thisDict.values()) # before update
thisDict.update({"year":2024}) # update() will update 
# the dictionary with the itmes from the given
print(thisDict.values()) # after update

# add item, thisDict["color"] = "red"
# add an item to the dictionary is done by using new index
# thisDict.update({"color":"red"})
# add a color item to the dictionary by using update() method

# remove items
# pop()
thisDict.pop("model")
print(thisDict)

# popitem() method removes the last inserted item
thisDict.popitem()
print(thisDict)

thisDict ={
    "brand": "K",
    "model": "EV9",
    "year": 2023,
    "color":"grey",
    "type": "electric"
}

# del keyword remove the item with the specific key name:
# the del keyword can also delete the dictionary completely
# clear() method makes empty the dictionary

#loop through dctionary
# print all key names
for x in thisDict:
    print(x)

# print all values in the dictionary
for x in thisDict:
    print(thisDict[x])

# we can also use the values() method to return values of a dictionary
for x in thisDict.values():
    print(x)

# keyword return
for x in thisDict.keys():
    print(x)

# loop through both keys and values, by using the items() method
for x, y in thisDict.items():
    print(x, y)

