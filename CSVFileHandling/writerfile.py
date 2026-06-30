
# import csv 
# with open("student.csv", "w", newline="") as file1:
#     writer = csv.writer(file1) # delimiter = ","
#     writer.writerow(["Firstname", "Lastname"])
#     writer.writerow(["a1", "a2"])
#     writer.writerow(["a3", "a4"])
#     writer.writerow(["a5", "a6"])
#     writer.writerow(["a7", "a8"])

# import csv
# with open("student.csv", "w", newline="") as file1:
#     writer = csv.writer(file1, delimiter=",") 
#     n = int(input("Enter number of students: "))
#     for i in range(n):
#         name = input("Enter name: ")
#         sub1 = float(input("Enter marks of subject 1: "))
#         sub2 = float(input("Enter marks of subject 2: "))
#         percentage = (sub1 + sub2) / 2
#         writer.writerow([name, sub1, sub2, percentage])
#####################################################################
### read mode (open)
import csv  
with open("student.csv", "r", newline="") as file1:
    reader = csv.reader(file1)
    for i in reader:
        print(i)
##############
### calculate grade according to percentage
import csv  
with open("student.csv", "r", newline="") as file1:
    reader = csv.reader(file1)
    for i in reader:
        percentage = float(i[3]) # string -> float  
        if percentage >= 90:
                grade = "A"
        elif percentage >= 80:
                grade = "B"
        elif percentage >= 70:
                grade = "C"
        elif percentage >= 60:
                grade = "D"
        else:
                grade = "F"
        print(f"Name: {i[0]}, English: {i[1]}, Maths: {i[2]} , Percentage: {percentage}, Grade: {grade}")
# ###################################################################
#  A csv file "P_record.csv" contains the record of patients in a hospital.
# Each record of the file contains the following data:
# • Name of a patient
# • Disease
# • Number of days patient is admitted
# • Amount
# For example, a sample record of the file may be:
# ["Gunjan", "Jaundice", 4,15000]
# Write the following Python functions to perform the specified operations on this file:
# (i) Write a function read_data() which reads all the data from the file and displays the details of
# all the 'Cancer' patients. 
# (ii) Write a function count_rec() which countsand returns the number of records in the file
# import csv
# def read_data():
#     with open("P_record.csv", "r", newline="") as file1:
#         reader = csv.reader(file1)
#         for i in reader:
#             if i[1] == "Cancer":
#                 print(i)   
# # ////#  example read_data_amount(amt) function to read and display records with amount greater than a specified value 
# def read_data_amount(amt): # amt -> float
#     with open("P_record.csv", "r", newline="") as file1:
#         reader = csv.reader(file1)
#         for i in reader:
#             if float(i[3]) > amt:
#                 print(i)

# def count_rec():
#     count = 0
#     with open("P_record.csv", "r", newline="") as file1:
#         reader = csv.reader(file1)
#         for i in reader:
#             count += 1
#     return count
# ///////////////////////////////////////////////////////
# Question 2024
# Q32
# def add_device():
#     with open("peripheral.csv", "a", newline="") as file1:
#         writer = csv.writer(file1)
#         p_id = int(input("Enter device id: "))
#         p_name = input("Enter device name: ")
#         p_price = float(input("Enter device price: "))
#         writer.writerow([p_id, p_name, p_price])

# def Count_device():
#     count = 0
#     with open("peripheral.csv",'r', newline="") as file1:
#         reader = csv.reader(file1)
#         for i in reader:
#             if float(i[2]) < 1000:
#                 print(i)
#                 count+=1
#     return count 
##############################################################################






# /////////////////////////////////////////////////////////////////////
# import csv 
# header = ["Firstname","Lastname"]
# with open("names.csv" ,"w", newline="") as csvfile:
#     writer  = csv.DictWriter(csvfile , fieldnames=header)
#     writer.writeheader()
#     writer.writerow({"Firstname": "a10", "Lastname": "a20"})
#     writer.writerow({"Firstname": "a11", "Lastname": "a21"})
#     writer.writerow({"Firstname": "a12", "Lastname": "a22"})
#     writer.writerow({"Firstname": "a13", "Lastname": "a23"})

# with open("names.csv", "r", newline="") as csvfile:
#     reader = csv.DictReader(csvfile)
#     for i in reader:
#         print(i)
    
