# python dates
# import the datetime module and display the current date
import datetime
x = datetime.datetime.now()
print(x)

# date output
# year
print(x.year)
# name of weekday
print(x.strftime("%A")) # why?

# create date objects
# to create a date, we can use the datetime() class(constructor)
# of the datetime module
# the datetime() class requires three parameters to create: year, month, day
x = datetime.datetime(2020, 5, 17)
print(x)

# the datetime object has a method for formatting date objects
# into readable strings.
# the method is called strtime()
# and takes one paramenter, format, to specify the format of the returned
# string, 
x = datetime.datetime(2018, 6, 1)
print(x.strtime("%B"))
# https://www.w3schools.com/python/python_datetime.asp
# a reference of all the legal format codes
# %a, %A, %w, ......

# Built-in Math Function
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

# return the absolute value of the specified number. 
x = abs(-7.25)
print(x)

# pow(x, y)
x = pow(3, 4)
print(x)

# the math module -> built-in module called math, 
# the extended list of mathematical functions. 
import math
x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1

# pi -> math.pi -> 3.14
# https://www.w3schools.com/python/python_math.asp

