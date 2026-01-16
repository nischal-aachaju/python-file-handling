f=open("write.txt","w")

f.write("hello, Nischal")


print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.close())
f.close()
print(f.close())