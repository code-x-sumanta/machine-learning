# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 18:17:02 2022

@author: Asus
"""
"""


In this tutorial we explain How to Handle Missing Value in Python 
in Hindi and describe these:
1) Pandas isnull()
2) Pandas isnull().sum()
3) Pandas isnull.sum().sum()
4) Pandas notnull()
5) Pandas dataframe.isnull()
6) Pandas series.isnull()
7) Pandas dataframe.notnull()

"""

import pandas as pd


df1=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df1)


df1.isnull()

df1.isnull().sum()
df1.isnull.sum().sum()


df1.notnull()
df1.notnull().sum()
df1.notnull().sum().sum()

import numpy as np
import pandas as pd

#   Series
sr=pd.Series([1,2,3,np.nan,4,np.nan])
sr
sr.notnull()
sr.notnull().sum()

sr.isnull()














