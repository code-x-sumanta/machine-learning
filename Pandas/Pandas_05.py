# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:51:05 2022

@author: Asus
"""

"""

In this tutorial we explain How to Write CSV File Using Pandas in Hindi and describe these:
1) Pandas read_csv Function
2) How to read csv File Using Pandas
3) Parameters of read_csv Function
4) Pandas read csv ‘header’
5) Pandas read csv ‘prefix’
6) Pandas read csv ‘names’
    
"""

import pandas as pd


df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df)
type(df)

df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',header=1)
print(df)
type(df)


df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',header=None)
print(df)
type(df)


df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',header=None,prefix='SOOM ')
print(df)
type(df)


df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',names=['A','B','C','D','E','F'])
print(df)
type(df)

df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',header=1)
print(df)
type(df)


df=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df)
type(df)




















