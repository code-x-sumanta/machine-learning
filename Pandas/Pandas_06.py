# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:41:51 2022

@author: Asus
"""

"""

In this tutorial we explain How to Write CSV File Using Pandas in Hindi and 
describe these:
1) Pandas head()
2) Pandas tail()
3) Pandas write csv ‘dtype’
4) Pandas write csv ‘true_values‘
5) Pandas write csv ‘false_values’

"""

import pandas as pd


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df1)

df1.head()

df1.head(4)


df1.head(10)

df1.tail()

df1.tail(3)
df1.tail(8)

df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv', dtype={'ID':'float64'})
df1

df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv', dtype={'ID':'float64','Approx Weight':'float64'})
df1


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv',true_values=['Third Year'])
print(df1)





