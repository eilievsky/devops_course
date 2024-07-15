# f = open("mydata.txt", "a")
# names = []
# for i in range(3):
#     f.write(input("Enter name: ") + "\n")
# f.close()
#
# f = open("mydata.txt", "r")
# for name in f.readlines():
#     print(name,end='')
# f.close()

# file1  =  open("requirements.txt")
# for line in file1.readlines():
#     print(line,end='')

with open("mydata.txt","a") as file:
    for i in range(3):
        file.writelines(input("Insert nane: ") + "\n",)

with open("mydata.txt","r") as file:
    for data in file.readlines():
        print(data,end='')