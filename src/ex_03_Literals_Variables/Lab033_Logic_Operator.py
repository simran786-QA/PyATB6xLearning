# -------------------------------------------------------------
# 🧠 Lab056_Logical_Operators.py
# Author: Simran Shaikh
# Topic: Logical Operators in Python (तार्किक ऑपरेटर्स)
# -------------------------------------------------------------

# 🎯 Objective:
# Understand the use of logical operators: and, or, not
# These operators are used to combine or modify multiple conditions.

# -------------------------------------------------------------
# Step 1: Assign values
a, b = 5, 10

print(f"Given values: a = {a}, b = {b}\n")

# -------------------------------------------------------------
# Step 2: Logical Operations
print("📘 Logical Operations Results (तार्किक ऑपरेशन के परिणाम):\n")

# AND Operator → True if both conditions are True
print(f"1️⃣ (a > 0 and b > 0) → {a > 0 and b > 0}")
# ✅ True because both a and b are positive

# OR Operator → True if any one condition is True
print(f"2️⃣ (a > 0 or b < 0)  → {a > 0 or b < 0}")
# ✅ True because a > 0 is True (even though b < 0 is False)

# NOT Operator → Reverses the result (True → False, False → True)
print(f"3️⃣ not (a > 0)       → {not (a > 0)}")
# ❌ False because a > 0 is True, and NOT changes it to False

print("\n✅ Program executed successfully by Simran Shaikh.")
