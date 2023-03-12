#.................Multiple Inheritance....................

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


class player:
    no_of_game=8
    def __init__(self,name,game):
        self.name=name
        self.game=game

        def printdetails(self):
            return f"The name is {self.name}, and the game is {self.game}.."

class cool_programmer(Employee,player):
    language="PHP"
    def printlanguage(self):
        print(self.language)

ram=Employee("Ram",50000,"HR")
syam=Employee("Syam",45000,"Sumanta")


karan=cool_programmer("Karan",590000,"Cool_P")


det=karan.printdetails()
karan.printlanguage()
print(det)