# TAEKIL OH
# SEP 04TH 3023
# NumPyNormalDistribution.py

# Normal(Gaussian) Distribution
# Normal Distribution
# one of hte most important distributions. 
# random.normal() method to get a Normal Data distribution. 
# loc: (mean)peak of the bell exist
# scale: (standard deviation) how flat the graph distribution 
# size: the shape of the returned array. 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.normal(size=(2, 3))
print(x)

# size 2X3 with mean at 1 and standard deviation of 2
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# visualization of Normal Distribution
sns.distplot(random.normal(size=1000), hist=False)
plt.show()

# Binomial Distribution: Discrete Distribution(n, p, size)
# Poisson Distribution: 
# Uniform Dsitribution:
# Ligistic
# Multinomial
# Exponential
# Chi Square
# Rayleigh
# Pareto
# zipf





