#    f=open("PythonWrt.txt","w")
#    a=f.write("I am the king \n")
#    print(a)
#    f.close()

#    f=open("PythonWrt.txt","a")
#    a=f.write("I am the king \n")
#    print(a)
#    f.close()


f=open("PythonWrt.txt","r+")
print(f.read())
f.write("I am the king of my world")
f.close()
