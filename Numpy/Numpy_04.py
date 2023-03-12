# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:44:05 2022

@author: Asus
"""

"""

In this tutorial we explain How to Slice NumPy Array  in Hindi and describe these questions:
.1) np.arange()
2) np.arange().reshape()
3) Slicing – [:, 0],   [:, 0:1],   [1:4, 1:4],   [:, 1:3],   [::],   [:,:]
4) np.itemsize


"""

import numpy as np

arr=np.arange(1,101).reshape(10,10)
print(arr)

arr[0,0]
arr[4,5]

arr[0,0].ndim   # to get dimension

arr[0].ndim
arr[2].ndim


arr[:,0] # in 1 dimansion

arr[:, 0:1] # for 2 diman
arr[:, 0:1].ndim

arr
arr[1:4, 1:4]

arr[3:8,3:8]

arr[:,1:3]

arr[:]
arr[::]
arr[:,:]


arr.dtype
arr.itemsize



























