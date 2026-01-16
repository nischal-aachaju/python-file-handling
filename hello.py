f=open("write.txt","r")

data=f.readlines()

# print(data,end=" ")
for i in range(len(data)):
    if i ==1:
        print(data[i])