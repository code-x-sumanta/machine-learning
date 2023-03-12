l=["a","b","c","d","g"]
#    i=1
#    for item in l:
#        if i%2 is not 0:
#            print(f"Please buy {item}")
#            i+=1

for index, item in enumerate(l):
    if index%2==0:
        print(f"Please buy {item}")
        