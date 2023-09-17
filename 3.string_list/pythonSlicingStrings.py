# python_Slicing Strings

# slicing: return a range of characters by using 
# slice syntax, the first character has index 0
b = "Hello, world"
print("Slice[2:5]: ", b[2:5])
# slice from the start
print("Slice from the start: ", b[:5])
# slice to end
print("Slice to end: ", b[2:])
# negative indexing
print(b[-5:-2])
# modifying strings
print("upper modify:", b.upper())
print("lower modify:", b.lower())
b2 = "   Hello, world   "
print("remove white space from the begining or the end:", b2.strip())
#replacing
print(b2.replace("H", "J"))
print(b2.split(","))

# string concatenation
# what is concatenation? 
# inaddition to string concatenation, you can also
# concatenate other sequence types. 
# concatenation is the process of combining two or
# more strings or other sequences into a sinlge string
# sequence. 
a = "Hello"
b = "World"
c = a+b
print(f"Test c = a + b: {c}")
c = a + " " + b
print(f"Test c = a + \" \" +  b: {c}")

# formatting string
# what is formatting
# we can not combine strings and numbers like
# txt = "1232" + 123
# so format() method the passed arguements, formats them. 
age  = 36
txt = "My name is TK, and I am {}"
print(txt.format(age))
#format() -> unlimited number of arguements
quantity = 3
itemNo = 567
price = 49.54
myOrder = "I want {} pieces of item {} for {} dollars."
print(myOrder.format(quantity, itemNo, price))
myOrder = "I want {2} pieces of item {1} for {0} dollars."
print(myOrder.format(quantity, itemNo, price))
# Escape Characters
txt = "we are the socalled \"vikings\" from the north. \n"
# \', \\. 
# string method: all string methods return new values. 
# they do not change the original string. 
# capitalize() first into upper
# casefold() into lower
# casefold() is more aggressive than lower()
# it coverts a string to lowercase using a more
# aggressive algorithm that is designed to work corretly
# for all unicode characters, including those in 
# non-english or scripts. 
# center() return a centered string
# count()
# encode() -> encoded version?
# string.encode(encoding=encoding, errors=errors)
# endswith() true if the string ends with the sepecific value
# index()
# is~~~() methods: alnum, alpha, decimal, digit, 
# lower, identifier, lower, numeric, space, printable
# istitle() methods

# what is titile, and what is identifier
# title? the first letter of each word capitalized. 
# hello world -> Hello World
# istitle() -> another built-in string method -> 
# returns "True" if a string is in title case.
# example, Hello World -> true
# but, Hello world -> false

# ASCII -> 
# to validate user input, filter out unwanted characters, 
# or sanitize text data. 
# text validation: accepting user input through a form or 
# other input field -> you might want to validate
# that  the input contain only printable characters and
# reject any input that contains non-printable characters. 
# 1. Text validation
# 2. text filtering
# 3. text sanitization: displaying user-generated content
# on a websize or other public platform, you might to 
# sanitize the text to remove any non-printable charaters

"""
import string
def sanitize_text(text):
    printable_chars = set(string.printable)

    sanitized_text = "".join(filter())
    
    return sanitized_text

dirty_text = 
clean_text = sanitize_text(dirty_text)
"""

"""
isidentifier(): returns true if the string is a valid
identifier? -> a name given to a variable, function, or 
class, and it must satisfy certain rules in python. 

one of usage example. 

validating user input. 
if you are writing a program that allows users to input 
names ro identifiers, you can use isidentifier() to 
validate the input and ensure that it follows the rules
for valid identifiers in python. 
"""