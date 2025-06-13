def is_leap_year(year):
    # Write your code here. 
    # Don't change the function 
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
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
