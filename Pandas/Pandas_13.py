# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:56:40 2022

@author: Asus
"""

"""
Parameters of interpolate
interpolate axis
interpolate limit
interpolate limit_direction
interpolate limit_areea
interpolate inplace
"""



import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df0)

df0.interpolate()
df0.dtypes
df0.interpolate(limit=1)
df0.interpolate(limit=2)
df0.interpolate(limit=1,limit_direction='backward')
df0.interpolate(limit=2,limit_direction='backward')
df0.interpolate(limit=1,limit_direction='both')
df0.interpolate(limit_area='inside')
df0.interpolate(limit_area='outside')
df0
df0.interpolate(inplace=True)
df0
df0
