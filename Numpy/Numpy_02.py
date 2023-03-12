# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:59:33 2022

@author: Asus
"""

"""
1) np.arange() Python NumPy Function
2) np.linspace() Python NumPy Function
3) np.reshape() Python NumPy Function
4) np.ravel() Python NumPy Function
5) np.flatten() Python NumPy Function
6) np.transpose() Python NumPy Function

"""

import numpy as np

# arange(start,end,step)

range_fun=np.arange(1,10,1)
print(range_fun)

# for even 
range_fun2=np.arange(1,10,2)
print(range_fun2)

# linspace is used to get same differance of values at any point

#linspace_fun3=np.linspace(1,6,4)
print(np.linspace(1,6,4))

# reshape func is used to convert one dimansion to another
arr_2d=range_fun.reshape(3,3)
print(arr_2d)

arr_2d=range_fun.reshape(1,3,3)
print(arr_2d)


arr=np.arange(1,13,1).reshape(2,6)
print(arr)

#ravel is used to convert multidimansional array to one dimansion
arr_2d.ravel()
print(arr_2d.ravel())
