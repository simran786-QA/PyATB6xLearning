# -------------------------------------------------------------
# 🧠 Lab058_Division_Operators.py
# Author: Simran Shaikh
# Topic: Difference between '/' and '//' in Python
# -------------------------------------------------------------

# 🎯 Objective:
# To understand the difference between normal division (/) and floor division (//).

# '/'  -> True Division Operator → Always returns a float value.
# '//' -> Floor Division Operator → Returns the quotient as an integer (floored result).

# -------------------------------------------------------------

print(5 / 2)   # True Division: gives float result → 2.5
print(5 // 2)  # Floor Division: gives integer quotient → 2

# -------------------------------------------------------------
# Let's test with negative numbers to see the difference clearly
print(-5 / 2)   # Normal Division → -2.5
print(-5 // 2)  # Floor Division → -3 (floored down to nearest integer)

# -------------------------------------------------------------
# You can also store and format results
num1 = 7
num2 = 3

true_div = num1 / num2
floor_div = num1 // num2

print(f"\nTrue Division of {num1}/{num2} = {true_div}")
print(f"Floor Division of {num1}//{num2} = {floor_div}")
