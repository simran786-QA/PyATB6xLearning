# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Error Handling – ZeroDivisionError
# -------------------------------------------------------------

# Step 1: Perform a division with zero in denominator
# -------------------------------------------------------------
# This operation is mathematically invalid:
# 10 / 0  → ❌ Cannot divide by zero
print(10 / 0)   # ZeroDivisionError: division by zero


# -------------------------------------------------------------
# Hindi Explanation:
# - Jab hum kisi bhi number ko 0 se divide karte hain,
#   Python usse execute nahi kar sakta.
# - Isliye Python error deta hai:
#   ZeroDivisionError: division by zero
#
# English Explanation:
# - Dividing a number by zero is mathematically undefined.
# - Python cannot execute this operation, so it throws:
#   ZeroDivisionError: division by zero
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. 0 se divide karna allowed nahi hai → error.
# 2. Python isko ZeroDivisionError ke form me show karta hai.
# 3. Avoid by checking denominator before division.
# -------------------------------------------------------------
