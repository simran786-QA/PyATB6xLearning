# -------------------------------------------------------------
# Lab058_Logical_Operators.py
# Author: Simran Shaikh
# Topic: Logical and Comparison Operators in Python
# -------------------------------------------------------------

# 🎯 Objective:
# To understand how logical and comparison operators work in Python.

# -------------------------------------------------------------
# ✅ 1. Boolean Value Example
# -------------------------------------------------------------

is_pramod_married = True

print(not is_pramod_married)  # Logical NOT -> reverses True to False
print(is_pramod_married)      # Original value remains True

# Output:
# False
# True

# -------------------------------------------------------------
# ✅ 2. Comparison Operators
# -------------------------------------------------------------
# > , < , >= , <= , == , !=

x = 10
y = 20

print(x > y)   # False (10 is NOT greater than 20)
print(x < y)   # True  (10 is less than 20)

print(" --- ")

a = 10
b = 10
print(a == b)  # True (both equal)
print(a >= b)  # True (10 is equal to 10)

# -------------------------------------------------------------
# ✅ 3. Logical Operators with Comparison
# -------------------------------------------------------------
# and → True if both conditions are True
# or  → True if any one condition is True
# not → Negates the condition

age = 25
has_id = True

# Example: Checking voting eligibility
if age >= 18 and has_id:
    print("You are allowed to vote 🗳️")
else:
    print("You cannot vote ❌")

# Another Example
salary = 60000
experience = 3
if salary > 50000 or experience >= 5:
    print("Eligible for senior role 💼")
else:
    print("Not eligible yet 🚧")
