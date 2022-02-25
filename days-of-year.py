# Scenario
# Your task is to write and test a function which takes three arguments 
# (a year, a month, and a day of the month) and returns the corresponding day of the year,
# or returns None if any of the arguments is invalid.
# Use the previously written and tested functions. Add some test cases to the code.
# This test is only a beginning.

from calendar import SUNDAY
from http.client import SWITCHING_PROTOCOLS


def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False                
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month == 1:
        return 31
    if is_year_leap(year) == True:
        if month == 2:
            return 29
    else:
        if month == 2:
            return 28
    if month == 3:
        return 31
    if month == 4:
        return 30
    if month == 5:
        return 31
    if month == 6:
        return 30
    if month == 7:
        return 31
    if month == 8:
        return 31
    if month == 9:
        return 30
    if month == 10:
        return 31
    if month == 11:
        return 30
    if month == 12:
        return 31

def day_of_year(year, month, day):
    #Year code
    last_digits_year = str(year)
    last_digits_year = last_digits_year[-2] + last_digits_year[-1] #Take the last 2 digits from year
    last_digits_year = int(last_digits_year)    
    year_code = (last_digits_year + (last_digits_year // 4)) % 7
    print('Year code:')
    print(year_code)
    #Month Code
    year = int(year)
    if is_year_leap(year) == False:
        if month == 1:
            month_code = 0
        if month == 2:
            month_code = 3
        if month == 3:
            month_code = 3
        if month == 4:
            month_code = 6
        if month == 5:
            month_code = 1
        if month == 6:
            month_code = 4
        if month == 7:
            month_code = 6
        if month == 8:
            month_code = 2
        if month == 9:
            month_code = 5
        if month == 10:
            month_code = 0
        if month == 11:
            month_code = 3
        if month == 12:
            month_code = 5
    else:
        if month == 1:        
            month_code = 6
        if month == 2:
            month_code = 2
        if month == 3:
            month_code = 3
        if month == 4:
            month_code = 6
        if month == 5:
            month_code = 1
        if month == 6:
            month_code = 4
        if month == 7:
            month_code = 6
        if month == 8:
            month_code = 2
        if month == 9:
            month_code = 5
        if month == 10:
            month_code = 0
        if month == 11:
            month_code = 3
        if month == 12:
            month_code = 5
    
    print('Month code:')
    print(month_code)
    #Century Code
    year = int(year)
    if year >= 1700 and year < 1800:
        century_code = 4
    elif year >= 1800 and year < 1900:
        century_code = 2
    elif year >= 1900 and year < 2000:
        century_code = 0
    elif year >= 2000 and year < 2100:
        century_code = 6
    elif year >= 2100 and year < 2200:
        century_code = 4
    elif year >= 2200 and year < 2300:
        century_code = 2

    print('Century code:')
    print(century_code)
    #Leap Year Code
    if is_year_leap(year) == True:
        if month == 1:
            leap_year_code = 1
        elif  month == 2:
            leap_year_code = 1
        else:
            leap_year_code = 0
    else:
        leap_year_code = 0
        
    print('Leap Year code:')
    print(leap_year_code)
    #Calculating the Day
    calculating_day = (year_code + month_code + century_code + day - leap_year_code) % 7
    print(calculating_day)
    if calculating_day == 0:
        return "Sunday"
    if calculating_day == 1:
        return "Monday"
    if calculating_day == 2:
        return "Tuesday"
    if calculating_day == 3:
        return "Wednesday"
    if calculating_day == 4:
        return "Thursday"
    if calculating_day == 5:
        return "Friday"
    if calculating_day == 6:
        return "Saturday"
    
input_year = int(input("Write a year: "))
input_month = int(input("Write a month: "))
input_day = int(input("Write a day: "))

print(day_of_year(input_year, input_month, input_day))
