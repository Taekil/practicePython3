# apr 20th 2023
# python-AccessDictionary items
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisDict["model"]
#get()
y = thisDict.get("model")
#keys()
z = thisDict.keys()
print(x, y, z)

"""
add a new item to the original dictionary, 
and wee the keys list get updated as well. 
"""
car = {
    "brand":"H",
    "model":"A",
    "year":1983
}
x = car.keys()
print(x) # before the change
car["color"] = "white"
print(x) # after the change
# get Values
# values()
# get a list of the values

# make change in the original dictionary, 
# and see that the values list get updated as well
x = car.values()
print(x) # before the changes
car["year"] = 2020
print(x) # after the change 

car2 = {
    "brand": "f",
    "model": "m",
    "year": 1964
}

x2 = car2.values()
print(x2)
car2["color"] = "red" # update the key an value
print(x2)

# get items 
# the items() method will return each item in a dictionary, 
# as tuples in a list
x = thisDict.items()

car3 = {
    "brand": "f",
    "model": "m",
    "year": 1964
}

x = car3.items()
print(x) # before the change
car["year"] = 2020
print(x) # after the change in tuple
"""
what is tuple? myTuple = ("apple", "banana", "cherry")
"""

# how to check if key exists

if "model" in car3:
    print("yes, 'model' is one of the keys")



