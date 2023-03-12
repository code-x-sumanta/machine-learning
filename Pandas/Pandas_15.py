# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:00:35 2022

@author: Asus
"""

"""
1)Parameters of groupby func
2)groupby.().get_group()
3)Splitting the opject into group
4)Appling the function

"""
import pandas as pd


df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df)

gr1=df.groupby(by='Class')
gr1

gr1.groups

df.groupby(['Class','Study Hr']).groups
for Class, df_1 in gr1:
    print(Class)
    print(df_1)

list(gr1)

dict(list(gr1))

gr2=df.groupby('Class').get_group(10)
gr2

gr3=df.groupby('Study Hr').get_group(6.6)
gr3

gr1.sum()
gr1.describe()

gr1.agg(['sum','max','min'])









