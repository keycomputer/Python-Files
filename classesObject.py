# POP , OOP 

# OOP 
# 1. Encapsulate - Data Binding 
# 2. data abstraction (private, protected , public )
# 3. Inheritance (Resuable ) (parent/child , Super/sub , base/derived )
#                      Vehical 
#            Car   Bike   plane   Train
#    sedane, SUV, HB, ELEC           
# 4. Polymorphism -> static/compile  ,  runtime/dynamic 
# 5. Message passing 


# Class -> blueprint / template
# Object -> instance of a class 
# self -> current object reference 

###################################################3
# Define an Empty Vehicle Class
# class Vehicle:
#     pass

# print(Vehicle)
###################################################3
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# vehicle1 = Vehicle("Tesla Model S", 250, 18)
# print(f"Vehicle Name: {vehicle1.name}, Speed: {vehicle1.max_speed}, Mileage: {vehicle1.mileage}")
###################################################3

# Rectangle Class with Area & Perimeter
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

#     def perimeter(self):
#         return 2 * (self.length + self.width)

# rect = Rectangle(10, 4)
# print("Area =", rect.area())
# print("Perimeter =", rect.perimeter())


###################################################3
# class Phone:
#     def describe(self):
#         self.brand= "Samsung" 
#         self.model = "S25"
#         self.osVersion = 14 
#         print(self.brand, self.model, self.osVersion)
        
# S1 = Phone() # object 
# S1.describe()
# S1.osVersion = 15
# S1.describe()
# S2 = Phone() 
#####################################################

# class Student :
#     # constructor / initialize  (declaraion of an object )
#     def __init__(self):
#         print("Enter Details ")
#         self.name = input("Enter student name ")
#         self.cls = input("Enter class ")
#         self.section = input("Enter section ")
#         self.per = 0.0 
#     def display(self):
#         print(self.name , self.cls , self.section , self.per)
#     # getter - accessor 
#     def getPer(self):
#         return self.per 
#     def getName(self):
#         return self.name
#     def getClass(self):
#         return self.cls
#     # setter - Mutator 
#     def setPer(self, p):
#         self.per = p 
#     def setName(self, n):
#         self.name = n 
#     def setClass(self,c):
#         self.cls = c 
#     def setSection(self,s):
#         self.section = s 
# obj1 = Student() # object 
# obj1.display() 
# # obj1.per = 100
# obj1.setPer(100)
# obj1.display() 

###################################################

# class Book :
#     def input(self):
#         self.bookName = input("enter book name ")
#         self.__bookprice__ = float(input("enter price "))
#         self._bookStock_ = int(input("enter book stock "))

# b1 =Book() 
# b1.input()
# print(b1.bookName, b1.__bookprice__, b1._bookStock_)
######################################################
# Student Class with Average Grade

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def average(self):
#         return sum(self.marks) / len(self.marks)

# s1 = Student("Alice", [85, 90, 78, 92, 88])
# print(f"{s1.name}'s Average Grade: {s1.average()}")

######################################################
# Product Class with Stock Value Calculator

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_value(self):
#         return self.price * self.quantity

# p1 = Product("Laptop", 899.99, 5)
# print(f"Total stock value of {p1.name}: ${p1.total_value():.2f}")

######################################################
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Balance after deposit: {self.balance}")
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Balance after withdrawal: {self.balance}")
#         else:
#             print(f"Insufficient funds. Current balance: {self.balance}")
# account = BankAccount(1000)
# account.deposit(500)
# account.withdraw(200)
# account.withdraw(2000)
######################################################

class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")

light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()
######################################################


######################################################
###### class variable and method  attribute
    #  static variable @staticmethod
    
####### init -> parameters 
