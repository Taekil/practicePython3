# https://www.w3schools.com/python/python_scope.asp
# python Scope
# a variable is only availabe from inside the region it is created. 
# "scope"
 
# local scope
# a variable -> belongs to the local scope of that function. 
# only be used "inside that function"
def myFunc():
    x = 300
    print(x)

myFunc()

# the local variable can be accessed from a function within the function,
def myFunc():
    x = 300
    def myInnerFunc():
        # it is availabe for any function inside the function
        print(x)
    myInnerFunc()
myFunc()

# global scope
# a variable created in the main body of the python code 
# a global variable and belongs to the global scope. 
# global variable s are available from within any scope, global and local. 
x = 300

def myFunc():
    print(x)

myFunc()

print(x)

# Naming variables.
# if you operate with the same variable name insde and outside of a function, 
# python will treat them as two separate variables. 
x = 300

def myFunc():
    x = 200
    print(x)

myFunc()

print(x)

# global keyword
# if you need to create a global variable, but are stuck in the local scope, 
# you can use the global keyword
# the global keyword makes the variable global. 

def myFunc():
    global x
    x = 300

myFunc()
print(x)

# also, use the global keyword if you want to make a change to a global
# variable inside a function. 
# to change the value of a global variable inside a function, refer to the 
# variable by using the global keyword, 
x = 300
def myFunc():
    global x
    x = 200

myFunc()
print(x)




