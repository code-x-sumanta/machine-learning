#...........Operator overloding and Dunder method............

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

    def __add__(self, other):    #............Search mapping operatorS in Google and use here
        return self.salary + other.salary

syam=Employee("Syam",45000,"Sumanta")

ram=Employee("Ram",50000,"HR")

print(syam + ram)