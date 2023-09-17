# what is modules?
# a module to be the same as a code library
# a file containing a set of functions you want to include
# in your application. 

# Create a Module
# to create a module just save the code you want in a file
# with the file extension .py
import mymodule

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

# this example to import a module by using "as" keyword
import mymodule as mx # create an alias for mymodule called mx
a = mx.person1["age"]
print(a)

# Built-in Modules
# there are several built-in modules in python, 
# which you can import whenever you like. 

import platform
x = platform.system()
print(x)

# using the dir() function. 
x = dir(platform)
print(x)

# Import From Module
# we can choose to import only parts from a module, by using from keyword
# import only the person1 dictionary from the module
from mymodule import person1
print(person1["age"])




