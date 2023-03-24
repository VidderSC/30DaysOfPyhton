# Day 16 - 30DaysOfPython Challenge

# Pyhton datetime
"""
Python has got datetime module to handle date and time.

import datetime
print(dir(datetime))
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 
'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

With dir or help built-in commands it is possible to know the available 
functions in a certain module. As you can see, in the datetime module 
there are many functions, but we will focus on:
- date, datetime, time and timedelta.
"""
from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

# Getting datetime information

# from datetime import datetime
now = datetime.now()

print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(day, month, year, hour, minute)
print("timestamp", timestamp)
print(f"{day}/{month}/{year}, {hour}:{minute}:{second}")
print()

# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

# Formatting date output using strftime
# Link to strftime cheatsheet: https://strftime.org/

# from datetime import datetime
t = now.strftime("%H:%M:%S")
print("Time:", t)

t1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Time:", t1)

t2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("Time:", t2)
print()

# String to Time Using strptime
DATE_STRING = "14 February, 2019"
print("DATE_STRING:", DATE_STRING)
date_object = datetime.strptime(DATE_STRING, "%d %B, %Y")
print("date_object:", date_object)
print()

# Using date from datetime

# from datetime import date
d = date(2019, 2, 14)  # YYYY, MM, DD format
print(d)
print("Current date:", d.today())
today = date.today()  # Date Object of today's date
print("Current year: ", today.year)
print("Current month: ", today.month)
print("Current day: ", today.day)
print()

# Time objects to represent time

# from datetime import time
# time(hour = 0, minute = 0, second = 0) by default.
a = time()
print("a =", a)
# we can pass the values without the descriptors
b = time(10, 30, 50)
print("b =", b)
c = time(hour=10, minute=30, second=50)
print("c =", c)
# time(hour, minute, second, millisecond)
d = time(10, 30, 50, 200555)
print("d =", d)
print()

# Difference between two points in time using date and datetime.
today = date(year=today.year, month=today.month, day=today.day)
NEW_YEAR = date(year=2024, month=1, day=1)
time_left_to_new_year = NEW_YEAR - today
print("time left to new year:", time_left_to_new_year)

t1 = datetime(year=now.year,
              month=now.month,
              day=now.day,
              hour=now.hour,
              minute=now.minute,
              second=now.second)
N_YEAR = datetime(year=2024,
                  month=1,
                  day=1,
                  hour=0,
                  minute=0,
                  second=0)
diff = N_YEAR - t1
print("time left to new year:", diff)
print()

# Difference between two points in time using timedelta

# from datetime import timedelta
TIME1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
TIME2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
time3 = TIME1-TIME2
print("TIME1 =", TIME1)
print("TIME2 =", TIME2)
print("time3 =", time3)
