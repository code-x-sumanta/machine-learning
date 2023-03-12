#.................Single Inheritance....................

class Employee:
    total_leaves=9
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

class programmer(Employee):
    def __init__(self,aname,asalary,arole,language):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=language


    def printprog(self):
        return f"Programmer is {self.name}. And salary is {self.salary}. Role is {self.role}.The languaguaes are {self.language}" 

ram=Employee("Ram",50000,"HR")
syam=Employee("Syam",45000,"Sumanta")

subham=programmer("Subham",78000,"Programmer",["Python","C","C++"])
print(subham.printdetails())
print(subham.printprog())

