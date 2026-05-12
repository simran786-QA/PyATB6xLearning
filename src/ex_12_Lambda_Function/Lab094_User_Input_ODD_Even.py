```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Lambda Function – Even or Odd Checker
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Normal function example (commented)
# -------------------------------------------------------------
# This normal function checks whether a number is even or odd.

# def find_even_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# -------------------------------------------------------------
# Step 2: Take input from the user
# -------------------------------------------------------------
# User enters a number for checking.

user_input = int(input("Enter the number"))


# -------------------------------------------------------------
# Step 3: Define lambda function
# -------------------------------------------------------------
# Lambda function uses conditional expression
# to check even or odd.

check_even_odd_f = lambda num: "Even" if num % 2 == 0 else "Odd"


# -------------------------------------------------------------
# Step 4: Call lambda function
# -------------------------------------------------------------
# Result is stored and printed.

result = check_even_odd_f(user_input)
print(result)


# -------------------------------------------------------------
# Hindi Explanation:
# - User se ek number input liya gaya hai.
# - Lambda function check karta hai ki number 2 se divide ho raha hai ya nahi.
# - Agar remainder 0 aata hai, to number Even hota hai.
# - Otherwise number Odd hota hai.
# - Conditional expression lambda ke andar use ki gayi hai.
#
# English Explanation:
# - A number is taken as input from the user.
# - The lambda function checks divisibility by 2.
# - If remainder is 0, the number is Even.
# - Otherwise, the number is Odd.
# - A conditional expression is used inside the lambda function.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Lambda functions can use conditional expressions.
# 2. num % 2 == 0 checks for even numbers.
# 3. Lambda provides concise one-line logic.
# 4. Useful for simple decision-making operations.
# -------------------------------------------------------------
```
