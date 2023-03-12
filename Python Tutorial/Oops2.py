class Employee:
    total_leaves=9


ram=Employee()
syam=Employee()

ram.name="Ram"
ram.salary=4500
ram.role="Instructor"

syam.name="Syam"
syam.salary=7000
syam.role="Student"

print(Employee.total_leaves)
print(Employee.__dict__)
Employee.total_leaves=11
print(Employee.total_leaves)
print(Employee.__dict__)
