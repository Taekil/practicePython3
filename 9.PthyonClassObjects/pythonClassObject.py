# https://www.w3schools.com/python/python_classes.asp
# python classes and objects
# object oriented programming language
# everython in python is an object, 
# with its properties and methods. 
# a class is like an object consructor, or 
# blueprint for creating objects. 

# create a class. 
# keyword, class
class MyClass:
    x  = 5

p1 = MyClass()
print(p1.x)

class Person:

    # the example s above are classes and objects
    # in their simplest form, and are not really useful
    # in real life applications. 

    # all classes has a function called __init__()
    # which is always executed when the class is being
    # initiated. 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)

# the __str__() function
# returned when the class object is representing as a string. 
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # the string representation of an object with 
    # the __str__() function
    def __str__(self):
        return f"{self.name}({self.age})"
    
p2 = Person2("John", 36)
print(p2)

# object method
# belong to the object. 
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # insert a function that print a greeting
    # execute it on the p3 object
    def myfunc(self):
        print("Hello my name is " + self.name)

p3 = Person3("John", 36)
p3.myfunc()
# note: self parameter is a reference to the current instance of the class
# and is used to access variables taht belong to the class. 
# it does not have to be named self
# you can call it whatever you like, but it has to be the first paramenter
# of any function in the class
class Person4:
    def __init__(mySillyObject, name, age):
        mySillyObject.name = name
        mySillyObject.age = age
    
    def myFunc(abc):
        print("Hello my name is " + abc.name)

p4 = Person4("John", 36)
p4.myFunc

# modify object properties
p1.age = 40

# delete object properties
del p1.age

# delete objects
del p1

# the pass statement
# class definition cannot be empty, but if you for some reason have
# a class definition with no content, but in the pass statement
# to avoid getting an error. 
class Person:
    pass




