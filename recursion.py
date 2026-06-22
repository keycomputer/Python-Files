# def display():
#     print("hello ")
#     display()

# display() 
###################  
# def printNumber(n1, n2):
#     if n1 > n2:
#         return 
#     else:
#         print(n1,end=" ")
#         printNumber(n1+1, n2)
# # (1,10) -> 1 (2,10)-> 2 (3,10) -> (10,10) _> 10 (11,10)return 
# printNumber(1,10)
######################

# def printNumber(n1, n2):
#     if n1 < n2:
#         return 
#     else:
#         print(n1,end=" ")
#         printNumber(n1-1, n2)
# printNumber(10,1 )
##########################

# def sumofN(Num):
#     # Base Case -> stop 
#     if Num == 1:
#         return 1
#     else:
#         return (Num + sumofN(Num-1))   
# # (5) -> 5 + (4) -> 4 + (3)-> 3+ (2) + 2+(1) -> 1 STOP 
# num = int(input("Enter "))
# result = sumofN(num)
# print("Result = ", result)
################################################


# def factorial(Num):
#     # Base Case -> stop 
#     if Num == 1:
#         return 1
#     else:
#         return (Num * factorial(Num-1))   
# # (5) -> 5 * (4) -> 4 * (3)-> 3 * (2) + 2*(1) -> 1 STOP 
# num = int(input("Enter "))
# result = factorial(num)
# print("Result = ", result)
####################################################

# def primeNumber( n , i ):
#     if i == 1 :
#         return 1 
#     elif n % i == 0:
#         return 0 
#     else   :
#         return (primeNumber(n, i-1))
    
# n = int(input("Enter any number "))
# if primeNumber( n, n-1  ) == 1 :
#     print("Yes")
# else:
#     print("no")
####################################################
# def factors (N, i = 1 ):
#     if (i == N):
#         print(i)
#         return 
#     elif (N % i == 0):
#         print(i, end=" ")
#     factors(N, i+1 )
# factors(10)
#######################################
# def sumofFactors(N, i=1): 
#     if (i == N):
#         return i
#     elif (N % i == 0):
#         print(i, end=" ")
#         return(i + sumofFactors(N, i+1 )) 
#     else:
#         return(0 + sumofFactors(N, i+1 ))
# print("Sum of Factors " ,sumofFactors(10))
#############################################
def fibonacci (N):
    if N == 0 :
        return 0 
    elif N == 1 :
        return 1 
    else :
        return( fibonacci(N-1 ) + fibonacci(N-2))
# print(fibonacci(4))  # 0 1 1 2 3 
for i in range( int(input("enter nth term "))):
    print(fibonacci(i ), end=" ") 
################################################ 