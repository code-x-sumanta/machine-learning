# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:23:24 2022

@author: Asus
"""

"""

In this tutorial we explain How to Write CSV File Using Pandas in Hindi and describe these:
1) Pandas read_csv Function
2) How to read csv File Using Pandas
3)  Parameters of read_csv Function
4) Pandas read csv ‘nrows’
5) Pandas read csv ‘usecols’
6) Pandas read csv ‘skiprows’
7) Pandas read csv ‘index_col’
    
"""
import pandas as pd

df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv')
print(df)
type(df)



df.columns
df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',nrows=1)
print(df)


df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',nrows=3)
print(df)

df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',usecols=[0])
print(df)

df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',usecols=[0,1])
print(df)


df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',skiprows=1)
print(df)


df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',skiprows=[1,2])
print(df)

df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',index_col='User Name')
print(df)

df=pd.read_csv('E:\ML SD\CSV files\sample_csv.csv',index_col='First Name')
print(df)

