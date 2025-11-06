# -------------------------------------------------------------
# 🧠 Lab057_Exponentiation_Operator.py
# Author: Simran Shaikh
# Topic: Exponentiation Operator in Python (**)
# -------------------------------------------------------------

# 🎯 Objective:
# To understand how the exponent (power) operator ** works in Python.
# Syntax: base ** exponent

# Example: 2 ** 3 means 2 raised to the power of 3 → 8

# -------------------------------------------------------------

print(2 ** 2)  # 2 raised to the power of 2 = 4
print(2 ** 3)  # 2 raised to the power of 3 = 8
print(2 ** 4)  # 2 raised to the power of 4 = 16

# -------------------------------------------------------------
# You can use it with variables as well
base = 5
exponent = 3
result = base ** exponent

print(f"\n{base} raised to the power of {exponent} is {result}")  # 5 ** 3 = 125

# -------------------------------------------------------------
# Real-world Example:
# Suppose you want to calculate compound growth or area (like area of square = side ** 2)
side = 4
area_square = side ** 2
print(f"The area of a square with side {side} is {area_square}")  # 4 ** 2 = 16
