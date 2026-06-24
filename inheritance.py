# 1. Single Level 
# 2. MultiLevel
# 3. Multiple 
# 4. hierarchical 
# 5. hybrid

# single Level
# Bus Subclass Inheriting from Vehicle
# class Vehicle:
#     def __init__(self, name, max_speed):
#         self.name = name
#         self.max_speed = max_speed

#     def display(self):
#         print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

# class Bus(Vehicle):
#     pass

# bus1 = Bus("School Bus", 60)
# bus1.display()
# bus2 = Bus("Travel", 100)
# bus2.display()

##################################################
# Overriding 
# class Vehicle:
#     def __init__(self, name, max_speed):
#         self.name = name
#         self.max_speed = max_speed

#     def seating_capacity(self, capacity):
#         print(f"{self.name} seating capacity is: {capacity}")

# class Bus(Vehicle):
#     def seating_capacity(self):
#         super().seating_capacity(50)

# bus = Bus("School Bus", 120)
# bus.seating_capacity()
# v1 = Vehicle("Car", 180)
# v1.seating_capacity(5)
##################################################
# Parent Method Using super()
# class A: # super 
#     def __init__(self):
#         print("A constructor ")
# class B(A):
#     def __init__(self):
#         # super().__init__()
#         A.__init__(self)
#         print("B constructor ")
# obj1 = B()
###################################################  
# Maintenance Fee in Child Class via super()

# class Vehicle:
#     def __init__(self, base_fare):
#         self.base_fare = base_fare

# class Taxi(Vehicle):
#     def __init__(self, base_fare):
#         super().__init__(base_fare)
#         self.maintenance_fee = base_fare * 0.10

#     def total_fare(self):
#         return self.base_fare + self.maintenance_fee

# taxi = Taxi(500)
# print("Total fare with maintenance fee:", taxi.total_fare())
###################################################
####################################################

#Overriding hierarchical
# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# dog = Dog()
# cat = Cat()

# print("Dog says:", dog.speak())
# print("Cat says:", cat.speak())

##################################################
########## override avoid ######################
# class Animal:
#     def speak(self):
#         print("Some sound")
# class Dog(Animal):
#     def speak(self):
#         # super().speak()
#         Animal.speak(self)
#         return "Woof!"
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         return "Meow!"
# dog = Dog()
# cat = Cat()

# print("Dog says:", dog.speak())
# print("Cat says:", cat.speak())


####################################################
# Full-Time vs Part-Time Employee Pay

# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def calculate_pay(self):
#         return 0

# class FullTimeEmployee(Employee):
#     def __init__(self, name, annual_salary):
#         super().__init__(name)
#         self.annual_salary = annual_salary

#     def calculate_pay(self):
#         return self.annual_salary / 12

# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_pay(self):
#         return self.hourly_rate * self.hours_worked

# ft = FullTimeEmployee("Alice", 60000)
# pt = PartTimeEmployee("Bob", 500, 20)

# print(f"{ft.name}'s monthly pay: {ft.calculate_pay()}")
# print(f"{pt.name}'s monthly pay: {pt.calculate_pay()}")


####################################################

###### MULTIPLE ############# 

# class A :
#     def funct1(self):
#         print("class A function ")
# class B:
#     def funct2(self):
#         print("class B function ")
# class C(A,B):
#     def funct3(self):
#         print("Class C function ")
# obj = C() 
# obj.funct1()
# obj.funct2()
# obj.funct3()
##########################################################
#### multiple -> init and override ####
# class A :
#     def __init__(self):
#         print("A class constructor ")
#     def funct(self):
#         print("class A function ")
# class B:
#     def __init__(self):
#         print("B class constructor ")
#     def funct(self):
#         print("class B function ")
# class C(A,B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("C class constructor ")
#     def funct(self):
#         A.funct(self)
#         B.funct(self)
#         print("Class C function ")
# obj = C() 
# obj.funct()
