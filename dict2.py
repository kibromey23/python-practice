students = [

    {"name":"kibrom", "age": 20, "grade": "A"},
    {"name":"aruway", "age": 21, "grade": "B"},
    {"name":"elaye", "age": 22, "grade": "C"},
    {"name":"honey", "age": 23, "grade": None}

]


for student in students:
    print(student["name"],student["age"],student["grade"],sep=", ")
   