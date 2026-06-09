                                                     #ASSIGNMENT 2:
                                        #Module 3: Control Structures in Python


# Task 1: Check if a Number is Even or Odd

# 1.Takes an integer input from the user.
num = int(input("Enter a number: "))

# 2. Checks whether the number is even or odd using an if-else statement.
if num % 2==0:
    print(f"{num} is an Even number")
    
else:
    print(f"{num} is an Odd number")
    

# Task 2: Sum of Integers from 1 to 50 Using a Loop

# 1. Uses a for loop to iterate over numbers from 1 to 50.
for a in range(1,51):
    print(a)

#2. Calculates the sum of all integers in this range.
sum = 0
for z in range(1,51):
    sum = sum + z
    
#3.  Displays the final sum.
print(f"The sum of number from 1 to 50 is: {sum}")
