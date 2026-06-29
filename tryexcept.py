# Python uses try and except to handle errors gracefully. 
# A graceful exit (or graceful handling) of errors is a simple programming 
# idiom - a program detects a serious error condition and "exits gracefully", in a controlled manner as a result. 
# Often the program prints a descriptive error message to a terminal or log as part of the graceful exit, this 
# makes our application more robust. The cause of an exception is often external to the program itself.
# An example of exceptions could be an incorrect input, wrong file name, unable to find a file, 
# a malfunctioning IO device. Graceful handling of errors prevents our applications from crashing.

# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong



try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
    
    
    
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
    
    ####################################################
    
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
    
####################################################

# It is also shorten the above code as follows:

try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)