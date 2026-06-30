##print(1)
##print("abc")
##print(123.45)
##
##print(1, end=" ")
##print(2, end=" ")
##print(3)
##
##print(1,2,3)
##print(1,2,3,sep="@")
#################################
##TOKEN
##1. keywords if else elif match for while
##2. identifier - a) alpha, underscore b) followed by number  c) space, special symbols
##3. operators - unary binary
##4. literals / constant 1 , 1.2(float), "a", 1+2j , True
##5. punctuators
##################################
##variable -> store data
# name = input("enter name ") # string 
# print(name)
#################################
# name = input("enter name ")
# print("Name =",name)
# age = int(input("enter age "))
# print("Age =", age)
# print("after 5 years age = ", age+5)
##################################

## type function in python
# a = 10 
# print(a , type(a))
# a = 10.123
# print(a , type(a))
# a = "abc"
# print(a , type(a))
# a = [1,2,3,4]
# print(a , type(a))
################################################
## int , float functions 
# a = "123"
# b = int(a)
# print(b, type(b))
# a = "123.45"
# # b = int(a) #ValueError
# b = float(a)
# print(b)
##################################################
# arithmetic operators 
# + - * /  //  **  % 
# num1 = int(input("enter number 1 "))
# num2 = int(input("enter number 2 "))
# print(num1 + num2 )
# print(num1 - num2 )
# print(num1 * num2 )
# print(num1 / num2 )
# print(num1 // num2 ) #floor division 
# print(num1 ** num2 ) # power 
# print(num1 % num2 ) # remainder 
################################################ 
####### salary ############ 
# basic= float(input("enter basic salary (monthly )  "))
# hra = basic * 0.40  # monthly  (40%)(house rent allowance)
# medical = 2500 # monthly 
# incentive = basic * 0.15 # 15% 
# gross  = basic + hra + medical + incentive 
# yearly = gross * 12 
# print("Gross salary = ", gross)
# print("Yearly salary = ", yearly)
##################################################

## swapping of two numbers
# num1 = int(input("enter "))
# num2 = int(input("enter "))

# num3 = num1  # num3= 1 
# num1 = num2 # num1 = 2 
# num2 = num3  # num2 = 1 
# print(num1, num2 )
### or  ### 
# num1 , num2 = num2 , num1 # packing and unpacking 
# print(num1, num2 )

###### 
# num1 = num1 ^ num2
# num2 = num1 ^ num2
# num1 = num1 ^ num2

# num1 = num1 + num2 
# num2 = num1 - num2 
# num1 = num1 - num2 

######################################################










