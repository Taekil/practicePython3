# python while loops and for loops
# primitive two loops commands

# One way to simulate a do-while loop in python 
"""
while True:
    if condition:
        break
"""
# another way to simulate a do-while loop in python
# use recursion, with a technique where a function calls
# itself repeatly until a certain condition is met. 
"""
def my_loop():
    if condition:
        return
    my_loop()
"""
# while loop 
i = 1
while i < 6:
    print(i)
    i += 1

# break statement
i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i += 1

# the continue statement
# with theh continue statement we can stop the current
# iteration, and continue with the next:
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    # i is 3, the print(i) is skipped for that iteration
    # but the loop continues to run for the next value
    # of i
    print(i)
# 1 2 4 5 6 # number 3 is missed in tht result

# the else statement
# with the else statement can run a block of code 
# once whne the conditioni no longer True:

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# after the loop has finished running, the 'else' block
# will be executed, which will print the message
# this is the loop condition evetually becomes false
# when i is incremented to 6 there are no 'break'
# statement to exit the loop early. 


