# Method Overloading
# The process of calling the same method with different parameters is known as method overloading. Python does not support method overloading. 

# Overloading Built-in Functions
# Giving a Length to Your Objects Using len()
class Order:
    def __init__(self, cart, customer):
         self.cart = list(cart)
         self.customer = customer

    def __len__(self):
         return len(self.cart)

order = Order(['banana', 'apple', 'mango'], 'Real Python')
len(order)
# Work With abs()
class Vector:
    def __init__(self, x_comp, y_comp):
        self.x_comp = x_comp
        self.y_comp = y_comp

    def __abs__(self):
        return (self.x_comp ** 2 + self.y_comp ** 2) ** 0.5
vector = Vector(3, 4)
abs(vector)
5.0
#str()
def __str__(self):
    pass 
def __repr__(self):
    return f'Vector({self.x_comp}, {self.y_comp})'
def __bool__(self):
    return len(self.cart) > 0    

# Indexing and Slicing Your Objects Using []
class Order:
    def __init__(self, cart, customer):
        self.cart = list(cart)
        self.customer = customer

    def __getitem__(self, key):
        return self.cart[key]

order = Order(['banana', 'apple'], 'Real Python')
order[0]
# 'banana'
order[-1]
# 'apple'


###################################

class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()

vehicle.change_gear()

##################################################
# Overrride Built-in Functions

class Shopping:
    def __init__(self, basket, buyer):
        self.basket = list(basket)
        self.buyer = buyer

    def __len__(self):
        print('Redefine length')
        count = len(self.basket)
        # count total items in a different way
        # pair of shoes and shir+pant
        return count * 2

shopping = Shopping(['Shoes', 'dress'], 'Jessa')
print(len(shopping))
######################################
# Polymorphism In Class methods
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

ferrari = Ferrari()
bmw = BMW()

# iterate objects of same type
for car in (ferrari, bmw): 
    # call methods without checking class of object
    car.fuel_type()
    car.max_speed()
    
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)
############################################
# Operator Overloading in Python

# Special Methods for Operator Overloading
# Python provides specific methods for each operator.

# Binary Operators
# Operator	Magic Method
# +	__add__(self, other)
# -	__sub__(self, other)
# *	__mul__(self, other)
# /	__truediv__(self, other)
# //	__floordiv__(self, other)
# %	__mod__(self, other)
# **	__pow__(self, other)

class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

ob1 = A(1)
ob2 = A(2)
print(ob1 + ob2)
print(A.__add__(ob1, ob2))
print(ob1.__add__(ob2))

# Comparison Operators
# Operator	Magic Method
# <	__lt__(self, other)
# >	__gt__(self, other)
# <=	__le__(self, other)
# >=	__ge__(self, other)
# ==	__eq__(self, other)
# !=	__ne__(self, other)

class A:
    def __init__(self, a):
        self.a = a
    
    def __gt__(self, other):
        return self.a > other.a

ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")
    
#     Overloading Boolean Operators
# We can also overload Boolean operators using magic methods:

# and: __and__(self, other)
# or: __or__(self, other)
# not: __not__(self)
    
class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)

a = MyClass(True)
b = MyClass(False)
c = a & b  
print(c.value)


# Assignment Operators
# Operator	Magic Method
# -=	__isub__(self, other)
# +=	__iadd__(self, other)
# *=	__imul__(self, other)
# /=	__itruediv__(self, other)
# //=	__ifloordiv__(self, other)
# %=	__imod__(self, other)
# **=	__ipow__(self, other)
# Unary Operators
# Operator	Magic Method
# -	__neg__(self)
# +	__pos__(self)
# ~	__invert__(self)