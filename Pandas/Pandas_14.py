# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:47:25 2022

@author: Asus
"""

"""
loc
iloc
"""
import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df0)

df0.loc[0]
df0.loc[10]
df0.loc[[0,1,2]]
df0.loc[[4,8,7]]
df0.loc[4,'Student ID']
df0.loc[0:3,'Date']
df0.loc[0:10,'Student ID']
df0.loc[[False,False,False,False,False,False,False,False,False,False,False]]
df0.loc[df0['Class']<10]
df0.loc[df0['Class']<10,['Percentage']]


df0.iloc[0]
df0.iloc[[0]]
df0.iloc[:,0]
df0.iloc[[0,1]]
df0.iloc[[True,False,True]]