# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:37:16 2022

@author: Asus
"""

"""
1. np.random.random()
2. np.random.randint()
3. np.random.seed()
4. np.random.rand()
5. np.random.randn()
6. np.random.choice()
7. np.random.permutation()

"""

import numpy as np
import random

np.random.random(1)

np.random.random((3,3))

np.random.randint(1,4)

np.random.randint(1,4,(4,4))

np.random.randint(1,4,(2,4,5))

np.random.seed(10)
np.random.randint(1,4,(2,4,5))

np.random.seed(10)
np.random.randint(1,4,(2,4,5))

np.random.rand(4)

np.random.rand(4,4)

np.random.randn(4,4)


x=[1,2,3,4,5,6]
np.random.choice(x)

for i in range(20):
    print(np.random.choice(x))

np.random.permutation(x)
np.random.permutation(x)




