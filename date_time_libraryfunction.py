from datetime import date
d = date(1996, 12, 11)
print(d)


from datetime import date
t = date.today()
print(t)


from datetime import date
t = date.today()
print(t.year)
print(t.month)
print(t.day)


from datetime import datetime
date_time = datetime.fromtimestamp(1887639468)
print(date_time)
print(date_time.date())


from datetime import date
t = date.today()
date_str = t.isoformat()
print(date_str)
print(type(date_str))


#####################################################################

from datetime import time

# Create time object with hour, minute and second
my_time = time(13, 24, 56)
print("Entered time:", my_time)

# Time object with only minute specified
my_time = time(minute=12)
print("Time with one argument:", my_time)

# Time object with default (00:00:00)
my_time = time()
print("Time without argument:", my_time)

# time(hour=26)      → ValueError: hour must be in 0..23
# time(hour='23')    → TypeError: string passed instead of int

#########
from datetime import time

Time = time(11, 34, 56)
print("hour =", Time.hour)
print("minute =", Time.minute)
print("second =", Time.second)
print("microsecond =", Time.microsecond)


##############

from datetime import time

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
Str = Time.isoformat()
print("String Representation:", Str)
print(type(Str))


#Datetime class
from datetime import datetime

# Initializing constructor
a = datetime(1999, 12, 12)
print(a)

# Initializing constructor with time parameters as well
a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

from datetime import datetime

a = datetime(1999, 12, 12, 12, 12, 12)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

from datetime import datetime

# Calling now() function
today = datetime.now()
print("Current date and time is", today)


from datetime import datetime as dt

# Getting current date and time
now = dt.now()
string = dt.isoformat(now)
print(string)
print(type(string))