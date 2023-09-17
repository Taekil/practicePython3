"""
try block lets you test a block of code for errors. 
the except block lets you handle the error. 
the else block lets you execute code when htere is no error. 
the finally block lets you execute code, regardless of the 
result of the try- and except blocks. 
"""
"""
exception handling.
when an error occurs, or exception as we call it, python
will normally stop and generate an error message. 
"""
try:
    print(x)
except:
    print("An exception occurred") # raise an error
                                   # x is not defined

# Many exceptions
# We can define as many exception blocks as  we want, 
# e.g. if you want to execute a special block of code
# for a special kind of error. 
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# else
# useing else keyword to define a block of code to be 
# executed if no errors were raised.
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong") # not generated any error

# finally
# if specified, the finally block will be executed
# if the try block raises an error or not. 
try:
    print(x)
except:
    print("Something went wrong")
    # the finallya block gets executed no matter if the try
    # block raises any errors or not
finally:
    print("The 'try except' is finished")
"""
Something went wrong
The 'try except' is finished
"""

# This can be useful to close objects and clean up resources
# try open and write to a file that is not writable
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except: 
    print("Something went wrong when opening the file")

# the program can continue, without leaving the file object open. 

# Raise an exception.
# we can shoose to throw an exception if a condition occurs. 
# to thorow(or raise) an exception, use the raise keyword. 
x = -1
if x < 0:
    raise Exception("Sorry, No numbers below zero")

# the raise keyword is used to raise an exception.
# you can define what kind of error to raise, and the text
# to print to the user. 

x = "Hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")


  





