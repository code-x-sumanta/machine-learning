def function(normal, *arg,**kwarg):
    print(normal)
    for item in arg:
        print(item)
    print("Now I would like to introduce some of our heros\n")
    for key, value in kwarg,item():
        print(f"{key} is a {value}")

har=["Ram","Syam","Jodu"]
normal="I am normal argumant and the students are :"
kw={"Ram":"Monitor","Syam":"Student","Jodu":"Teacher"}
function(normal,*har,**kw)