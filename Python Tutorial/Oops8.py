#.................Multilevel Inheritance....................

class Dad:
    basketball=1

class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes i  an dance {self.damce} no of times "

class Grandson(Son):
    dance=6

    def isdance(self):
        return f"Jackson yeah !!"\
            f"Yes i can dance very awesomely {self.dance} no of times"


ram=Dad()
syam=Son()
harry=Grandson()

print(harry.isdance())