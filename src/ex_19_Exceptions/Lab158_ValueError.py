# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Error Handling – ValueError (invalid int conversion)
# -------------------------------------------------------------

# Step 1: Perform an invalid type conversion
# -------------------------------------------------------------
# int("a") → ❌ Cannot convert a non-numeric string into an integer.
# Python expects digits only (0–9) when converting to int.

# Uncomment to see the error:
# print(int("a"))

# Expected Error:
# ValueError: invalid literal for int() with base 10: 'a'


# -------------------------------------------------------------
# Hindi Explanation:
# - "a" ek alphabet hai, number nahi.
# - int() sirf numeric strings ko integer me convert kar sakta hai.
# - Jab hum int("a") karte hain, Python confuse hota hai aur ValueError deta hai.

# English Explanation:
# - "a" is an alphabet, not a numeric value.
# - int() can only convert strings that contain valid numbers.
# - Therefore int("a") throws a ValueError.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. int() only works with numeric strings → "10", "25", "3".
# 2. int("a") fails because "a" is not a number.
# 3. Python throws ValueError when conversion is impossible.
# 4. Correct usage example:
#       print(int("123"))   # Works
#       # print(int("abc")) → ValueError
# -------------------------------------------------------------
