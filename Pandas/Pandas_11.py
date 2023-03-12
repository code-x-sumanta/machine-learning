# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:03:31 2022

@author: Asus
"""

"""
Replace function
"""
    
import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df0)


df0.replace(to_replace='Third Year',value='3rd year')

df0.replace('Third Year','3rd YEAR')

df0.replace(17,27)

df0.replace([1,2,3,4,5,6,7,8],0)
df0.replace([1,2,3,4,5,6,7,8],[11,22,33,44,55,66,77,88])

df0.replace({'Course':'Second Year'}, 'none')
df0.replace({'Course':'Second Year','Grade':'A'}, 'none')


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df0)

df0.replace('[A-Za-z]',0)
df0.replace('[A-Za-z]',0,regex=True)

df0.replace({'Course':'[A-Za-z]'},0,regex=True)

df0.replace('B','SD',inplace=True)
df0