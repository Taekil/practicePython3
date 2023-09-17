# user input
username = input("Enter username: ")
print("username is: " + username)

# python string formatting
# string format()
# the format() method allows you to format selected parts
# of a string. 
# add a placeholder where you want to display the price
price = 49
txt = "the price is {} dollars"
print(txt.format(price))

# you can add parameters inside the curly brakets to specify
# how to convert the value. 
# format the price to be displayed as a number with two
# decimals. 
txt = "The price is {:.2f} dollars"
"""
txt = "for only {price:.2f} dollars!"
print(txt.format(price=49))

string.format(value1, value2 ......)

the placeholders

txt1 = "My name is {fname}, I'm {age}.".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
"""
"""
formattingh types
:<
:>
:^
:=
.
.
.

https://www.w3schools.com/python/ref_string_format.asp
"""
# multiple values
Quantity = 3
itemNo =567
price =49
myorder = "I want {} pieces of item number {} for {:.2f} dollars"
print(myorder.format(Quantity, itemNo, price))

# https://www.w3schools.com/python/python_string_formatting.asp

# index numbers


