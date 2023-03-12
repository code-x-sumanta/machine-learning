# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 09:23:48 2022

@author: Asus
"""
"""
Parameters of Pandas contat function
1)pd.contat()
2)Concatenate multiple series
3)Cancatenate multiple data frame
4)Pandas concat objs
5)Pandas concat axis
6)Pandas concat ignore_index

"""
import pandas as pd


df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
print(df)

sr1=pd.Series([0,1,2])
sr1

sr2=pd.Series([3,4,5,6,7])
sr2

pd.concat([sr1,sr2])

df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1


df2=pd.DataFrame({'ID':[5,6,7,8],'Name':['E','F','G','H'],'Class':[9,10,11,12]})
df2

pd.concat([df1,df2])
pd.concat([df2,df1])
pd.concat([df1,df2],axis=1)
pd.concat([df1,df2],axis=0)
pd.concat([df1,df2],axis=0,ignore_index=True)


