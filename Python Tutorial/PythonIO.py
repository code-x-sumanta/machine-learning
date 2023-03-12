#File IO Besics

#    "r" - File for read    DEFAULT
#    "w" - File for write
#    "x" - Create file if not exists
#    "a" - Add more content to the file_dispatcher
#    "t" - Text mode   DEFAULT
#    "b" - Binary mode
#    "+" - Read and write

f=open("PythonIO.txt","rt")
#content=f.read()
#print(content)
#   for line in content:
#     print(line)

#    print(f.readline())
#    print(f.readline())
#    print(f.readline())

print(f.readlines())


f.close()