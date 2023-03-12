# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:19:17 2022

@author: Asus
"""

"""
1)Parameters of pandaas marging function
2)Pandas merge on
3)Pandas merge how
4)Pandas merge indicator
5)Pandas merge left_index
6)Pandas merge right_index
7)Pandas merge suffixes

"""
import pandas as pd


df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df)

df1=pd.DataFrame({'ID':[1,2,3,4,5],'Class':[8,9,10,11,12]})
df1

df2=pd.DataFrame({'ID':[1,2,3,4,5],'Name':['A','B','C','D','E']})
df2

df3=pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
df3

pd.merge(df1, df2, on='ID')

pd.merge(df2, df1, on='ID')

pd.merge(df3, df1, on='ID')

pd.merge(df3, df1, on='ID',how='inner')

pd.merge(df1, df3, on='ID',how='left')

pd.merge(df1, df3, on='ID',how='right')

pd.merge(df1, df3, on='ID',how='outer')
pd.merge(df1, df3, on='ID',how='outer', indicator=True)

df1
df2
df2=pd.DataFrame({'ID':[6,7,8,9,10],'Name':['A','B','C','D','E']})
df2

pd.merge(df1, df2)
pd.merge(df1, df2, left_index=True,right_index=True)

df4=pd.DataFrame({'ID':[1,2,3,4,5],'Class':[8,9,10,11,12]})
df5=pd.DataFrame({'ID':[1,2,3,4,5],'Class':[8,9,10,11,12]})
pd.merge(df4, df5, on='ID')         #..........merge suffixes
pd.merge(df4, df5, on='ID',suffixes=('_Higher','_Lower')) # merge suffixes











