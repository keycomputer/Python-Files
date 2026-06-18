# Ctrl + F5 
# Command+ f5 + fn 

##### Lambda #####
f1 = lambda x : x+1 
print(f1(1))

f2 = lambda x ,y : x + y 
print(f2(1,2))

f2 = lambda x ,y : x if x > y  else y 
print(f2(1,2))
###################################################
# ----- map -----
L1= [1,54,56,67,23,34,56,67,34,23,23,5,65,65]
L2 = list(map( lambda x : x +1 , L1))
print(L2)

################
# ----- filter -----
L1= [1,54,56,67,23,34,56,67,34,23,23,5,65,65]
L2 = list(filter(lambda x : x %2 ==0  , L1))
print(L2)
#################
# ---- reduce ------- 
import functools
n = [1, 2, 3, 4]
prod = functools.reduce(lambda x, y: x * y, n)
print(prod)

print (functools.reduce(lambda x, y: x * y, 
       list(map(int, input("enter list values seperated by space ").split() ))))

print(functools.reduce(lambda x, y: x + y,
            list(filter(lambda x : x > 10 , 
            map(lambda x : x +1 , 
            list(map(int, input("enter list values seperated by space ").split() ))
            )))))
###################################