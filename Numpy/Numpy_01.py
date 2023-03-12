# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 19:05:17 2022

@author: Asus
"""

import numpy as np
arr_1d = np.array([1,2,3,4])
print(arr_1d)

type(arr_1d)
arr_1d.ndim

arr_2d = np.array([[1,2,3,4,],[5,6,7,8]])
print(arr_2d)

type(arr_2d)
arr_2d.ndim

arr_1d.size
arr_2d.size

arr_1d.shape
arr_2d.shape   #(row, colomn)

arr_1d.dtype
arr_2d.dtype


np.ones(5)
print(np.ones(5))

print(np.ones((3,4), dtype = int))


print(np.zeros((3,4), dtype = int))
print(np.zeros((3,4), dtype = bool))
print(np.zeros((3,4), dtype = str))
print(np.ones((3,4), dtype = bool))
print(np.ones((3,4), dtype = str))

import numpy as np
ex_mx=np.empty((3,3))
print(ex_mx)

np.empty((3,3))
print(np.empty((3,3)))
