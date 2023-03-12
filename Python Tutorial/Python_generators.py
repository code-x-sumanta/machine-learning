"""
    Iterable---> __iter__()  or __getitem__()
    Iterator---> __next__()
    Itretion--->
"""

def gen(n):
    for i in range(n):
        yield i

#for i in range(100):
#    print(i)

#g=gen(564613512321)
#print(g)

g=gen(5)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
#for i in g:
#   print(g)

s="sumanta"
ier=iter(s)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())