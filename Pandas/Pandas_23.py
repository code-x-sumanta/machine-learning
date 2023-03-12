# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:46:04 2022

@author: Asus
"""
"""
Pandas DatetimeIndex
read_csv parse_dates
"""
import pandas as pd

df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df)

df.dtypes
type(df.Date[0])

df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv',parse_dates=['Date'])
print(df)

df.dtypes
type(df.Date[0])