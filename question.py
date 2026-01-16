
f=open("data.txt","r")
data=f.read()
f.close()
f=open("dataCopy.txt","w")
f.write(data)
f.close()