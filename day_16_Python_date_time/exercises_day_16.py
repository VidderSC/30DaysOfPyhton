"""
-- Exercises: Day 16

1. Get the current day, month, year, hour, minute and timestamp 
from datetime module

2. Format the current date using this format: "%d/%m/%Y, %H:%M:%S".

3. Today is 24 March, 2023. Change this time string to time.

4. Calculate the time difference between now and new year.

5. Calculate the time difference between 1 January 1970 and now.

6. Think, what can you use the datetime module for? Examples:
    - Time series analysis
    - To get a timestamp of any activities in an application
    - Adding posts on a blog
"""

from datetime import datetime
from datetime import date

day = datetime.day
month = datetime.month
year = datetime.year
hour = datetime.hour
minute = datetime.minute
timestamp = datetime.timestamp

current_date = datetime.now()
print("Current:", current_date.strftime("%d/%m/%Y, %H:%M:%S"))
print()

TODAY = "24 March, 2023"
today_object = datetime.strptime(TODAY, "%d %B, %Y")
print(today_object)

NEW_YEAR = datetime(year=2024,
                    month=1,
                    day=1,
                    hour=0,
                    minute=0,
                    second=0)

time_to_new_year = NEW_YEAR - datetime.now()
print("Countdown to New Year:", time_to_new_year)
print()

OLD_DATE = date(year=1970, month=1, day=1)
print("Days since OLD_DATE:", date.today() - OLD_DATE)
