
from logging import raiseExceptions


#    a=input("What is your name ??  ")
#    b=input("What is your age ??  ")
#    if int(b)==0:
#        raise ZeroDivisionError("Actuslly b is 0 thats whay stpping the program")
#    if a.isnumeric():
#        raiseExceptions ("Numbers are not allowed")
#
#    #print("Hellow ",a)
#    print(f"Hellow {a}")

a=input("What is your name ??  ")
try:
    print(a)

except Exception as e:
    if a=="Soom":
        raise ValueError("Soom is blocked....He is not allowd....")
    
    print("Exception Handled")