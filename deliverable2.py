def trialFunc():
    for num in range(1, 101): #to iterate from 1 to 100
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)

# Calling the function to execute
trialFunc()
