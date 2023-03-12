# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:23:28 2022

@author: Asus
"""
"""
1) Creating empty Series
2) Creating Series from list
3) Creating Series from scalar value
4) Creating Series from Python Dictionary
5) Mathematical Operations in Series
6) Slicing in Series
7) Handling Missing Data
"""

import pandas as pd

list_s=[1,2,3,4,"Sumanta Dey"]
print(list_s)

series1=pd.Series(list_s)
print(series1)

type(series1)

series2=pd.Series([1,2,3,4,5])
print(series2)

empty_s=pd.Series([])
print(empty_s)

series3=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(series3)

series3=pd.Series([1,2,3,4,5], dtype=float)
print(series3)

series3=pd.Series([1,2,3,4,5], index=['a','b','c','d','e'], dtype=float, name="Data values")
print(series3)

scalar_s=pd.Series(0.5)
print(scalar_s)


scalar_s=pd.Series(0.5, index=[1,2,3,4,5])
print(scalar_s)

dict_s=pd.Series({'a':1,'b':2})
print(dict_s)

s4=pd.Series([1,2,3,4,5])
print(s4)

s4[0]
s4[1]
s4[3]

s4[0:3]

max(s4)

min(s4)

s4[s4>3]

s4

s5=pd.Series([1,2,3,4,5])
s4+s5

s6=pd.Series([1,2,3])
s5+s6
