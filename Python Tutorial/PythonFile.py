f=open("PythonWrt.txt")
#print(f.tell())
print(f.readline())
#print(f.tell())
f.seek()
print(f.readline())
#print(f.tell())
print(f.readline())


f.close()