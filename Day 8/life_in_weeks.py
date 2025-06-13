def life_in_weeks(age):
    age_until_XC = 90 - age
    age_in_weeks = age_until_XC * 52
    print(f"You have {age_in_weeks} weeks left.")
age = int(input("What is your age?"))
life_in_weeks(age)