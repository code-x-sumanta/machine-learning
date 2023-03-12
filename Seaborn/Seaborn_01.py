# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:33:48 2022

@author: Asus
"""
"""
Seaborn is a python library for data visualization builds on the matplotlib library. It is used for statistical graphics.
In this python Seaborn tutorial part-2, We explained with a real-time example. How to draw line graph using the seaborn line plot sns.lineplot() function?
1. What is the seaborn line plot?
2. Seaborn line plot vs matplotlib line plot
3. How to load the dataset from GitHub seaborn dataset repository?
4. How to use sns.load_dataset() function?
5. How to create DataFrame from the list? 
6. How to find a relation between two different DataFrame columns values?
7. After plotting line how to analyze the graph and make a decision?
"""

import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temperature = [36.6, 37, 37.7,39,40.1,43,43.4,45,45.6,40.1,44,45,46.8,47,47.8]

temp_df = pd.DataFrame({"days":days, "temperature":temperature})
 

sns.lineplot(x = "days", y = "temperature", data=temp_df,)
plt.show() 


























































