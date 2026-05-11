# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Addition of Three Numbers
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define a normal function
# -------------------------------------------------------------
# This function adds three numbers.

def sum_three_num(a, b, c):
    return a + b + c


# -------------------------------------------------------------
# Step 2: Define lambda function
# -------------------------------------------------------------
# Lambda function performs the same addition in one line.

op_f = lambda a, b, c: a + b + c


# -------------------------------------------------------------
# Step 3: Call lambda function
# -------------------------------------------------------------
# Passing values 3, 4, and 5 to the lambda function.

print(op_f(3, 4, 5))


# -------------------------------------------------------------
# Hindi Explanation:
# - sum_three_num() ek normal function hai jo teen numbers add karta hai.
# - Lambda function bhi same kaam short syntax me karta hai.
# - op_f(3, 4, 5) ka output 12 hoga.
# - Lambda functions concise aur quick operations ke liye useful hote hain.
#
# English Explanation:
# - sum_three_num() is a regular function that adds three numbers.
# - The lambda function performs the same operation in one line.
# - op_f(3, 4, 5) returns 12.
# - Lambda functions are useful for concise operations.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lambda functions can accept multiple parameters.
# 2. Useful for short mathematical expressions.
# 3. lambda creates anonymous one-line functions.
# 4. Both normal and lambda functions provide the same output.
# -------------------------------------------------------------