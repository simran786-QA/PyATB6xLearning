# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Simple Addition Example
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define a normal function
# -------------------------------------------------------------
# This function adds 10 to the given number.

def add(n):
    return n + 10


# -------------------------------------------------------------
# Step 2: Define lambda function
# -------------------------------------------------------------
# Lambda function performs the same addition operation.

l_add = lambda n: n + 10


# -------------------------------------------------------------
# Step 3: Call lambda function
# -------------------------------------------------------------
# Passing value 30 to the lambda function.

print(l_add(30))


# -------------------------------------------------------------
# Hindi Explanation:
# - add() ek normal function hai jo number me 10 add karta hai.
# - lambda function bhi same kaam short syntax me karta hai.
# - l_add(30) ka output 40 hoga.
# - Lambda simple aur one-line operations ke liye useful hota hai.
#
# English Explanation:
# - add() is a regular function that adds 10 to a number.
# - The lambda function performs the same task in short syntax.
# - l_add(30) returns 40.
# - Lambda functions are useful for simple one-line operations.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lambda functions are compact alternatives to normal functions.
# 2. They are useful for simple calculations.
# 3. lambda keyword creates anonymous functions.
# 4. Both normal and lambda functions can give the same result.
# -------------------------------------------------------------