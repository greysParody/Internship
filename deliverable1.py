#Hameeda Task1
def primenum(number):
    if number <= 1:
        return False  # anything less than 1 is not a prime  number

    # Check for factors from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, not prime

    return True  # No factors found other than 1 and itself, prime number


# Taking input from user
num = int(input("Enter a number: "))

if primenum(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
