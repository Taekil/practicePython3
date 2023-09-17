# python if...else
# if statement
a = 33
b = 200
if b > a:
    print("b > a") # indentation(White space a the
                   # the beginning of a line
                   # to define scope in the code
elif a == b:
    print("a == b")

else:
    print("not any cases")

if a > b: print("")

print("A") if a > b else print("B")
# one line if else statement, with 3 conditions:
print("A") if a > b else print("=") if a == b else print("B")

# 'and' is a logical operator, used to combine conditional 
# statement
a = 200
b = 100
c = 300
if a > b and c > a:
    print("c > a > b") # both conditions are true

# 'or' : at least one of the condition is True
# 'not': not 
if not a > b:
    print("a is not Greater than b")

# nested if
x = 41
if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
    
# pass statement 
# if statement cannot be empty, but if you 
# for some reason have an if statement with no 
# content, put in the pass statement to avoid getting an
# error. 
a = 30
b = 200
if b > a:
    pass




