# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 09:34:25 2022

@author: Asus
"""
"""
Matplotlib Bar Chart

"""
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]

plt.bar(classes, class1_students)

plt.barh(classes, class1_students)

plt.bar(classes, class1_students,width=0.5)
plt.bar(classes, class1_students,width=0.5,align='edge')
plt.bar(classes, class1_students,width=0.5,align='edge',color='y')

plt.bar(classes, class1_students,width=0.5,align='edge',
        color='y',edgecolor="m")

plt.bar(classes, class1_students,width=0.5,align='edge',
        color='y',edgecolor="m",linewidth=5)


plt.bar(classes, class1_students,width=0.2,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.5)
plt.bar(classes, class1_students,width=0.2,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9)

plt.bar(classes, class1_students,width=0.2,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9, linestyle='--')


plt.bar(classes, class1_students,width=0.2,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9, 
        linestyle='--', label="Class 1 Students")

style.use("ggplot")
plt.figure(figsize=(16,9))
plt.bar(classes, class1_students,width=0.2,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9, 
        linestyle='--', label="Class 1 Students")    # visible=False


plt.figure(figsize=(16,9))
plt.barh(classes, class1_students,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9, 
        linestyle='--', label="Class 1 Students")  

plt.figure(figsize=(16,9))

plt.bar(classes, class1_students,align='edge',
        color='y',edgecolor="m",linewidth=5, alpha=0.9, 
        linestyle='--', label="Class 1 Students")  
plt.title("Bar Chart of IAIP Class", fontsize=18)
plt.xlabel("Classes", fontsize=15)
plt.ylabel("No of Students", fontsize=15)
plt.show()



plt.bar(classes, class1_students,width=0.5,align='edge',
        color='b', label="Class 1 Students")  
plt.bar(classes, class2_students,width=0.5,align='edge',
        color='y', label="Class 2 Students")
plt.title("Bar Chart of IAIP Class", fontsize=18)
plt.xlabel("Classes", fontsize=15)
plt.ylabel("No of Students", fontsize=15)
plt.show()



classes_index=np.arange(len(classes))
width=0.2
plt.bar(classes_index, class1_students,width,align='edge',
        color='b', label="Class 1 Students")  
plt.bar(classes_index + width, class2_students,width,align='edge',
        color='y', label="Class 2 Students")
plt.bar(classes_index + width + width, class3_students,width,align='edge',
        color='g', label="Class 3 Students")
plt.xticks(classes_index + width, classes)
plt.title("Bar Chart of IAIP Class", fontsize=18)
plt.xlabel("Classes", fontsize=15)
plt.ylabel("No of Students", fontsize=15)
plt.show()


classes_index=np.arange(len(classes))
width=0.2
plt.barh(classes_index, class1_students,width,align='edge',
        color='b', label="Class 1 Students")  
plt.barh(classes_index + width, class2_students,width,align='edge',
        color='y', label="Class 2 Students")
plt.barh(classes_index + width + width, class3_students,width,align='edge',
        color='g', label="Class 3 Students")
plt.yticks(classes_index + width, classes)
plt.title("Bar Chart of IAIP Class", fontsize=18)
plt.ylabel("Classes", fontsize=15)
plt.xlabel("No of Students", fontsize=15)
plt.show()