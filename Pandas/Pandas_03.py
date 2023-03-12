# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 22:24:05 2022

@author: Asus
"""

"""
In this tutorial we explain How to Read CSV File Using Pandas in Hindi 
and describe these:
1) What is CSV File ?
2) Advantages of CSV File
3) pd.read_csv Function
4) How to import the dataset into Python IDE
5) How to read DataFrame 
6) How to read Series
7) What is OS Module in Python
8) os.getcwd()
    
A CSV is a comma separated values file which allows to store data in 
tabular format. 
That data includes numbers and text in plain text form. CSV is an 
extension of any file or spreadsheet .

Advantages of CSV File
1. Universally used
2. Easy to read
3. Easy to understand
4. Quick to create

"""

import pandas as pd


help(pd.read_csv)

pd.read_csv('E:\\ML SD\\CSV files\\sample_csv.csv')
import os
print(os.getcwd())
