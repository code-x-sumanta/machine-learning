class Employee:
    total_leaves=9
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name}. And salary is {self.salary}. Role is {self.role}."


ram=Employee("Sumanta",50000,"HR")
'''
syam=Employee()

ram.name="Ram"
ram.salary=4500
ram.role="Instructor"

syam.name="Syam"
syam.salary=7000
syam.role="Student"
print(ram.printdetails())
print(syam.printdetails())

'''
print(ram.salary)