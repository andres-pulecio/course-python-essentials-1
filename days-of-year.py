from turtle import st


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
    
    #
    
    print(year_code)

print(day_of_year(1897, 12, 31))
