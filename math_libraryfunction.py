########## math
import math
# print(math.factorial(10))
# print(math.gcd(10,15,17,20))
# print(math.gcd(10,15,20))
# # # N! / (N-K)! * (K!)
# print(math.comb(10,2))
# print(math.lcm(100,111))
# print(math.lcm(100,200))

# print(math.sqrt(100))
# print(math.sqrt(100.100))
# print(math.isqrt(100))
# print(math.isqrt(100.100)) # error

# import numpy as np 
# arr1 = np.array(list(map(int, input("enter numbers(seperated by , ) ").split(","))))
# print(np.sqrt(arr1))
    
# from math import *
# print(sqrt(100))

# from math import comb, lcm
# print(comb(10,2))
# print(lcm(100,111))

# from math import *
# print(perm(10,2));

# print(ceil(100.9))
# print(ceil(100.0001))
# print(floor(100.9))
# print(floor(100.0001))

# sp=  eval(input("enter sp"))
# cp = eval(input("enter cp "))
# p_l = cp - sp 
# print(fabs(p_l))
# if (p_l>0):
#     print("profit ")
# elif(p_l==0):
#     print("no profit - no loss")
# else:
#     print("loss")

import math 

# print(math.remainder(100,10))
# print(math.remainder(100,3))

# print(math.frexp(1))   #m * 2**e 
# print(math.frexp(100))

# a= -1
# b = 1 
# print(math.copysign(a,b))
# print(math.copysign(b,a))

# print(math.isfinite(10/10))
# print(math.isinf(math.inf))
# import numpy as np
# print(math.isnan(np.nan)) # not a number
# print(math.isfinite(np.nan))

# print("next after")
# print(math.nextafter(100, 120))
# print(math.nextafter(100, 200))
# print(math.nextafter(100, 120, steps=100000000000000))
# print(math.nextafter(100, 200,steps=20))


# print(math.exp(1))
# print(math.exp2(0))

# str1 = "1110"
# sum = 0 
# count = 0
# for i in str1[::-1]:
#     sum+= int(i) * math.exp2(count)
#     count+=1
# print(sum)

# print(math.cbrt(225))
# print(math.log(100))

print(math.log(int(input("number")), int(input("base"))))

print(math.log2(100))
print(math.log10(100))
a = 25000
b = 2500000
print(math.log10(a))
print(math.log10(b))
print(math.pow(10,2))

###############################
print(math.hypot(3,4))
print(math.prod((10,3,4,5,6)))

print(math.degrees(100))
print(math.radians(90))
### sin cos tan 
print(math.sin(1.57))

# asin, acos, atan
# asinh, acosh, atanh
