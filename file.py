#name = input("what is your name ")
'''
file =open("name.txt", "a")
file.write(name + "\n")
file.close()


for name in sorted(open("name.txt")):
    print(name)

'''



# lets use with statement to open the file
with open("name.txt", "r") as file:
    for line in file:
        print(line.strip())

print("==============")

names =[]

with open('name.txt', "r") as file2:
    for line in file2:
        names.append(line.strip())


for name in sorted(names,reverse=True):
    print(name)