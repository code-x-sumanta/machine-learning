'''
def func1():
    print("Sumanta Dey")

func2=func1
del func1
func2()
'''

'''
def fun(num):
    if num==0:
        return sum
    if num==1:
        return print
print(fun(1))
'''

def dec1(func1):
    def nowexec():
        print("Executing now")
        func1()
        print("Executed....")
    return nowexec

def who_is_sumanta():
    print("Sumanta is a very good boy")

who_is_sumanta=dec1(who_is_sumanta)
who_is_sumanta()
