from datetime import datetime
from newClass import Square
from newClass import fruit

# author Taekil oh
# date feb 10 2023
# hello.py
# purpose practice python 
# https://www.w3schools.com/python/python_syntax.asp

today = str(datetime.today().date())
print("Hello, World!")
print(f"Today is {today}")

if 5>2:
	print("Five is greater than two!")

#print("Five is greater than two!")
#no internal space causes syntax error

#variable in python

x = 5;
y = "hello, world!"

# https://www.w3schools.com/python/python_comments.asp
"""
This is a comment
Written in more than
one line
"""
print(x)
print(y)

newClass = Square(5)
val = newClass.getVal()
print(val)

newClass = fruit()
newClass.getFruit()

