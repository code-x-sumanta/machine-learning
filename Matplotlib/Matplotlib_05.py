# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 10:12:05 2022

@author: Asus
"""

"""
Matplotlib Scatter Plot

"""
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

df=pd.read_csv('E:\ML SD\CSV files\Student_Details3.csv')
df.shape
df

x=df["Class"]
y=df["Percentage"]

plt.scatter(x, y)
plt.title("Students Details")
plt.xlabel("Class")
plt.ylabel("Percentage")






















