# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 17:47:53 2022

@author: Asus
"""
"""

In this tutorial we explain How to Handle Missing Values in Python in Hindi and describe these:
1) Pandas read_csv na_values
2) Pandas read_csv keep_default_na
3) Pandas read_csv na_filter
    
"""

import pandas as pd


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df1)

df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',na_values='not available')
print(df1)

df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',na_values=['not available','no values'])
print(df1)


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',na_values={'Course':'no values'})
print(df1)


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv', na_filter=False)
print(df1)
















