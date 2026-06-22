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

import numpy as  np 
import pandas as pd 
arr1 = np.array([10,11,12])
s1 = pd.Series(arr1)
print(s1+10) #  + - % / // ** , > < >= <= == !- 

## add operation on two series 
series1 = pd.Series([1,2,3,5,6,7,9,1,10])
series2 = pd.Series([2,3,5,2,5,6,1,3,0])

print("Sum of series 1 and series 2 :\n",series1.add(series2))
# sub ,  mul etc 

print(" >  ", series1 > series2)
################## attributes #######################################
import numpy as  np 
import pandas as pd 
arr1 = np.array([10,11,12])
s1 = pd.Series(arr1)
print(s1.dtype)
print(s1.values)
print(s1.ndim , s1.shape)
print(s1.values.itemsize) # 8 byte 
print(s1.size)
####################################################################
############################### DataFrame ##########################
L1 = [ ["abc",20] ,["abc2",25],["abc3",30]]
df1= pd.DataFrame(L1, index=["e1","e2","e3"], columns=["name","age"])
print(df1)

data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
################
df.to_csv("mydata.csv")
########## read csv  ###################
df = pd.read_csv('data.csv')
print(df)
