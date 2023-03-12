# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:22:08 2022

@author: Asus
"""

"""
1) What is Pandas DataFrame ?
2) How to Create Pandas DataFrame ?
3) Creating Empty DataFrame
4) Creating Pandas DataFrame from List
5) Creating Pandas DataFrame from List of List/ ndaray
6) Creating Pandas DataFrame from Dict
7) Creating Pandas DataFrame from List of Dicts
8) Creating Pandas DataFrame from Dict of Series

Pandas DataFrame is two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes(rows & columns).
"""

import pandas as pd

emp_df=pd.DataFrame()
print(emp_df)

list1=['a','b','c','d']
print(list1)

df1=pd.DataFrame(list1)
print(df1)

df1
ls_of_ls=[[1,2,3],[4,5,6],[7,8,9]]
print(ls_of_ls)

df2=pd.DataFrame(ls_of_ls)
df2

dict_1={'ID':[11,22,33,44]}
dict_1

df3=pd.DataFrame(dict_1)
df3

dict_2={'ID':[11,22,33,44],'SN':[1,2,3,4]}
dict_1

df4=pd.DataFrame(dict_2)
df4

ls_of_dict=[{'a':1,'b':2},{'a':3,'b':4}]
df5=pd.DataFrame(ls_of_dict)
df5

dict_st={'ID':pd.Series([1,2,3]), 'SN':pd.Series([111,222,333])}
df6=pd.DataFrame(dict_st)
df6







