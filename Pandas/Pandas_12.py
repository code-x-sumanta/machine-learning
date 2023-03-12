# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:22:38 2022

@author: Asus
"""

"""
Parameters of interpolate
interpolate method
method = linear
method=time
method=index
method=nearest
method=polinomial
method=spline

"""
   
import pandas as pd


df0=pd.read_csv('E:\ML SD\CSV files\Student_Details2.csv')
print(df0)

df0.interpolate()


df0.interpolate(method='linear')

df0.interpolate(method='time')
df0.interpolate(method='index')















