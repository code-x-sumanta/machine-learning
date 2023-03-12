#.................Public Private Protected.......................

class Employee:
    total_leaves=9
    _protected=8 #.................You have to write protected var in this way..............
    __private=7  #.................You have to write private var in this way.............
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole

    def printdetails(self):
        return f"Name is {self.name}. And salary is {self.salary}. Role is {self.role}."
    #classmethod
    def change_leaves(cls,new_leaves):
        cls.total_leaves=new_leaves

    #classmethod
    def from_dash(cls,string):    #alternative constructor
        return cls(*string.split("-"))

    #Staticmethod
    def printstatic(string):
        print("This is good "+string)

sd=Employee("Sumnata",45000,"Student")
print(sd.printdetails())
print(sd._protected)
print(sd._Employee__private)