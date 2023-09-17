# python_global variables
"""
https://www.w3schools.com/python/python_variables_global.asp
global variables
created outside of a function 
are knonw as global variables. 
can be used by everyone, both inside of function and 
outside variables
"""

# example1
x = "awesome"
def myfunc1():
    print("python is " + x)
myfunc1()
# example2
# create a variable inside a function, with the same name
# as the global variable. 
def myfunc2():
    x = "fantastic"
    print("python is " + x)
# pythone is fantastic
myfunc2()
# python is awesome
print("python is" + x)

# example2
# GLOBAL KEYWORD
# Create Variable Inside a function -> local
# only use insdie the function. 
# but, global keyword -> create a global variable. 
def myfunc3():
    global x
    x = "FANTASTIC"
    # python is FANTASTIC
    print("python is " + x)
myfunc3()
# python is FANTASTIC
print("python is " + x)




