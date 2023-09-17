# https://www.w3schools.com/python/python_functions.asp
# python functions
# a block of code which only runs when it is called. 
# a function can return data as a result. 

# Creating a function
# using def key word
def my_function():
    print("hello from a function")

# To call a fucntion use the function name followed by parenthesis
my_function()

# argument
# information can be passed into functions as arguements
# argueemtns are specified after the function name, inside the parentheses
# add as many arguments as you want, just sperated them with a comma

def my_function(fname):
    print(fname + "Refses")
# function call with argument
my_function("Email")

"""
the function should get 2 arguement when the function wants 2 arguments
if you try to call the function with 1 or 3 arguments, I will get error
"""

# arbitrary arguements, *args
# This way the functioni will rececive a tuple of arguments
# and can access the items accordingly
def my_function(*kids):
    print("the Youngest Child is " + kids[2])

my_function("emil", "tobias", "linus")
# the expected return is, linus

# keyword arguments
def my_function(child3, child2, child1):
    print("the yougest child is " + child3)

my_function(child1= "emil", child2= "tobias", child3= "linus")
# this also has same expected return. 
# keyword arguement -> kwargs in python documentations

# arbitrary keyword arguments, **kwargs
# two asterisk, ** before the paramenter name in the function definition. 
# this was the function will recieve a dictionary of arguments, 
# and can access the items accrodingly. 
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "tbobias", lname = "Refs")
# **kwargs, arbitrary kword arguements are in python documentations. 

"""
*kwargs and **kwargs: Special syntax in Python
allowing a function to accept a variable number of arguments. 

addtional examples for *kwargs and **kwargs

def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {values}")

example_function(name="Alice", age = 30, city = "NY")

expected output, 
name = Alice
age = 30
city = NY

**kwargs allows the function to accept a variable number of 
keyword arguements, the keyword arguments are passed as a dictionary to
the function, and the function iterates over the dictionary to print each
key-value pair

def example_function(*args):
    for arg in args:
        print(arg)

example_function("Alice", 30, "NY")

expected output, 
Alice
30
NY

*kwargs is used to pass a variable number of non-keyword arguments
to a function. It allows the function to accept any number of non-keyword
arguments as a tuple. 
"""

# Default Paramenter Value
# the following example shows how to use a default parameter value
# if we call the fuction without arguemnt 
# it uses the default value:

# default value is "Norway"
def my_function(country = "Norway"):
    print("I am from" + country)

my_function("Sweden")
my_function("India")
my_function() # default value returns
my_function("Brazil")

# passing a list as an arguement
# send any data types of argument to a function
# string, number, list, dictionary etc
# and it will be treated as the same data type inside the function

def my_function(food):
    for x in food:
        print(x)
fruits = ["Apple", "Banana", "Cherry"]
my_function(fruits)

# return values
# return statement
def myfunction(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(7))

# The pass statement
# function definitions cannot be empty, but if 
# you for some reason have a function definition with no content
# put in the pass statement to avoid getting an error. 
def myfunction():
    pass

# recursion
# python also accepts functions recursion, which means a defined function
# call itself. 

# tri_recursion() 
# we use the k variable as the data
# which decrements(-1) eavery time we recurse. 
# the recursion ends when the condition is not greater than 0
# to a new developer it can take some time to work out how 
# exactly this works, best way to find out is by testing and modifying it. 
def tri_recurion(k):
    if k > 0:
       result = k + tri_recurion(k-1)
       print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recurion(6)

# expected return, 1 3 6 10 15 21 












