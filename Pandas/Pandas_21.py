# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:13:15 2022

@author: Asus
"""
"""
Parameters of pandas pivot table
1) pivot_table
2) pivot table eindex
3) pivot table columns
4) pivot table aggfunv
5) pivot table fill value
8) pivot table margins

"""
import pandas as pd
df=pd.read_csv('E:\ML SD\CSV files\Student_Details2.csv')
print(df)

df.pivot_table(index='Course')
df.pivot_table(index='Course',columns='Approx Weight')
df.pivot_table(index='Course',columns='Approx Weight',aggfunc='count')
df.pivot_table(index='Course',columns='Approx Weight',aggfunc='max')
df.pivot_table(index='Course',columns='Approx Weight',aggfunc='sum')
df.pivot_table(index='Course',columns='Approx Weight',fill_value='none')
df.pivot_table(index='Course',columns='Approx Weight',fill_value=0)
df.pivot_table(index='Course',columns='Approx Weight',fill_value=0,margins=True)
df.pivot_table(index='Course',columns='Approx Weight',aggfunc='sum',fill_value=0,margins=True)
