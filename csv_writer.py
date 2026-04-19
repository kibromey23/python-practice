import csv


name = input("what is your name? ")
house = input("whers is your house? ")

with open("students.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,house])


 

