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

# Getting datetima information

from datetime import datetime
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

# Timestamp or Unix timestamp is the number of seconds elapsed from 1st of January 1970 UTC.

# Formatting date output using strftime
