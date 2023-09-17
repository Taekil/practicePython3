# copy dictionary
# false: dict2 = dict1

# dictionary variable, thisDict
thisDict = {
    "brand": "KIA",
}

thisDict.update({"model": "EV9"})
thisDict.update({"type": "Electric"})
thisDict.update({"color": "Grey"})
thisDict.update({"year": 2023})

print("*** Print the thisDict ***")
for x, y in thisDict.items():
    print(x, y)

myDict = dict(thisDict)

print("*** Print the myDict ***")
for x, y in myDict.items():
    print(x, y)

# testing pop()
print("*** myDict.pop('brand') ***")
print(myDict.pop("brand"))

print("*** Print the myDict again ***")
for x, y in myDict.items():
    print(x, y)

# Nested Dictionaries
# create a dictionary that contain three dictionaries
myFamily = {
    "child1" : {
    "name": "TK",
    "year": 2002
    },
    "child2" : {
    "name": "HW",
    "year": 2003
    },
    "child3" : {
    "name": "KK",
    "year": 2004
    }
}

# another form. 
child4 = {
    "name": "TK",
    "year": 2002
}
child5 = {
    "name": "HW",
    "year": 2003
}
child6 = {
    "name": "KK",
    "year": 2004
}

myFamily2 = {
    "child4": child4,
    "child5": child5,
    "child6": child6
}

print(myFamily)
print(myFamily2)

# access items from a nest dictionary, 
# use the name of the nested dictionary and the key
print(myFamily["child2"]["name"])

# can I update the nested dictionaries?
