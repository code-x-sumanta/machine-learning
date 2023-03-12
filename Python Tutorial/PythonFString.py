# F String
import math

me="Sumanta"
a1=3
a="This is %s %s"%(me,a1)
print(a)


b="This is {} {}"
c=b.format(me,a1)
print(c)

d="This is {1} {0}"
e=d.format(me,a1)
print(e)

x=f"This is {me} {a1} {math.cos(0)}"
print(x)