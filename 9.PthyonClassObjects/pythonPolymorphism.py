# the word polymorphism -> many forms
# string
# function polymorphism
# for string len() returns the number of characters. 
x = "Hello World"
print(len(x))

# for tuple len() returns the number of times in the tuple.
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) 

# Dictionary
thisDict = {
    "brand" : "Ford",
    "Model" : "Mustang",
    "Year" : 1964
}
print(len(thisDict))

# class polymorphism. 
# usage with class methods. 
# having multiple classes with the same method name. 

# called move():
class Car: 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 =Car("Ford", "Mustang") # create a car class
boat1 = Boat("Ibiza", "Touring 20") # Create a Boat Class
plane1 = Plane("Boeing", "747") # Create a plane class

for x in (car1, boat1, plane1):
    x.move()

# inheritance class polymorphism
# classes with child classes

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("move")

# child classes inherits the properties and mothods from the parent class    
# pass but it inherits brand, model, and move() from vehicle
class Car(Vehicle):
    pass

# the Boat and Plane classes also inherit brand model and move()
# from vehicle but they both override the move() method
class Boat(Vehicle):
    def move(self):
        print("sail")

class Plane(Vehicle):
    def move(self):
        print("fly")

car2 = Car("Ford", "Mustang")
boat2 = Boat("Ibiza", "Touring 20")
plane2 = Plane("Boeing", "747")

for x in (car2, boat2, plane2):
    print(x.brand)
    print(x.model)
    x.move()


