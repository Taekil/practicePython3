# a lambda function is a small anonymous function
# a lambda function can take any number of arguments
# but can only have one expression. 

"""
Syntax
lambda arguments: expression
"""
# the expression is executed and the result is returned. 
# example. 
# add 10 to argument a, and return the result:
x =  lambda a : a + 10
print(x(5))

# lambda is a way to crate small anonymous function in Python
# the shorten way to define a function without using def. 

"""
Q: lambda in lambda or lambda in class in possible?
Yes, it is possible. 
lambda functions can be used as arguments to other functions
or as elements in lists, dictionaries, and other data structures. 

    sum = lambda a, b: a + b
    product = lambda a, b: a * b
    apply_operation = lambda x, y, operation: operation(x, y)

    print(apply_operation(2, 3, sum)) # output: 5
    print(apply_operation(2, 3, product)) # output: 6

apply_operation lambda function takes in two numbers and a 
function as arguments, and applies the function to the numbers. 
at the operation, sum or product will be applied as operator.

class MyClass:
    def__init__(self):
        self.my_lambda = lambda x: x**2
    
    def apply_lambda(self, x):
        return self.my_lambda(x)
"""

# multiple arguments
x = lambda a, b: a * b
print(x(5, 6))

# summarize argument a, b, and c and return the result
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# why use lambda functions?
# the power of lambda is better shown when you use thme as 
# an anonymouse function insisde another function

def myfunc(n):
    return lambda a: a * n
myDoubler = myfunc(2)
print(myDoubler(11))

# the code creates a function called myfunc returning a lambda function
# the lambda function takes in an arguement a and multiplies by the value of n
# myDoubler is assgined to the lambda fucntion return myfunc(2)

# the example lambda with recursion
factorial = lambda n:1 if n == 0 else n * factorial(n-1)

# factorial lambda function takes in an arguement n and returns
# the factorial of n. the function uses recursion to calculate the factorial, 
# by calling itself with n-1 until it reacehs the base case where n is equal to 0

fibonacci = lambda n: n if n <=1 else fibonacci(n-1) + fibonacci(n-2)

# 

# additional example lambda with recursion and memoization
# it is possible but not recommended...to long and not easy to read. 
factorial_dict = {}
factorial = lambda n: 1 if n == 0 else factorial_dict[n] if n in factorial_dict else factorial_dict.setdefault(n, n * factorial(n-1))
print(factorial(5)) # Output: 120

# some examples of simple transformations and filtering operations
# on data structures suing lambda functions
my_list = [1, 2, 3, 4, 5]
double_list = list(map(lambda x: x * 2, my_list))
print(double_list)
# the map() function applies a function to each element of a list
# and return s a new list with the results. 
# lambda functions are commonly used with map() to apply a simple
# transformation to each element of a list. 

even_list = list(filter(lambda x: x % 2 == 0, my_list))
print(even_list)
# finter() be used to return a new list
# with only the elements that meet a ceratin condition. 

# lambda functions are commonly used with sort()
# so specify a custom sorting order based on a certain key
my_list = ["Apple", "Banana", "Cherry", "Date"]
my_list.sort(key = lambda x: len(x))
print(my_list)