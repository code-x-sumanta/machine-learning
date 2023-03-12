#  Factorial
#  n!=n*n-1*n-2*...........1
#  n!=n*(n-1)!

#  Iterative method

#    def factorial(n):
#       fac=1
#       for i in range(n):
#           fac=fac*(i+1)
#           return fac


#   num=int(input("Enter the number..."))
#   print(factorial(num))



#  Recursive method


def factorial(n):

    if n==1:
        return 1
    else:
        return n*factorial(n-1)



#   num=int(input("Enter the number..."))
#   print(factorial(num))


#   Fibanacci series
#   0 1 1  2 3 5 8 13 21 .....

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

num=int(input("Enter the number..."))
print(fibonacci(num))