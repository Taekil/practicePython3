# Taekil Oh
# NumPyRandom.py
# SEP 4TH 2023
# random intro

"""
random is meaning is somthing that can not be predicted logically. 

Pseudo Random and True Random
Pseudo Random: Random number generated from through a generation algorithm. 
We need to get the random data from some outside source-> we will make true Random. 
"""

from numpy import random
import numpy as np

xInt = random.randint(100)
print(xInt)
xFloat = random.rand()
print(xFloat)

# Generate Random Array
# randInt() method takes a size parameter where you can specify the shape of an array
xArray_1D = random.randint(100, size=(5))
print(xArray_1D)
print("Datatype", type(xArray_1D)) # checking the data type: 'numpy.ndarray'

xArray_2D = random.randint(100, size=(3, 5))
print(xArray_2D) 
print("Datatype", type(xArray_2D))
# we can also use with rand() method
# x = random.rand(5) and x = random.rand(3, 5)

# Generate Random Number from Array
# choice() method: based on an array of values. 
# takes an array as a parameter and randomly returns one of the values.
x_choice = random.choice([3, 5, 7, 9])
print("return one of the value: ", x_choice)
print("Datatype: ", type(x_choice))

# the choice() meothod also allows you to return an array of values. 
xArray_choice = random.choice([3, 5, 7, 9], size=(3, 5))
print(xArray_choice)
print("the data type of xArray_choice is", type(xArray_choice))

# Random Data Distribution
# What is data Distribution?
"""
data distribution is a list of all possibl values, and how often each 
value occurs.

such lists are important when working with statistics and data science. 
the random module offer methods that returns randomly generated data 
distributions. 
"""
"""
Random Distribution: Probability density function.(a continuous probability)
"""
# the choice() meothod allows use to specify probability for each value
# the probability between 0 and 1. 
# 0 is the value never occur
# 1 is the value alway occur
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size = (100))
# the sum of all probility: 1.0
print(x) # 9 is never occurred. 
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3,5))
print(x)

# Random Permutations
# a permutation refers to an arrangement of elements. 
# [3, 2, 1] -> is a permutation of [1, 2, 3]
# shuffle() and permutation()

arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("random shuffle of array [1, 2, 3, 4, 5]: ", arr)
print("permuation: ", random.permutation(arr))

import matplotlib.pyplot as plt
import seaborn as sns
# what is seaborn: library uses matplotlib underneath to plot graphs. 
# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show() # plotting a distplot

sns.displot([0, 1, 2, 3, 4, 5], kde=True)
plt.show()










