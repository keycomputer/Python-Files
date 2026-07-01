# str1=  'abc'
# str2 = "abc"
# str3 ='''abc'''
# str4 ="""abc"""
# print(str1)
# print(str2)
# print(str3)
# print(str4)


# str1=  'abc\nxyz'
# str2 = "abc\nxyz"
# str3 ='''abc
# xyz'''
# str4 ="""abc
# xyz"""
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# ///// raw literal 
str1 = "C:\newfolder\temp "
print(str1)
str2 ="C:\\newfolder\\temp"
print(str2)
str3 = r'C:\newfolder\temp'
print(str3)

# ///////////////////
# a = str(1)
# print(a, type(a))

# a = str(1.1)
# print(a, type(a))

############ +  *  ###########
# str1 = "abc"
# str2 = "xyz"
# print(str1 + str2)

# print(str1 * 10)

##########  in , not in ###########
# str1 = "abcdefghijkl"
# print("de" in str1)
# print("de" not in str1)

# ////////// index  
#   0 1 2 3 4 5 6 7 8 9 
#   A B C D E F G H I J 
# -10-9-8-7-6-5-4-3-2-1 
# str1 = "ABCDEFGHIJ"
# print(str1[0])
# print(str1[-10])
# print(str1[9], str1[-1])

#//////////// SLICING 
# [ start : stop :  step ]

#   0 1 2 3 4 5 6 7 8 9 
#   A B C D E F G H I J 
# -10-9-8-7-6-5-4-3-2-1 
# str1 = "ABCDEFGHIJ"
# print(str1[0:10 ])
# print(str1[-10 : -1 ])
# print(str1[ : ])
# print(str1[ : : ])
# print(str1[ : 5]) # start , end= 4 index 
# print(str1 [5 : ]) # start =5, end 
# print(str1[-10: ]) # line 64 , end 
# print(str1 [ -4: ]) 

# print(str1[ :: 2]) # start, end, step =2 
# print(str1[ 0 : 7:2])
# print(str1[9:2:-1]) 
# print(str1[-1:-8:-1 ])


# print(str1[ : : -1 ]) ## reverse the data 

# str1 = "abcdef"
# str2 = r'abcdef'
# print(str1, str2)  # no difference 

# str1 = "abc\ndef"
# str2 = r'abc\ndef'
# print(str1, str2) # diff 

# str1 = "C:\newfolder\temp\abc"
# str2 = r'C:\newfolder\temp\abc'
# str3 = "C:\\newfolder\\temp\\abc"

# print(str1)
# print(str2)
# print(str3)

# str4 = "'this is a quote'"
# print(str4)
# str4 = '"this is a quote"'
# print(str4)
# str4 = "\"this is a quote\""
# print(str4)
###########################################
# name = "abcde"
# for i in name:
#     print(i)

# for i in range(len(name)): # start 0 stop length-1 
#     print(name[i])

# i=0
# while i <len(name):
#     print(name[i])
#     i=i+1 

# print(name[0], name[-len(name)])
# print(name[len(name)-1], name[-1])
######################################

# str1 = input("Enter data ")
# print(str1) # "1" , "1.1" , "abc"

# num = 1 
# str1 = str(num)
# print(str1, type(str1))
# num2 = int(str1)
# print(num2, type(num2))

# num = 1.1 
# str1 = str(num)
# print(str1, type(str1))
# num2 = float(str1)
# print(num2, type(num2))
######## Slicing ############### 
# name = "abcde"
# print(name[:])
# print(name[::])
# print(name[1:4])
# print(name[ : 4 : 2 ])
# print(name[::2])
# print(name[4: 1:-1])
# print(name[::-1]) # reverse 
# print(name[-5:])
# print(name[-5:3])
# print(name[-1:-5:-1])

##########################   Operators ################### 
# +  (concatenate / Joining )
# fname = input("Enter first name ")
# lname = input("Enter last name ")
# fullname= fname + lname
# print(fullname)

# fullname= fname + " " + lname
# print(fullname)

# # fullname = fullname + 1  # error 
# fullname = fullname + str(1) # type casting 
# print(fullname)

####  *  replicate 
# str1 = "abc"
# print(str1 * 10 )

# str1 = "a"
# for i in range(1,6):
#     print(str1*i)

#########  in / not in 

# sentence = input("Enter sentence")
# word = input("Enter word ")

# print(word in sentence)
# print(word not in sentence)

############### 
# a
# ab 
# abc 
# abcd 

# str1 ="abcd" 
# for i in range(4):
#     print(str1[:i+1])

# str2 = ""
# for i in range(4):
#     str2 = str2 + str1[i]
#     print(str2)

######################################
# chr 
# print(chr(65))
# print(chr(97))

# ord 
# print(ord("A"))
# print(ord("a"))

# A 
# AB 
# ABC 
# ABCD 

# str1 =""
# for i in range(4):
#     str1 += chr(65+i)
#     print(str1)
# ABCD 
# ABC 
# AB 
# A 
# str1 = "ABCD"
# for i in range(len(str1)):
#     print(str1[ : len(str1)-i])

######################## 
# #1 
# print("abc".isupper())
# #2 
# print("abc".islower())
# #3
# print("abc".isalnum())
# #4
# print("abc".isalpha())
# #5
# print("123".isdigit())
# #6 
# print(" ".isspace())
# #7 
# print("This Is String".istitle())

# #8 
# print("abc".upper())
# print("aBc".upper())
# #9 
# print("ABC".lower())
# print("aBc".lower())
# #10 
# print("aBc".swapcase())
# # 11 
# print("this is string".capitalize())
# #12 
# print("this is string".title())
#13 
print("   this is string     ".strip()) # right and left space 
print("the abc the".strip("the"))
print("the abc the".strip("the").strip())
#14 
print("   this is string     ".lstrip()+"abc")
#15 
print("   this is string     ".rstrip() + "abc")
#16 
sentence = "this these those there they the those"
L1 = sentence.split()
print(L1)
L2 = sentence.split("s")
print(L2)
L3 = sentence.split("those")
print(L3)
# 17 
date = "29-5-2024"
L1 = date.split("-")
print(L1)
date2 = "/".join(L1)
print(date2)
#####################
str2 = " ".join("abc")
print(str2)
#18 
str1 = "abcabcabcabc"
print(str1.replace("a","X"))
print(str1)
str1 = str1.replace("a","z")
print(str1)

#19 
# partition - size 3 

str1 = "this those this those"
t1= str1.partition("those")
print(t1)
t1= str1.partition("these")
print(t1)

# 20 
str1 = "this those this those"
print(str1.startswith("this"))

# 21 
print(str1.endswith("this"))

# 22 
print("456.78".zfill(10))

# 23 
print("abc".center(50))
print("abc".center(50,"-"))

#24 
print("abc".ljust(50))
print("abc".ljust(50,"-"))
#25 
print("abc".rjust(50))
print("abc".rjust(50,"-"))

# 26
# index

# # 27 
# find 

# # 28 
# casefold()

# #29
# isidentifier()

# #30
# isprintable()

# #31
# splitlines()

# 26
# index , rindex
str1 = "abcabcabc"
print(str1.index("a"))
# print(str1.index("z")) # error 
if "z" in str1:
    print(str1.index("z"))
else:
    print("not found ")
# print(str1.index("a", 1))
# print(str1.index("a", 1,2))
# print(str1.index("a",-5)) # using negative indexing 

# str1 = "abcdefa"
# print(str1.index("a"))
# print(str1.rindex("a"))
# # 27 
# find , rfind 

# str1 = "abcabcabc"
# print(str1.find("a"))
# print(str1.find("z")) # -1 for not found 

# print(str1.find("a", 3))
# print(str1.find("a",4, 6))
# str1 = "abcdefagh"
# print(str1.find("a"))
# print(str1.rfind("a"))

# # 28 
# casefold()
# str1 = "AbcDefXYzß (î).  œ̃"
# print(str1.casefold())
# print(str1.lower())

# #29
# isidentifier()
# name = ""
# print(name.isidentifier())
# name=  "abc"
# print(name.isidentifier())
# name="1b"
# print(name.isidentifier())
# name= "a1"
# print(name.isidentifier())
# name = "_a"
# print(name.isidentifier())


# #30
# isprintable()
# str1= "Я"
# print(str1.isprintable())

# #31
# splitlines()
# str1 ="the these\nthose\nthey"
# L1 = str1.splitlines()
# print(L1)
# str1 ="""the these
# those
# they"""
# L1 = str1.splitlines()
# print(L1)

# 32 count 
# str1 ="the these\nthose\nthey"
# print(str1.count("the"))

# print(str1.replace("the","are"))
########################################################################
# import string
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
# print(string.whitespace)

#######################################################################
# print("a\tb\tc")
# print("a\tb\tc".expandtabs(12))
# print("a\tb\tc".expandtabs(0))

#################################################################

# name="abc"
# age = 21
# location ="Delhi"
# print("Name = {}, Age = {}, and Location = {} ".format(name,age, location))
# print("Name = {0}, Age = {1}, and Location = {2} ".format(name,age, location))
# print("Name = {2}, Age = {0}, and Location = {1} ".format(age, location,name))
# // or 
# print("%s %s %s" %(name, age, location))

################################################################
# str1= "the there is they their my are"
# str1 = str1.removesuffix("are")
# str1 = str1.removeprefix("the")
# print(str1)

###############################################################
# str1 ="abc1\nabc2\nabc3\nabc4"
# L1 = str1.splitlines()
# print(L1)

# str1="hello"
# print(str1.encode("cp866"))


# table = str.maketrans("abc123 d", "xyz$%^!D")
# print(table)
# str1="abc 123 D"
# print(str1.translate(table))

# count (frequency)

# str1 = input("Enter sentence ")
# word = input("Enter word ")

# list1 = str1.split()
# count = 0 
# for i in list1:
#     if i == word:
#         count+=1 
# if count == 0:
#     print("Not Found ")
# else:
#     print("Found - Freq -", count)
############################################################
# count=0
# for i in range(len(str1)):
#     if str1[i] == word[0]:
#         j=0 
#         while j<len(word) and str1[i+j] == word[j] :
#             j=j+1 
#         if j == len(word) and str1[i+j]==" " and str1[i-1]==" ":
#             count= count+1
# print(count)

############################################################

# replace 

# str1 = "this the are is the they their are"
# L1 = str1.split()
# str2 = ""

# for i in L1:
#     if i == "the":
#         str2 += "a "
#     else:
#         str2 += i+" "
# print(str2.strip()+"abc")