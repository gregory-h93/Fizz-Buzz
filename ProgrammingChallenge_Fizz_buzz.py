# Write a program that iterates over the integers 1 through 50 using a loop.
num_range = range(1, 51)
for num in num_range:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and num % 5 != 0:
        print("Fizz")
    elif num % 3 != 0 and num % 5 == 0:
        print("Buzz")
    else:
        print(num)