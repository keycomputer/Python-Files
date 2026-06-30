
import pickle
# // load, dump
# // new file , list of students, save to file. 
# students = []
# n = int(input("Enter number of students "))
# for i in range(n):
#     name = input("Enter student name: ")
#     marks = float(input("Enter student marks: "))
#     student = [name, marks]
#     students.append(student)

# with open("students.dat", "wb") as f:
#     pickle.dump(students, f)
###################################################
## read from file
# with open("students.dat", "rb") as f:
#     students_from_file = pickle.load(f)
# for i in students_from_file:
#     print(f"Name: {i[0]}, Marks: {i[1]}")
################################################################
    
# using dictionary of students 
# students_dict = {}
# n = int(input("Enter number of students "))
# for i in range(n):
#     rollno = int(input("Enter student roll number: "))
#     name = input("Enter student name: ")
#     marks = float(input("Enter student marks: "))
#     students_dict[rollno] = [name, marks]

# with open("students.dat", "wb") as f:
#     pickle.dump(students_dict, f)
# # //read
# with open("students.dat", "rb") as f:
#     students_from_file = pickle.load(f)
# for rollno, details in students_from_file.items():
#     print(f"Roll No: {rollno}, Name: {details[0]}, Marks: {details[1]}")
######################################################################  

# class Student:
#     def __init__(self, rollno, name, marks):
#         self.rollno = rollno
#         self.name = name
#         self.marks = marks
#     def calcGrade(self):
#         if self.marks >= 90:
#             self.grade = 'A'
#         elif self.marks >= 80:
#             self.grade = 'B'
#         elif self.marks >= 70:
#             self.grade = 'C'
#         elif self.marks >= 60:
#             self.grade = 'D'
#         else:
#             self.grade = 'F'
#     def __str__(self):
#         return f"Roll No: {self.rollno}, Name: {self.name}, Marks: {self.marks}"
# with open("students.dat", "wb") as f:
#     students = [] ## student object list 
#     n = int(input("Enter number of students "))
#     for i in range(n):
#         rollno = int(input("Enter student roll number: "))
#         name = input("Enter student name: ")
#         marks = float(input("Enter student marks: "))
#         student = Student(rollno, name, marks) # init -student class 
#         students.append(student)
#     pickle.dump(students, f)
    
    
# with open("students.dat", "rb") as f:
#     students_from_file = pickle.load(f)
# for student in students_from_file:
#     print(student) ## __str__ 
#     student.calcGrade()
    
    
