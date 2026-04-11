Fname = input("Enter your name: ")
Lname = input("Enter your last name: ")

name = (Fname + " " + Lname).strip("#$%&*()_+|~=`{}[]:\";'<>?,./\\").title()
print(f"your name is {name} and welocome!!")
