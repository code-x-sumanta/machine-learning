# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:19:18 2022

@author: Asus
"""

"""

In this python NumPy tutorial , We explain NumPy  trigonometric sin(),
cos(), and tan() functions in Hindi along with that also 
explain how to visualise curve of sin(), cos()
and tan() functions using matplotlib library.


"""

import numpy as np
import matplotlib.pyplot as plt

np.sin(30)
np.cos(0)
np.tan(45)
np.sin(75)


x_sin=np.arange(0, 3*np.pi, 0.1)
print(x_sin)

y_sin=np.sin((x_sin))
print(y_sin)

plt.plot(x_sin, y_sin)
plt.show()

x_cos=np.cos(x_sin)
plt.plot(x_sin, x_cos)
plt.show()

y_tan=np.tan(x_sin)
plt.plot(x_sin, y_tan)
plt.show()




