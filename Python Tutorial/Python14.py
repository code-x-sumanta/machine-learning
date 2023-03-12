#Try Except Exception

print("Enter a number \n")
a=input()
print("Enter b number \n")
b=input()

try:
    print("The sum is ",
    int(a)+int(b))
except Exception as e:
    print(e)


print("This is very impotant...")