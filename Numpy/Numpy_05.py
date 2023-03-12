# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:57:11 2022

@author: Asus
"""

"""
In this tutorial we explain Python NumPy array concatenation and array split in Hindi :
1) NumPy concatenate - np.concatenate()
2) NumPy vstack - np.vstack()
3) NumPy hstack - np.hstack()
4) NumPy split - np.split()

"""
import numpy as np

sd=np.arange(1,17).reshape(4,4)
print(sd)

sd2=np.arange(17,33).reshape(4,4)
print(sd2)

list1=[2,3,4,5]
list2=[7,8,9,2]

list1+list2

sd+sd2

sdd=np.concatenate((sd,sd2))
print(sdd)

sdd1=np.concatenate((sd,sd2), axis=1)
print(sdd1)

np.vstack((sd,sd2)) #for vartical

np.hstack((sd,sd2,sd,sd2)) # for horizontal

sd0=np.split(sd,2)
print(sd0)
type(np.split(sd,2))

sd0[0]
type(sd0[0])


np.split(sd,2, axis=1)

d1=np.array([4,5,6,7,8])

np.split(d1, [1,3])






