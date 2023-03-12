# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:25:42 2022

@author: Asus
"""
"""
Line plot(cont.)
"""
import matplotlib.pyplot as plt
from matplotlib import style
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp=[30.6,31,32.6,34.5,32.1,34,33.3,30.9,34,34.9,36.9,34,37,35.9,38]
style.use("ggplot")

#plt.plot(days,temp,color='r',marker='o')
#plt.plot(days,temp,color='r',marker='^')

#plt.plot(days,temp,color='r',marker='o',linestyle=':')
# linestyle supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'


#plt.plot(days,temp,color='g',marker='o',linestyle='--',linewidth=3,
#         markersize=10)

#plt.plot(days,temp,"go--",linewidth=3,
#        markersize=10)

plt.plot(days,temp,"mo--",linewidth=3,
         markersize=10)


#plt.axis([0,30,0,50])
plt.title('Garhbeta Temperature', fontsize=15)
plt.xlabel('days',fontsize=15)
plt.ylabel('temperature',fontsize=15)
plt.legend(["Temp line"], loc=4)    #location =0 to 15

#plt.grid(color='r',linestyle='-',linewidth=2)

plt.grid(color='k',linestyle='-',linewidth=2)
plt.show()


import matplotlib.pyplot as plt
from matplotlib import style
days=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
garh_temp=[30.6,31,32.6,34.5,32.1,34,33.3,30.9,34,34.9,36.9,34,37,35.9,38]
hoom_temp=[36.9,34,37,35.9,38,38,39.3,42.1,42,42.8,39.6,
           43.1,42.9,40.8,44]

style.use("ggplot")

plt.plot(days,garh_temp,"mo--",linewidth=3,
         markersize=10, label = "Garhbeta Temp Line")

plt.plot(days,hoom_temp,"ro:",linewidth=3,
         markersize=10, label = "Hoomgarh Temp Line")

plt.title('Garhbeta and Hoomgarh Temperature', fontsize=15)
plt.xlabel('days',fontsize=15)
plt.ylabel('temperature',fontsize=15)
plt.legend(loc=4)    #location =0 to 15

plt.grid(color='g',linestyle='-.',linewidth=2)
plt.show()

