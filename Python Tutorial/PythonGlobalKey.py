#    a=4

#    def func1(n):
#        a=5    #local variable
#        b=8    #local Variable
#        print(a,b)    #local scope variable
#        print(n,"I have printed.... ")
#    func1("This is me")

#    print("This is global var ",a)

#    #We can not change global va. If we want to change in def func we have to use global keyword like global l
a=1
def func1():
    a=3
    def func2():
        global a
        a=5
    print ("Before calling func2()",a)
    func2()
    print ("After calling func2()",a)

func1()
print("In global var a will be save as ",a)
    