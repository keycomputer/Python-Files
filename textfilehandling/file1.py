# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

############################################################
### text file handling ###
# file1 = open("file1.txt", "w")  # open file in write mode
# file1.write("Hello, this is a sample text file.\n")
# file1.write("This file is created for demonstration purposes.\n")
# file1.close()
###################################
# List1=[] # list of sentences
# file1= open("file1.txt","w")
# n = int(input("Enter number of sentences you want to write in the file: "))
# for i in range(n):
#     sentence = input("Enter sentence {}: ".format(i+1))
#     List1.append(sentence+"\n") # add newline character to each sentence
# file1.writelines(List1) # write list of sentences to the file
# file1.close()
####################################
# file1 = open("file1.txt", "r")  # open file in read mode
# content = file1.read()  # read the entire content of the file
# print(content)
#########################
# file1 = open("file1.txt", "r")  # open file in read mode
# content = file1.readlines() # read the content of the file line by line
# for i in content:
#     print(i) 
# file1.close()
# ###########################
# file1 = open("file1.txt", "r")
# str1 = file1.readline() # read the first line of the file
# while str1 != "":
#     print(str1)
#     str1 = file1.readline() # read the next line of the file
# file1.close()
#########################################################################