from pickle import TRUE


def is_year_leap(year):
# Si el año es uniformemente divisible por 4, vaya al paso 2. De lo contrario, vaya al paso 5.
# Si el año es uniformemente divisible por 100, vaya al paso 3. De lo contrario, vaya al paso 4.
# Si el año es uniformemente divisible por 400, vaya al paso 4. De lo contrario, vaya al paso 5.
# El año es un año bisiesto (tiene 366 días).
# El año no es un año bisiesto (tiene 365 días).
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

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
 