
import pickle

#   pickling a file  object

#    sd=["ram","syam","sourav","souma"]
#    file=("sd_dey.pkl")
#    fileobj=open(file,'wb')
#    pickle.dump(sd, fileobj)
#    fileobj.close()

file="sd_dey.pkl"
fileobj=open(file,'rb')
sd=pickle.load(fileobj)
print(sd)
print(type(sd))