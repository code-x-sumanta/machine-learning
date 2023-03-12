numbers=["1","4","5","8"]
numbers=list(map(int, numbers))
numbers[2]=numbers[2]+1
print(numbers[2])

def sq(a):
    return a*a

num=[5,6,7,8,9]
square=list(map(sq,num))
print(square)

#    num=[5,6,7,8,9]
#    square=list(map(lambda x:x*x,num))
#    print(square)
'''
list1=[5,6,7,8,9]
def is_greater_7(num):
    return num>7
gr_than_7=list(filter(is_greater_7,list1))
print(gr_than_7)
'''

from functools import reduce

list=[1,2,3,4,5,6,7]
#    num=0
#    for i in list:
#        num=num+i
#   print(num)

num=reduce(lambda x,y:x+y,list)
print(num)