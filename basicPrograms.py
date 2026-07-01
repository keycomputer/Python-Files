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

# amount = int(input("enter "))
# n500 = amount // 500 
# # amount = amount - (n500 * 500)
# amount = amount % 500 

# n200 = amount // 200 
# amount= amount % 200 

# n100 = amount // 100
# amount = amount % 100

# n50 = amount // 50
# amount = amount % 50

# n20 = amount // 20
# amount = amount % 20

# n10 = amount // 10
# amount = amount % 10
# print(n500, n200, n100,n50, n20, n10 )

######################################\
    # reverse of four digit 
# num = int(input("enter any number "))
# rev = 0 
# r = num % 10 
# # rev = r * 1000 
# rev = rev * 10 + r # 0 * 10 + 4 
# num = num // 10 

# r = num % 10 
# # rev = rev + r * 100
# rev = rev * 10 + r   # 4 * 10 + 3 
# num = num // 10 

# r = num % 10 
# # rev = rev + r * 10 
# rev = rev * 10 + r 
# num = num // 10 

# r = num % 10 ## 1 %10 ??? 
# # rev = rev + r
# rev = rev * 10 + r  
# num = num // 10 ## 1 // 10 
# print(rev)


#########################################
# r = int(input("enter any number "))
# area  = 3.14 * r * r 
# circ  = 3.14 * 2 * r 
# print(area, circ)
# ######################
# l=int(input("enter l "))
# b=int(input("enter b ")) 
# area = l*b 
# peri = 2*(l+b)
# print(area, peri)
# ######################
# side = int(input("enter side "))
# area = side ** 2 
# peri  = 2 *side 
# print(area, peri)
#####################################################
### Assignment Operator 
# += -= *= /= //= **= %= 
# a = 10 
# a = a + 1 
# a += 1
# print(a)
# ########################
# a = a - 1 
# a -= 1
######################################################
# relational operator / conditional 
# > < >= <= == != 
# num1 = int(input("enter"))
# num2 = int(input("enter"))
# print(num1  > num2)
# print(num1  < num2)
# print(num1  >= num2)
# print(num1  <= num2)
# print(num1  == num2)
# print(num1  !=  num2)
###########################################################
## # if ,  if else , if elif , if if or else if 
# num=int(input("enter "))
# if num > 100: 
#     print("yes")
#     print("number is greater than 100 ")
# else:
#     print("No")
#     print("number is not greater than 100 ")   
######################################
# max ( two numbers)
# a = int(input())
# b = int(input())
# if a > b :
#     print("A is greater")
# if b > a :
#     print("B is greater ")
# if a == b:
#     print("A equal B")
########################
# if a > b: 
#     print("A")
# elif b> a:
#     print("B")
# else:
#     print("equal ")
    
######################################
salary = int(input("enter basic "))
gross = salary * 12 
if gross <= 400000:
    tax = 0 
elif gross <= 800000:
    tax = gross*0.05
elif gross <= 1200000:
    tax = gross*0.10
elif gross <= 1600000:
    tax = gross*0.15
elif gross <= 2000000:
    tax = gross*0.20 
elif gross <= 2400000:
    tax = gross*0.25 
else:
    tax = gross *0.30 
print("Tax =", tax)

#################and or not logical operators #################

######## leap year 
######## buzz 
######## divisibility
########################





