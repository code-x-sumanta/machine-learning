#    ls=[]
#    for i in range(100):
#        if i%3==0:
#            ls.append(i)

#    ls=[i for i in range (100) if i%3==0]
#    print(ls)

#dict1={ i:f"item{i} for i in range (100)"}
#print(dict1)

sd={sd for sd in ["sd1","sd2","sd1","sd2"]}
print(type(sd))
print(sd)

#generators

evens= ( i for i in range(100) if i%2==0 )
for item in evens:
    print(item)