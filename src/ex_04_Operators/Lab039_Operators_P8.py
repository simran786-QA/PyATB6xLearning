# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Comparison Operator – Not Equal (!=)
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how the '!=' (Not Equal To) comparison operator works in Python.
# It checks whether two values are different.

# -------------------------------------------------------------
# ✅ 1. Example
x = 10
y = 30

# The '!=' operator returns True if the two values are NOT equal.
result = (x != y)

# -------------------------------------------------------------
# ✅ 2. Output
print(result)  # True, because 10 is not equal to 20

# -------------------------------------------------------------
# ✅ 3. Explanation
# x != y → True if x and y have different values
# x == y → True if x and y have the same value

# -------------------------------------------------------------
# ✅ 4. Real-World Example
# Suppose we check if two passwords are different.

saved_password = "Python@123"
entered_password = "python@123"

if saved_password != entered_password:
    print("❌ Passwords do not match! Try again.")
else:
    print("✅ Login Successful!")
