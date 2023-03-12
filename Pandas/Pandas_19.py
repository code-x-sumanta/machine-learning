# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:56:59 2022

@author: Asus
"""
"""
Parameters of Pandas Join method
1)Pandas join others
2)Pandas join on
3)Pandas join how
4)Pandas join lsuffix
5)Pandas join rsuffix
"""

import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1
df2=pd.DataFrame({'Roll':[5,6,7,8],'S1d':['E','F','G','H'],'Sd2':[9,10,11,12]})
df2

display(df1,df2)
df1.join(df2)

df1.join(df2)

df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]},index=['a','b','c','d'])
df1
df2=pd.DataFrame({'Roll':[5,6,7,8],'S1d':['E','F','G','H'],'Sd2':[9,10,11,12]},index=['a','b','c','d'])
df2

df1.join(df2)

df2=pd.DataFrame({'Roll':[5,6],'S1d':['E','F'],'Sd2':[9,10]},index=['a','b'])
df2
df1.join(df2)
df1.join(df2, how='inner')
df1.join(df2, how='outer')



df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]},index=['a','b','c','d'])
df1
df2=pd.DataFrame({'ID':[5,6,7,8],'S1d':['E','F','G','H'],'Sd2':[9,10,11,12]},index=['a','b','c','d'])
df2
df1.join(df2,lsuffix='_1')
df1.join(df2,rsuffix='_1')

























