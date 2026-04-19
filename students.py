#read the students.csv file and print out the name, house, and grade of each student
'''with open("students.csv", "r") as file:
    for line in file:
        name,house,grade= line.strip().split(",")
        print(f"{name} is in {house} and has a grade of {grade}")

'''

#lets use a list to store the students and then print them out sorted by name
students = []

with open("students.csv", "r") as file:
    for line in file:
        name,house,grade= line.strip().split(",")
        student ={"name": name, "house": house, "grade": grade}
        students.append(student)
       

    

for student in sorted(students, key=lambda student: student["name"]):
    print(f'{student["name"]} is in {student["house"]} and has a grade of {student["grade"]}')

