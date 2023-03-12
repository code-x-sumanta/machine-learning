# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 20:50:17 2022

@author: Asus
"""

"""
Pandas fillna
Parameters of fillna
fillna value
fillna methods
fillna axis
fillna inplace
fillna limit
"""
    
import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df0)

df0.fillna(0)
df0.fillna(4)


df0.fillna({'Grade':'S'})

df0.fillna(method='ffill')

df0.fillna(method='pad')

df0.fillna(method='bfill')

df0.fillna(method='ffill',axis=0)
df0.fillna(method='ffill',axis=1)


df0.fillna(method='bfill',axis=0)
df0.fillna(method='bfill',axis=1)

df0.fillna(0,limit=1)
df0.fillna(0,limit=2)



df0.fillna(method='ffill',limit=0)
df0.fillna(method='ffill',limit=1)

















