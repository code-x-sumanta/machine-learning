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



ram=Employee("Ram",50000,"HR")
syam=Employee("Syam",45000,"Sumanta")
print(ram.printdetails())
syam.change_leaves(6)

print(syam.total_leaves)