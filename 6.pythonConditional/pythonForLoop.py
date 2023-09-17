# python for loops
# used for interating over a sequence
# list, tuple, dictionary, set, string

fruit = ['apple', 'banana', 'cherry']
for x in fruit:
    print(x)

# Even strings are iterable objects,
# they contain a sequence of charaters
for x in "banana":
    print(x) # b a n a n a

# the break statement
# with the break, stop the loop 
for x in fruit:
    print(x)
    if x == "banana":
        break

# anothe break example
for x in fruit:
    if x == "banana":
        break
    print(x)

# continue statement
for x  in fruit:
    if x == "banana":
        continue
    print(x)

# the range() function
# to loop through a set of code a specified number of times
# we can use range() function. 
# the range() function returns a sequence of numbers, 
# starting from 0 by default, and increments by 1(by default)
# and ends at a specfic number

for x in range(6):
    print(x)

# range(6) is values 0 to 5
# range(2, 6) -> 2 3 4 5 
# increment the sequence with 3(defualt is 1):
for x in range(2, 30, 3):
    print(x) # 2 (+3) 5 (+3) 8 (+3) 11 (+3) 14 ......29 (not including 30)

# else in For loop
# the else keyword in a for loop
for x in range(6):
    print(x)
# the else block will not be executed if the loop is 
# stopped by a break statement
else:
    print("finally finished")

"""
i = 0
while i < 5:
    i += 1
    if i == 3:
        break
else:
    print("The loop completed normally.")
print("The value of i is:", i)

the loop is terminated by 'break' statement, 
'else' block is not executed. 

The value of i is: 3
"""