# array  -> homogeneous elements -> ndarray 

# import numpy 
import numpy as np  # alias np 

#  1. array 
arr1= np.array([1,2,3,4,5,6,7,8])
print(arr1)

# 2. arange(start, stop, step )
arr2 = np.arange(1,100,5)
print(arr2)
arr2 = np.arange(1,100,15.5)
print(arr2)

# 3. Zeros and Ones 
arr1  = np.zeros(10) # one dimensional array
print(arr1)
arr1  = np.zeros((3,10)) # two dimensional array
print(arr1)

arr1  = np.ones(10)
print(arr1)
arr1  = np.ones((3,10))
print(arr1)

# 4. full
arr1 = np.full(10,100)
print(arr1)
arr2 = np.full((3,10), 100)
print(arr2)
##################3 random functions ##########################
print(np.random.rand()) 
print(np.random.random()) 
############
print(np.random.randint(1,100,size=5))

print(np.random.rand(5)) # 5 size , of float values 
List1 = [10,265,32,3,56,67,3,32,56,56]
print(np.random.choice(List1))  # generate random value based on an array / List 

print(np.random.choice(List1, 4))

########### accessing elements ################
arr1 = np.array([4,7,345,67,54,6,67,3432])
print(arr1[6]) # 6th index value 

arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1[1, 2]) # 2ndrow and 3 column data index value   # List1[2][3]

#### negative indexing 
arr1 = np.array([4,7,345,67,54,6,67,3432])
print(arr1[-6]) # reverse -1, -2 til -6
arr1 = np.array([[1,2,3], [4,5,6]])
print(arr1[-1, -2]) # 2ndrow and 2 column data index value  
#######################################################
#### Slicing ####
arr1 = np.array([4,7,345,67,54,6,67,3432])
print(arr1[ : ])
print(arr1[ 1 : 4])
print(arr1[4: ])
print(arr1[ :  4])
#################################### 
### fancy slicing ########### 
print("-----------------  Indexing using array ------------")
import numpy as np 
# arr1 = np.arange(1,10)
arr1 = np.array([32454,65757,3232,567678,32323,34554,1345423,34346,234543,546534,546342,4356342])
indices = np.array([2,5,8])
print("Array " , arr1 )
print(arr1 [ indices ])# arr1[[2,5,8]]


 
#### Boolean indexing #### 
print("----- Boolean Indexing -------- ")
arr1 = np.array([32454,65757,3232,567678])
indices = np.array([True, False , True, False])
print(arr1[indices])
print("------ Example ----------")
booleanIndices = arr1 > 50000 
print("Index values - ", booleanIndices)
print("Values  - ", arr1[booleanIndices])

################################################################

print("------------  2D array - Slicing ---------------- ")
arr1  = np.array([ [30, 10] , [25, 15] ,[18, 21  ] ])

print(arr1[: , : ])
print(arr1[1, : ]) # row no 1(index), all columns 
print(arr1 [0 : 2 , 1:2 ])

print("------------ Copy using assignment ---------------- ")
arr2 = arr1 
arr2[0, 0] = 31
print(arr1)
print(arr2)
arr3 = arr1[1 , : ] # [25,15 ]copy 
arr3[0]  = 27
print(arr1)
print(arr3)
print("------------ Copy using function ---------------- ")
arr2 = arr1.copy()
arr2[0, 0] = 31
print(arr1)
print(arr2)
arr3 = arr1[1 , : ].copy() # [25,15 ]copy 
arr3[0]  = 27
print(arr1)
print(arr3)
print("-------------------- Functions -----------------------") 
print("---- SUM function ---- ")
import numpy as np 
arr1 = np.array([234,5476,78,3,34,67])
print(np.sum(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.sum(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.sum(arr1, axis=0))  # column by 
print(np.sum(arr1, axis=1))  # row  by 

print("Mean function ")
import numpy as np 
arr1 = np.array([234,5476,78,3,34,67])
print(np.mean(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.mean(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.mean(arr1, axis=0))  # column by 
print(np.mean(arr1, axis=1))  # row  by 

print("Median function ")
import numpy as np 
arr1 = np.array([234,5476,78,3,34,67])
print(np.median(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.median(arr1))
arr1 = np.array([[234,5476] ,[78,3],[34,67] ]) # 3 X 2 
print(np.median(arr1, axis=0))  # column by 
print(np.median(arr1, axis=1))  # row  by 
print("--- VAR function ----- ")
print(np.var(arr1))
print(np.std(arr1))
print(np.var(arr1, axis=0))
print(np.std(arr1, axis = 1))
print(np.var(arr1, axis = 0))
print(np.std(arr1, axis = 1))

print(" ---------  Min and MAX -------------")
arr1 = np.array([56,33,78,32,11,467,90,0,34])
print(np.min(arr1))  # max
print(np.amin(arr1))  # amax
arr1 = np.array([[56,33,78],[32,11,467],[90,0,34] ])
print(np.amin(arr1, axis = 0))
print(np.amin(arr1, axis = 1))

print("Product of Data ", np.prod(arr1))
print("Absolute Value ", np.abs(arr1))

##################
# print("--------- Addition ------------")
# arr1 = np.array([10,20,30])
# arr2 = np.array([1,2,3])
# print(np.add(arr1, arr2))
# print(arr1 + arr2 )
# print("--------- Subtraction ------------")
# print(np.subtract(arr1, arr2))
# print(arr1 - arr2 )

# np.multiply( )
# arr1 * arr2 
# np.divide(arr1, arr2)
# arr1 / arr2 
# np.mod(arr1, arr2)
# arr1 % arr2 ###############
###############################################

## all()
import numpy as np
arr1 = np.array([4,6,7,8,2])
print(all(arr1))
arr1 = np.array([1,6,2,1,34,6,7,4,2,1,15,7])
arr2 = arr1 [ arr1 > 5]
print(arr2)
print(all(arr2))
print("----------------")
arr3 = arr1 > 5 
print(arr3)
print(all(arr3))

arr1 = np.array([[1,0],[2,1],[34,6],[7,4],[2,1],[0,7]])
r = np.all(arr1, axis=0)
print(r)
print(np.all(arr1, axis=1))


######### any()
import numpy as np
arr1 = np.array([4,6,7,8,2])
print(np.any(arr1))
arr1 = np.array([1,6,2,1,34,6,7,4,2,1,15,7])
arr2 = arr1 [ arr1 > 5]
print(arr2)
print(np.any(arr2))
print("----------------")
arr3 = arr1 > 5 
print(arr3)
print(np.any(arr3))

arr1 = np.array([[1,0],[2,1],[34,6],[7,4],[2,1],[0,7]])
r = np.any(arr1, axis=0)
print(r)
print(np.any(arr1, axis=1))

###################### reshape ###################
a = np.arange(1, 11)
print(a)
b = np.reshape(a, (2,5))
print(b)
c = np.transpose(b)
print(c)
################ sort 
arr1 = np.array([1,6,2,1,34,6,7,4,2,1,15,7])
arr2 = np.sort(arr1)
print(arr2)
arr2 = np.sort(arr1)[::-1]
print(arr2)
a = np.array([
    [12, 30, 11],
    [50, 16, 24]
])
b = np.sort(a)
print(b)
b = np.sort(a, axis = 0 )
print(b)
##############################

import numpy as np
dtype = [('name', 'S10'),
         ('year_of_services', float),
         ('salary', float)]
employees = [
    ('Alice', 1.5, 12500),
    ('Bob', 1, 15500),
    ('Jane', 1, 11000)
]
payroll = np.array(employees, dtype=dtype)
result = np.sort(
    payroll,
    order=['year_of_services', 'salary']
)
print(result)