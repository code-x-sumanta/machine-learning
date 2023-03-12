# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:02:26 2022

@author: Asus
"""
"""
Parameters of Pandas appand function
1) pandas appand other
2) pandas append ignore index
3) pandas appand sort

"""
import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3,4],'Name':['A','B','C','D'],'Class':[5,6,7,8]})
df1

df2=pd.DataFrame({'ID':[5,6,7,8],'Name':['E','F','G','H'],'Class':[9,10,11,12]})
df2

#df2=pd.DataFrame({'Roll':[5,6,7,8],'S1d':['E','F','G','H'],'Sd2':[9,10,11,12]})
#df2


df1.append(df2)
df1.append(df2, ignore_index=True)
df2.append(df1, ignore_index=True)


df2=pd.DataFrame({'Roll':[5,6,7,8],'S1d':['E','F','G','H'],'Sd2':[9,10,11,12]})
df2

df1.append(df2, ignore_index=True)
df1.append(df2, ignore_index=True, sort=False)









