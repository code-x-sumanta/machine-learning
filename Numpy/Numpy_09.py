# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:27:56 2022

@author: Asus
"""

"""
In this tutorial we explain How to Handle Missing Value in Python in Hindi and describe these:
1) Pandas dropna()
2) Parameters of dropna() method
3) dropna axis
4) dropna how
5) dropna thresh
6) dropna subset
7) dropna inplace
    """
    
import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details.csv')
print(df0)

df0.dropna()


df0.dropna(axis=1)

df0.dropna(how='any')

df0.dropna(how='all')

df0.dropna(thresh=1)



