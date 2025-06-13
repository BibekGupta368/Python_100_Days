def is_prime(num):
    flag = 0
    for i in range(1, num+1):
        if num % i == 0:
            flag += 1
    if flag == 2:
        return True
    else:
        return False
num = int(input("Enter a number: "))
output = is_prime(num)
if output == True:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")