# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 13:25:06 2022

@author: Asus
"""

"""

1. np.char.add()
2. np.char.multiply()
3. np.char.capitalize()
4. np.char.center()
5. np.char.join()
6. np.char.lower()
7. np.char.upper()
8. np.char.replace()
9. np.char.split()
10. np.char.splitlines()
11. np.char.title()
12. np.char.equal()
13. np.char.not_equal()
14. np.char.count()
15. np.char.find()

"""
import numpy as np

s1="I am Sumanta Dey"
s2="I am a ECE student"

np.char.add(s1,s2)
np.char.lower(s1)
np.char.upper(s1)


np.char.center(s1, 45)
np.char.center(s1, 45, fillchar="*")

np.char.split(s1)
np.char.splitlines("Hello\nSumanta")


s3="dmy"
s4="dmy"
np.char.join([":","/"],[s3,s4])

np.char.replace(s1, "Sumanta", "Soom")

np.char.equal(s1,s2)

np.char.equal(s3,s4)

np.char.not_equal(s1, s2)

np.char.count(s1,"a")
np.char.count(s1,"e")

np.char.find(s1, "Dey")





