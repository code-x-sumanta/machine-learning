# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 08:33:39 2022

@author: Asus
"""
"""
Parameters of pandas melt valus
1)pd.melt()
2)pandas melt frame
3)pandas melt id_vars
4)pandas melt value_vars
5)pandas melt var_name
6)pandas melt value_name

"""

import pandas as pd
df=pd.read_csv('E:\ML SD\CSV files\Student_Details2.csv')
print(df)

pd.melt(df)
pd.melt(df,id_vars=['Course'])
pd.melt(df,id_vars=['ID'])
pd.melt(df,value_vars=['Course'])
pd.melt(df,id_vars=['ID'],value_vars=['Course'])
pd.melt(df,id_vars=['ID'],value_vars=['Approx Weight'])

pd.melt(df,id_vars=['ID'],value_vars=['Course'],var_name='Catagory')
pd.melt(df,id_vars=['ID'],value_vars=['Course'],var_name='Catagory',value_name='Data')
