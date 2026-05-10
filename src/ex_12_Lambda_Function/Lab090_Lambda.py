```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Anonymous Functions in Python
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define a normal function
# -------------------------------------------------------------
# This function multiplies the given number by 3.

def triple_number(num):
    return num * 3


# -------------------------------------------------------------
# Step 2: Call the normal function
# -------------------------------------------------------------
# Function is called with value 3.

result = triple_number(3)
print(result)


# -------------------------------------------------------------
# Step 3: Lambda Function
# -------------------------------------------------------------
# Lambda is a short anonymous function used for simple operations.

result_l_f = lambda num: num * 3


# -------------------------------------------------------------
# Step 4: Call lambda function
# -------------------------------------------------------------
# Lambda function is directly executed with value 3.

print(result_l_f(3))


# -------------------------------------------------------------
# Hindi Explanation:
# - triple_number() ek normal function hai jo number ko 3 se multiply karta hai.
# - result variable me function ka output store hota hai.
# - lambda ek anonymous function hota hai jiska naam nahi hota.
# - Lambda function short syntax me simple operations ke liye use hota hai.
# - Dono functions same output dete hain.
#
# English Explanation:
# - triple_number() is a regular function that multiplies a number by 3.
# - The result is stored in a variable and printed.
# - Lambda is an anonymous function without a name.
# - It is used for short and simple operations.
# - Both functions produce the same output.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Normal functions use def keyword.
# 2. Lambda functions are short anonymous functions.
# 3. Lambda is useful for one-line operations.
# 4. Both approaches can achieve the same result.
# -------------------------------------------------------------
```
