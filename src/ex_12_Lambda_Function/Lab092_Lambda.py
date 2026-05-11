```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Multiplication Example
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define a normal function
# -------------------------------------------------------------
# This function multiplies two numbers.

def mul(a, b):
    return a * b


# -------------------------------------------------------------
# Step 2: Define lambda function
# -------------------------------------------------------------
# Lambda function performs multiplication in one line.

mul_l = lambda a, b: a * b


# -------------------------------------------------------------
# Step 3: Call lambda function
# -------------------------------------------------------------
# Passing values 3 and 4 to the lambda function.

print(mul_l(3, 4))


# -------------------------------------------------------------
# Hindi Explanation:
# - mul() ek normal function hai jo do numbers ko multiply karta hai.
# - Lambda function bhi same multiplication operation karta hai.
# - mul_l(3, 4) ka output 12 hoga.
# - Lambda function short aur simple syntax provide karta hai.
#
# English Explanation:
# - mul() is a regular function that multiplies two numbers.
# - The lambda function performs the same operation in one line.
# - mul_l(3, 4) returns 12.
# - Lambda functions provide short and concise syntax.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lambda functions can take multiple arguments.
# 2. Useful for short mathematical operations.
# 3. lambda creates anonymous one-line functions.
# 4. Both normal and lambda functions can achieve the same result.
# -------------------------------------------------------------
