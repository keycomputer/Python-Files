# dynamic typed 
# def A(x):
#     print(x)
# A(123) 
# A("abc")
#########################################################
# POLYMORPHISM -> many forms 
# 1. static / compile-time  -> overloading (method, operator )
# 2. dynamic/ run-time -> override (upcasting )
#########################################################

# Method Overloading
# The process of calling the same method with different 
# parameters is known as method overloading. 
# Python does not support method overloading. 

# Overloading Built-in Functions
# Giving a Length to Your Objects Using len()

# class Test:
#     def __init__(self , List1):
#         self.cars = List1 
#     def retLenCars(self):
#         return len(self.cars)
# obj = Test(['a','b','c'])
# print(obj.retLenCars()) 
# print(len(obj)) # error
    
# class Order:
#     def __init__(self, cart, customer):
#          self.cart = list(cart)
#          self.customer = customer

#     def __len__(self):
#          return len(self.cart)

# order = Order(['banana', 'apple', 'mango'], 'Real Python')
# print(len(order))

############################################################

# Work With abs()
# class Vector:
#     def __init__(self, x_comp, y_comp):
#         self.x_comp = x_comp
#         self.y_comp = y_comp

#     def __abs__(self):
#         return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5
# vector = Vector(3, 4)
# print(abs(vector))
# 5.0

#######################################################
# #str()
# def __str__(self):
#     pass 
# class Test:
#     def __init__(self , List1):
#         self.cars = List1 
#     def retLenCars(self):
#         return len(self.cars)
#     def __str__(self):
#         return "#".join(self.cars) #string 
    
# obj = Test(["a","b",'c']) 
# print(obj)

# def __repr__(self):
#     return f'Vector({self.x_comp}, {self.y_comp})'


# def __bool__(self):
#     return len(self.cart) > 0    
# class ComplexNumber:
#     def __init__(self, r, i):
#         self.r = r 
#         self.i= i 
#     def __bool__(self):
#         return (self.r>0 and self.i>0)
# obj = ComplexNumber(1,0)
# print(bool(obj))
#######################################################################

# # Indexing and Slicing Your Objects Using []
# class Order:
#     def __init__(self, cart, customer):
#         self.cart = list(cart)
#         self.customer = customer

#     def __getitem__(self, key):
#         return self.cart[key]

# order = Order(['banana', 'apple'], 'Real Python')
# order[0]
# # 'banana'
# order[-1]
# # 'apple'


###################################

# class Vehicle:

#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price

#     def show(self):
#         print('Details:', self.name, self.color, self.price)

#     def max_speed(self):
#         print('Vehicle max speed is 150')

#     def change_gear(self):
#         print('Vehicle change 6 gear')


# inherit from vehicle class
# class Car(Vehicle):
#     def max_speed(self):
#         print('Car max speed is 240')

#     def change_gear(self):
#         print('Car change 7 gear')


# # Car Object
# car = Car('Car x1', 'Red', 20000)
# car.show()
# # calls methods from Car class
# car.max_speed()
# car.change_gear()

# # Vehicle Object
# vehicle = Vehicle('Truck x1', 'white', 75000)
# vehicle.show()
# # calls method from a Vehicle class
# vehicle.max_speed()

# vehicle.change_gear()

# ##################################################
# # Overrride Built-in Functions

# class Shopping:
#     def __init__(self, basket, buyer):
#         self.basket = list(basket)
#         self.buyer = buyer

#     def __len__(self):
#         print('Redefine length')
#         count = len(self.basket)
#         # count total items in a different way
#         # pair of shoes and shir+pant
#         return count * 2

# shopping = Shopping(['Shoes', 'dress'], 'Jessa')
# print(len(shopping))
# ######################################
# # Polymorphism In Class methods
# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("Max speed 350")

# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("Max speed is 240")

# ferrari = Ferrari()
# bmw = BMW()

# # iterate objects of same type
# for car in (ferrari, bmw): 
#     # call methods without checking class of object
#     car.fuel_type()
#     car.max_speed()
    
# class Ferrari:
#     def fuel_type(self):
#         print("Petrol")

#     def max_speed(self):
#         print("Max speed 350")

# class BMW:
#     def fuel_type(self):
#         print("Diesel")

#     def max_speed(self):
#         print("Max speed is 240")

# # normal function
# def car_details(obj):
#     obj.fuel_type()
#     obj.max_speed()

# ferrari = Ferrari()
# bmw = BMW()

# car_details(ferrari)
# car_details(bmw)
# ############################################
# # Operator Overloading in Python

# # Special Methods for Operator Overloading
# # Python provides specific methods for each operator.
# class Marks:
#     def __init__(self, m=0):
#         self.m = m 
#     def output(self):
#         print("Marks Obtained ", m)
# m1 = Marks(80)
# m2 = Marks(65)
# print(m1+m2)

# # Binary Operators
# # Operator	Magic Method
# # +	__add__(self, other)
# # -	__sub__(self, other)
# # *	__mul__(self, other)
# # /	__truediv__(self, other)
# # //	__floordiv__(self, other)
# # %	__mod__(self, other)
# # **	__pow__(self, other)
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return self.value + other.value
#     def average(self, obj):
#         return (self.value+obj.value) / 2  
#     def __pow__(self, obj):
#         return self.value ** obj.value
# ob1 = A(1)
# ob2 = A(2)
# print(ob1 + ob2)
# print(A.__add__(ob1, ob2))
# print(ob1.__add__(ob2))
# print(ob1.average(ob2))
# print(ob1**ob2)
#####################################################
# # Comparison Operators / Relational Operators
# # Operator	Magic Method
# # <	__lt__(self, other)
# # >	__gt__(self, other)
# # <=	__le__(self, other)
# # >=	__ge__(self, other)
# # ==	__eq__(self, other)
# # !=	__ne__(self, other)
# class A:
#     def __init__(self, a):
#         self.a = a
    
#     def __gt__(self, other):
#         return self.a > other.a

# ob1 = A(2)
# ob2 = A(3)
# if ob1 > ob2:
#     print("ob1 is greater than ob2")
# else:
#     print("ob2 is greater than ob1")
    
# #     Overloading Boolean Operators / Logical Operator 
# # and: __and__(self, other)
# # or: __or__(self, other)
# # not: __not__(self)
# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def __and__(self, other):
#         return MyClass(self.value and other.value)

# a = MyClass(True)
# b = MyClass(False)
# c = a & b  
# print(c.value)


# # Assignment Operators
# # Operator	Magic Method
# # -=	__isub__(self, other)
# # +=	__iadd__(self, other)
# # *=	__imul__(self, other)
# # /=	__itruediv__(self, other)
# # //=	__ifloordiv__(self, other)
# # %=	__imod__(self, other)
# # **=	__ipow__(self, other)

# class Product:
#     def __init__(self):
#         self.price = float(input("enter price "))
#         # self.name , self.stock, self.disc
#     def __iadd__(self,other):
#         self.price += other.price 
#         return self.price
#     def __str__(self):
#         return str(self.price)
# p1 = Product()
# p2 =Product()
# p1+=p2
# print(p1) 
######################################
# # Unary Operators
# # Operator	Magic Method
# # -	__neg__(self)
# # +	__pos__(self)
# # ~	__invert__(self)
########################################
# 5 -> 101 -> 010 