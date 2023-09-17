"""
https://www.w3schools.com/python/python_dictionaries.asp

* dictionary itmes are ordered, changeable, and 
but do not allow duplicates. 
"""
thisDict = {
    # basic dict form
    'brand' : "Ford",
    'model' : "Mustang",
    'year' : 1964
}
# create and print a dictionary
print(f"thisDict: {thisDict}")
# Here is not-understandable syntax. 
# f-string accept only '' instead of ""?
# the quotes inside the f-string. 
# using single quotes 
print(f"brand: {thisDict['brand']}")
print(thisDict["brand"])

#duplicates Not Allowed
thisDict2 = {
    # basic dict form
    'brand' : "Ford",
    'model' : "Mustang",
    'year' : 1964,
    'year' : 2020
}
print(f"thisDict2: {thisDict2}") # overwrite year
print("the number of items: ", len(thisDict2)) # length, how many items

# Data Types
# string int boolean and list
thisDict3 = {
    'brand' : "Ford",
    'model' : "Mustang",
    'electric': False,
    'year' : 1964,
    'colors': ["red", "white", "blue"]
}
print(f"thisDict3: {thisDict3}")

# the type() -> return <class 'dict'>
print(type(thisDict3))

# the dict() constructor
thisDict4 = dict(name="John", age = 36, country = "Norway")
print("thisDict4:", thisDict4)

