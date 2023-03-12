# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:00:28 2022

@author: Asus
"""
"""
Histogram

"""
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use("ggplot")
ml_students_age= np.random.randint(18,45,(100))
py_students_age= np.random.randint(15,40,(100))

#print(ml_students_age)
#print(py_students_age)

#plt.figure(figsize=(16,9))

bins=[15,20,25,30,35,40,45]
"""
plt.hist(ml_students_age,bins, rwidth=0.8, histtype='bar',
         orientation="horizontal", color='m')


plt.hist(py_students_age,bins, rwidth=0.8, histtype='bar',
         orientation="vertical", color='y')
"""
plt.hist([ml_students_age,py_students_age],bins, rwidth=0.8, histtype='bar',
         orientation="vertical", color=["m","y"], 
         label=["ML Student age","PY Students age"])


plt.title("ML Students age histograms")
plt.xlabel("Students age category")
plt.ylable("No of Students age")
plt.legend()
style.use("ggplot")
plt.grid(color='g',linestyle='-.',linewidth=2)
plt.show()

