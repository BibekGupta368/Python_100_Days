

def is_leap_year(year):
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
year = int(input("Enter the year: "))
output = is_leap_year(year)
print(output)
if output == True:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
