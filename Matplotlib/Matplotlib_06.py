# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 13:28:14 2022

@author: Asus
"""
"""
Pie Chart
"""
import matplotlib.pyplot as plt
import numpy as np

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
plt.pie(class1_students, labels= classes)
plt.show()


classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0.3,0,0.2,0,0]
colors=['c','b','r','y','g']
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%')
plt.show()


classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0.3,0,0.2,0,0]
colors=['c','b','r','y','g']
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%', shadow=True)
plt.show()

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0,0,0.2,0,0]
colors=['c','b','r','y','g']
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%', shadow=True, radius=1.5,
        startangle=90)
plt.show()


classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0,0,0.2,0,0]
colors=['c','b','r','y','g']
textprops= {"fontsize":15}
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%', shadow=True, radius=1.5,
        startangle=90, textprops=textprops)
plt.show()


classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0,0,0.2,0,0]
colors=['c','b','r','y','g']
textprops= {"fontsize":15}
wedgeprops={"linewidth":4, "width":1, "edgecolor":"k"}
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%', pctdistance=0.6,
        wedgeprops=wedgeprops,
        shadow=True, radius=1.5,
        startangle=90, textprops=textprops, center=(2,3), rotatelabels=True)
plt.show()

plt.figure(figsize=(3,2))
classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
explode=[0,0,0.2,0,0]
colors=['c','b','r','y','g']
textprops= {"fontsize":15}
wedgeprops={"linewidth":4, "width":2, "edgecolor":"k"}
plt.pie(class1_students, labels= classes, explode=explode, 
        colors=colors, autopct= '%0.3f%%', pctdistance=0.6,
        wedgeprops=wedgeprops,
        shadow=True, radius=2.5,
        startangle=90, textprops=textprops, center=(2,3), rotatelabels=True)

plt.legend()
plt.show()



import numpy as np
plt.figure(figsize=(7,4))

colors=['r','w','r','w','r','w','r','w','r','w','r','w']
labels= np.ones(20)

plt.pie([1], colors="k", radius= 2.05)
plt.pie(labels, colors= colors, radius=2.0)

plt.pie([1], colors="g", radius= 1.8)
plt.pie([1], colors="y", radius= 1.6)
plt.pie([1], colors="c", radius= 1.3)
plt.pie([1], colors="b", radius= 1.1)
plt.pie([1], colors="m", radius= 0.9)

plt.pie([1], colors="b", radius= 0.31)
plt.pie(labels, colors= colors, radius=0.3)

plt.pie([1], colors="w", radius= 0.2)
plt.pie([1], colors="k", radius= 0.1)
plt.show()













