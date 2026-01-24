# user_input=eval(input("Enter"))

# print(user_input)

# with open("sample.txt",'w') as f:
#     f.writelines(["ram","\nshyam","\nhari","\ngita"])

nam=[]

with open("sample.txt",'r') as f:
    for i in f:
        result=i.split()
        print(result)
        nam.append(result)
print(nam)
