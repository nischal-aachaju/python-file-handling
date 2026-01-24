# f=open("demo.txt","r")

# text =f.read()
# text2=f.readline(7)
# text3=f.readlines()
# print(text)
# print(text2)
# print(text3)
# f.close()


# with open("demo.txt","w") as f:
#     f.writelines("Hello, resale all \n2nd line \t nischal")

# with open("demo.txt","r+") as f:
#     f.truncate(20)
#     text= f.read()
      # print(text)
#     f.write("Hello me new data")
#     f.seek(0)
#     text=f.read()
    # print(text)

# print(text)

f=open("demo.txt","r")
text=f.read()
# print(text)
print(f.writable())
f.close()
print(f.closed)