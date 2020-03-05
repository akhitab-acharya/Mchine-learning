# CHECKING ADDRESS AND SIZE OF TWO VARIABLES

import numpy as np

a = np.arange(10)
a

b = a[::2]
b

print(a.data)
print(b.data)

import struct
from sys import getsizeof

print(getsizeof(a))
print(getsizeof(b))

------------------------------------

#DOT PRODUCT

import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

---------------------------------

#SUM:

import numpy as np

x = np.array([[1,2],[3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

-------------------------------------------------------------------------
#TRANSPOSE OF MATRIX:

import numpy as np

x = np.array([[1,2], [3,4]])
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3

-------------------------------------------------------------------------

#FOR COMPLEX NUMBER:

c = np.array([[1,2], [3,4]], dtype = complex)
c

OUTPUT:
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])

----------------------------------------------------------------

# cumulative sum:

print(b.cumsum())
print(b.cumsum(axis = 0))
print(b.cumsum(axis = 1))

--------------------------

