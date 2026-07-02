year = int(input("enter year "))
# According to the Gregorian calendar, which is the 
# civil calendar in use today, years evenly divisible 
# by 4 are leap years, with the exception of centurial 
# years that are not evenly divisible by 400. Therefore, 
# the years 1700, 1800, 1900 and 2100 are not leap years,
# but 1600, 2000, and 2400 are leap years.
if year % 100 == 0:
    if year % 400 == 0:
        print("leap")
    else:
        print("not a ")
else :
    if  year % 4 == 0 :
        print("leap")
    else:
        print("not a ")