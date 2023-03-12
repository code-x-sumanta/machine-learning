#dictionary is nothing but key value pairs

d1={}
print(type(d1))

d2={"a":1,"b":2,"c":3}
#print(d2)
#print(d2["c"])

d2["d"]=4
print(d2)

del d2["b"]
print(d2)

print(d2.get("c"))

print(d2.keys())

print(d2.items())