```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Square of a Number using math.pow()
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Import math module
# -------------------------------------------------------------
# math module provides mathematical functions like pow().

import math


# -------------------------------------------------------------
# Step 2: Normal function example (commented)
# -------------------------------------------------------------
# This function returns the square of a number.

# def give_me_power(num):
#     return math.pow(num, 2)
#
# op = give_me_power(10)
# print(op)


# -------------------------------------------------------------
# Step 3: Lambda function with user input (commented)
# -------------------------------------------------------------
# Lambda function can also calculate square.

# num = int(input("Enter the number"))
# op2 = lambda num: math.pow(num, 2)
# print(op2(num))


# -------------------------------------------------------------
# Step 4: Lambda function with direct input
# -------------------------------------------------------------
# User input is taken directly inside lambda function.

op2 = lambda: math.pow(int(input("Enter the number")), 2)


# -------------------------------------------------------------
# Step 5: Call lambda function
# -------------------------------------------------------------
# Lambda function executes and prints square value.

print(op2())


# -------------------------------------------------------------
# Hindi Explanation:
# - math.pow() function number ka power calculate karta hai.
# - Yahan power 2 diya gaya hai, isliye square calculate hoga.
# - Lambda function ke andar direct user input liya gaya hai.
# - int() input ko integer me convert karta hai.
# - Example: input 5 dene par output 25.0 aayega.
#
# English Explanation:
# - math.pow() calculates the power of a number.
# - Power 2 means square of the number.
# - User input is taken directly inside the lambda function.
# - int() converts input into integer type.
# - Example: input 5 gives output 25.0.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. math.pow() performs power calculations.
# 2. Lambda functions can directly take user input.
# 3. Square means power of 2.
# 4. Lambda is useful for short mathematical operations.
# -------------------------------------------------------------
```
