# -------------------------------------------------------------
# Lab059_Boolean_Logic.py
# Author: Simran Shaikh
# Topic: Boolean Logic – Understanding AND, OR, NOT
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how Python uses Boolean values (True/False) with logical operators.

# -------------------------------------------------------------
# ✅ 1. Basic Boolean values
f = False
t = True

# Logical OR (Returns True if *any* one condition is True)
print(f or t)   # True  (since t = True)

# Logical AND (Returns True only if *both* are True)
print(f and t)  # False (since f = False)

# Logical NOT (Reverses the value)
print(not f)    # True
print(not t)    # False

# -------------------------------------------------------------
# ✅ 2. Truth Table Reference

#   A      B     A and B     A or B
#  True   True     True        True
#  True   False    False       True
#  False  True     False       True
#  False  False    False       False

# -------------------------------------------------------------
# ✅ 3. Real-World Example
is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Welcome Admin 👑")
elif is_logged_in and not is_admin:
    print("Welcome User 👋")
else:
    print("Please log in first 🔒")

# -------------------------------------------------------------
# ✅ 4. Combining Conditions
age = 20
has_license = True

if age >= 18 and has_license:
    print("✅ You can drive.")
else:
    print("❌ You cannot drive.")
