class Student:
    class_year = 2026
    num_students = 0


    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_students += 1
    

student1 = Student("Kibrom",26)
student2 = Student("hellen",23)
student3 = Student("hellen",23)

print(Student.num_students)

