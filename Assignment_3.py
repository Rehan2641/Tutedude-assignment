# Task 1: Calculate Factorial Using a Function 

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
user = int(input("Enter a number: "))
print(f"Factorial of {user} is: {factorial(user)}")


# Task 2: Using the Math Module for Calculations

import math

num = int(input("Enter a number: "))
print(f"Sqaure root: {math.sqrt(num)}")
print(f"Logarithm: {math.log(num)} ")
print(f"Sine: {math.sin(num)}")


