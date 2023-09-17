# python inheritance. 
# https://www.w3schools.com/python/python_inheritance.asp

"""
python inheritance
allows us to define a class that inehrits all the methods
and properties from another class. 

parent class: inherited from, called base
child class: inherits from another class, called derived 
"""

# create person, first name, last name, and print name. 
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    
    def printFullName(self):
        print(f"{self.last_name}, {self.first_name}")
        # not f "", after f there is no whitespace. 

p1 = Person("John", "Doe")
p1.printFullName()

# create a child class
# using the pass keyword when you do not want to add 
# any other properties other methods to the class
class Student(Person):
    pass

s1 = Student("Mike", "Olsen")
s1.printFullName()

# adding the __init__() function
# instead of pass keyword

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

# using the super() function
# super() function that will make the child class
# inherit all the methods and properties from its parent. 
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
# By using the super() function, you do not have to use the name of 
# the parent element, it will automatically inherit the methods
# and properties from its parent. 

class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def printFullName(self):
        print(f"{self.last_name}, {self.first_name}")


class Student(Person):
    def __init__(self, fname, lname, student_id):
        super().__init__(fname, lname)
        # adding properties
        # adding student ID to the student class
        self.student_id = student_id
        self.graduationYear = 2019

s1 = Student("Mike", "Olsen", 12345)
s1.printFullName()
print(s1.student_id)

class Student(Person):
    def __init__(self, fname, lname, student_id, gYear):
        super().__init__(fname, lname)
        # adding properties
        # adding student ID to the student class
        self.student_id = student_id
        # adding graduationYear as variable
        self.graduationYear = gYear

    def welcome(self):
        print(f"welcome, {self.first_name}, {self.last_name}, ")
        print(f"to the class of {self.graduationYear}")
    
"""
class Person:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def printFullName(self):
        print(f"{self.last_name}, {self.first_name}")


class Student:
    def __init__(self, student_id):
        self.student_id = student_id


class Classmate(Person, Student):
    def __init__(self, fname, lname, student_id, class_name):
        Person.__init__(self, fname, lname)
        Student.__init__(self, student_id)
        self.class_name = class_name


c1 = Classmate("John", "Doe", 12345, "Math")
c1.printFullName()
print(c1.student_id)
print(c1.class_name)
"""

