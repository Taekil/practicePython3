# Python Strings. 
# https://www.w3schools.com/python/python_strings.asp
# quatation marks or double quotation markss
# 'hello' is the same as "hello"
print("HelloWorld")
print('HelloWorld')
# assigned string to a variable
a = "Hello"
print(a)
# multiline strings
a = """
    Certainly, here's a sentence using a randomly 
    generated word: "The effervescent bubbles in 
    the sparkling water tickled her nose with their 
    fizzy merriment." The randomly generated word 
    here is "effervescent".
"""
print(a)
# strings are  arrays
a = "Hello, World"
for index in range(len(a)):
    print(f"a[{index}]: {a[index]}")
# looping through a string
for x in "banana":
    print(x)
# string length
print(f"string length of a: {len(a)}")
print("string length of a:",len(a))
# check string
# to check if a certaioni phrase or charater is present
# we can use the keyword in. 
txt = "The best things in lif are free"
print("free" in txt) # true
# using if statement together
if "free" in txt:
    print("Yes, 'free' is present")
# check if NOT
txt = "The best things in life are free"
print("Expensive" not in txt)
# using if statement
txt = "the best things in life are free"
if "expensive" not in txt:
    print("No, expensive is not present")

# not and !=
# != operator to test whether x is not equal to 6
# using not to check if a list is empty
my_list= []
if not my_list:
    print("The list is empty")

# not keyword to negate the truth value of the 'my_list'
# not keyword inverts this to true

# 'in' keyword inpython 
# used as a membership oeprator to test

# a string -> is a sequence of charaters, 
# similar to an array or list. 
# strings are immutable, not be changed. 

