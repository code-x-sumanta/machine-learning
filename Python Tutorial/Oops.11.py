#............Super()and Overriding.............


class A:
    classvar1="I am class var in class A"
    def __init__(self):
        self.var1="Now i am inside class A's constructor"
        self.classvar1="Instance var in class A"
        self.special="Special"

class B(A):
    classvar1="Now i  am in class B"
    def __init__(self):
        super().__init__()
        self.var1="Now i am inside class B's constructor"
        self.classvar1="Instance var in class B"

a=A()
b=B()

print(b.special)