


from os import rename


with open ("data.txt") as file:
    rename("data.txt","datas.txt") # to rename files
    file.seek(2)
    print(file.tell()) # my cursor is in 2
    result=file.read()
    print(result)
    print(file.tell()) # after reading , my cursor is in 33(or it shows the last cursor point)

