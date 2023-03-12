from pydoc import classname


class A:
    def soom(self):
        print("This is a method from class A")

class B(A):
    def soom(self):
        print("This is a method from class B")


class C(A):
    def soom(self):
        print("This is a method from class C")


class D(B,C):
    def soom(self):
        print("This is a method from class D")

a=A()
b=B()
c=C()
d=D()

d.soom()