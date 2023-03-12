# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:08:20 2022

@author: Asus
"""

"""

Mathematical operation using NumPy functions and operators:
1) + operator for addition 
2) np.add() NumPy function
3) - operator for subtraction
4)/ operator for division
5) np.divid() NumPy function
6) * operator for for elementwise matrix multiplication
7) np.multiply() for elementwise matrix multiplication
8) @ operator for matrix product
9) np.dot() for matrix product
10) np.max() & np.min() for find maximum and minimum value from array
11) np.argmax() & np.argmin() for find index of maximum and minimum value of array
12) np.sum() to calculate sum of array
13) np.mean() to calculate average of array
14) np.std() to calculate standerd division of array
15) np.exp()  to calculate exponent of array element
16) np.log()  to calculate natural logof array element
17) np.log10()  to calculate og to base 10 of array element

"""

import numpy as np
arr1=np.arange(1,10).reshape(3,3)
arr2=np.arange(1,10).reshape(3,3)
print(arr1)
print(arr2)

print(arr1+arr2)
print(np.add(arr1, arr2))


print(arr1-arr2)
print(np.subtract(arr1,arr2))

print(arr1/arr2)
print(np.divide(arr1,arr2))

print(arr1*arr2)
print(arr1 @ arr2)

print(arr1.dot(arr2))

print(arr1.max())
print(arr1.max(axis = 0))
print(arr1.argmax())

print(arr1.min())
print(arr1.min(axis = 0))
print(arr1.argmin())

print(arr1.sum())
print(arr2.sum())
np.sum(arr1)

np.sum(arr1, axis=0)

print(arr1.mean())
print(arr2.mean())

np.sqrt(arr1)

np.std(arr1)
np.std(arr2)

np.exp(arr1)
np.exp(arr2)

np.log(arr1)


np.log10(arr1)





