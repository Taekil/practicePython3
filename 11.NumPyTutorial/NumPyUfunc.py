# NumPy ufunc
"""
what are ufunc? Universal functions ndarray for object operation

where dtype out
"""
# vectorization
# coverting iterative statements into a vector based operation is called
# faster as modern CPU are optimized for usch operations. 

# add the elements fo Two Lists. 
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
# using zip() (python built-in)
for i, j in zip(x, y):
    z.append(i + j)
print(z)

import numpy as np 
# using add() function 
z = np.add(x, y)
print(z)

# create own ufunc
def myadd(x, y):
    return x + y

# frompyfunc() has function, inputs, and outputs. 
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))

# check function is a ufunc
print(type(np.add)) # return <class 'numpy.ufunc'>
print(type(np.concatenate)) # return <class 'builtin_function_or_method'>

if type(np.add) == np.ufunc:
    print('add is ufunc')
else:
    print('add is not ufunc')




