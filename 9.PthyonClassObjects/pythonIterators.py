# python iterators
# https://www.w3schools.com/python/python_iterators.asp
# what is iterators?
# an interaor is an object that contains a contable number of values
# __inter__() and __next__()

# Iterator vs Iterable
# lists, tuples, dictionaries, and sets are all iterable objects. 
# iterable containers which you can get an iteraor form. 

# iter() method

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # return an iterator form a tuple -> print each value

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# looping through an iterator
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
    print(x)

mystr = "banana"
for x in mystr:
    print(x)


"""
create an iterator
__iter__() and __next__()

the __iter__() -> we can operations (initializing etc) but must always return
the iterator object itself. 

the __next__() -> allows us to do operations, and must return the next item
in the sequence. 
"""

class MyNumbers:
    def __iter__(self):
        self.a = 1
        print(self.a)
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myIter = iter(myclass)

print(next(myIter))
print(next(myIter))
print(next(myIter))

class MyNumbers2:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = MyNumbers2()
myiter = iter(myClass)

for x in myiter:
    print(x)

"""
why do we need iterator object?
to access elements from a collection or sequence one at a time. 

Data processing? building a data processing pipeline where each step of the 
pipeline is represented by an iterator object. 
This could involve reading data from different sources, applying transformations
or filters, and producing the final result. 
Practice chaining iterator objects together to create a modular and efficient
data processing system. 

Custom Data structures? 

stream processing: 
a stream in real time such as reading log files or processing live sensor data
fetch data from the stream, and design your processing logic to consume and
process the elements as they become available. 

algorithmic problems
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    # basic sigly linked list. 
    # it has a head attribute that points to the 
    # first node in the list. 
    # the append() method is used to add new nodes to the 
    # end of the list
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    # to make the linke list iterable, 
    # we implement the __iter__() and __next__()
    # In __inter__(), we initialize the "current" attribute to the head of 
    # the list and return "self", the instance of the linked list, 
    # as the iterator object.
    def __iter__(self):
        self.current = self.head
        return self
    
    # we retrieve the data of the current node, move the current pointer to the
    # next node, and return the data. If current become None, we raise 
    # StopIteration. 
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data
    