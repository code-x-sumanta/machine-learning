f1=open("PythonWrt.txt")

try:
    f=open("ddd.txt")
except Exception as e:
    print(e)
else:
    print("This will run only if except is not running..........")

finally:
    print("Run this anyway...")
    f1.close()