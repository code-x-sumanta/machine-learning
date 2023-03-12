# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 14:06:55 2022

@author: Asus
"""
"""
Sub plot
"""
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(2,2,1)
plt.subplot(2,2,2)
plt.subplot(2,2,3)
plt.subplot(2,2,4)


plt.subplot(2,2,1)
plt.pie([1])

plt.subplot(2,2,2)
plt.pie([1,2])

plt.subplot(2,2,3)
plt.pie([1,2,3])

plt.subplot(2,2,4)
plt.pie([1,2,3,4])
plt.show()


plt.figure(figsize=(16,18))


plt.subplot(3,2,1)

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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

plt.subplot(3,2,2)

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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

plt.subplot(3,2,3)

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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


plt.subplot(3,2,4)

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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


plt.subplot(3,2,5)

classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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


plt.subplot(3,2,6)
classes=["Python","ML","AI","R","DS"]
class1_students=[30,10,20,25,10]
class2_students=[40,5,20,20,10]
class3_students=[35,5,30,15,15]
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


