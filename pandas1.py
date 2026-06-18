#  Series(1-D) and Data Frames(2-D )
# Panel(3-D)

# start -> command prompt (cmd) -> pip install conda
#                             pip install pandas

import pandas 
############# List  -> Series ###################
import pandas as pd 
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)
#############Numpy -> Series ################### 
import pandas as pd 
import numpy as np 
arr1 = np.array([1,2,3,4,5])
s = pd.Series(arr1)
print(s)
###############Custome Index ############
import pandas as pd 
import numpy as np 
arr1 = np.array([1,2,3,4,5])
s = pd.Series(arr1, index = [101,102,103,104,105])
print(s)
############################################
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)
###########################################
arr1 = np.array([1.1,2,3,4,5])
s = pd.Series(arr1, index = [101,102,103,104,105])
print(s)
############3 Creating Pandas Series from a Dictionary ##########
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s)
dct = {"name" :['a','b','c'], 'Age': [10,20,30]}
s = pd.Series(dct)
print(s)
###################### Accessing by Index ###################################
np_array = np.array([11,21,34,658,46,77,99,91,110])
data = pd.Series(np_array)
print("data present at index 1 is :",data[1])
print("First 5 data elements : ", data[:5]) # Slicing 
######
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
s = pd.Series(dct)
print(s[1], s['country'])
#####
np_array = np.array([11,21,34])
data = pd.Series(np_array, index = [1,1,2])
print("data present at index 1 is :",data[1])
##############3 
salesmen = pd.Series([3454,87,65,34,34,56,67,87], index=['N','S','N','W','S','N','E','W'])
print(salesmen['N'])
######################### loc and iloc functions ####################
np_array = np.array([1,2,3,5,6,7,9,1,10])
data = pd.Series(np_array, index =['A','B','C','D','E','F','G','H','I'])
# print("data extracted using .loc[] :\n",data.loc['B':'F']) # include F 
print("data extracted using .iloc[] :\n",data.iloc[1:6]) #exclude 6  
################################################################## 
# Binary Operations , Attribute  