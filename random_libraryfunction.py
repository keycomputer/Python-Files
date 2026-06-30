# import random 

# print(random.random())

from random import *
# print(random())   #0 to <1 
# print(randint(1,11)) # inclusive
# seed(1)
# print(random())
# print(random())
# print(random())
# print(random())
# print(random())
# seed(10)
# print(random())
# print(random())
# print(random())
# print(random())
# seed(1)
# print(random())
# print(random())
# print(random())
# print(random())
# seed(10)
# print(random())
# print(random())


# print(randrange(1,11))
# print(randrange(1,11,3))
print(uniform(1, 10))  # floating 

# L1 = [1,2,3,4,5]
# shuffle(L1)
# print(L1)
# print(choice(L1))

# print(getstate())


# seed(0)
# print("seed 0 ")

# s = getstate()
# print(random())
# print(random())
# print(random())
# # print(s)
# setstate(s)
# print("SetState ")
# print(random())
# print(random())
# print(random())
# print(random())
# print(random())
# print(random())
# seed(0)
# print("seed 0")
# print(random())
# print(random())
# print(random())



print(randbytes(10))
print(getrandbits(2))
L = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16]
L1 = sample(L, k = 5)

print(L1)

print(binomialvariate(n=1, p=0.5))
# https://www.geeksforgeeks.org/python-random-function/
# https://docs.python.org/3/library/random.html#random.setstate