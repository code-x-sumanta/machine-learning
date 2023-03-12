# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:11:42 2022

@author: Asus
"""
"""
Line Plot
"""
import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[30.6,34,31,34.5,32.1,38,33.3,30.9,39,34.9,31.9,34,37,35.9,31]



plt.plot(days,temp)
plt.axis([0,30,0,50])
plt.title('Garhbeta Temperature')
plt.xlabel('days')
plt.ylabel('temperature')
plt.show()
