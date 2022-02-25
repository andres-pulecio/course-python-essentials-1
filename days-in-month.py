# Scenario
# Your task is to write and test a function which takes two arguments (a year and a month) 
# and returns the number of days for the given month/year pair (while only February is sensitive to 
# the year value, your function should be universal).
# The initial part of the function is ready. Now, convince the function to return None if its arguments 
# don't make sense.
# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6). 
# It may be very helpful. We encourage you to use a list filled with the months' lengths. 
# You can create it inside the function - this trick will significantly shorten the code.

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

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
