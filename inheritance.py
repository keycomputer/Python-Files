# Bus Subclass Inheriting from Vehicle
# class Vehicle:
#     def __init__(self, name, max_speed):
#         self.name = name
#         self.max_speed = max_speed

#     def display(self):
#         print(f"Vehicle: {self.name}, Max Speed: {self.max_speed} km/h")

# class Bus(Vehicle):
#     pass

# bus1 = Bus("School Bus", 120)
# bus1.display()

# Parent Method Using super()

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

##################################################

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
####################################################
# Polymorphism with Dog & Cat
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


