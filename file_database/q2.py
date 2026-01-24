
with open("a.txt","r") as f:
    data=f.readlines()  
    
print(data)

f=open("b.txt","w")
f.writelines(data)
f.close()