# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Error Handling – TypeError (int + str)
# -------------------------------------------------------------

# Step 1: Perform an invalid operation
# -------------------------------------------------------------
# 1 + "1" → ❌ Cannot add integer and string together
# Python does not know how to combine different data types like this.

# Uncomment to see the error:
# print(1 + "1")

# TypeError:
# unsupported operand type(s) for +: 'int' and 'str'


# -------------------------------------------------------------
# Hindi Explanation:
# - Yahan hum ek integer (1) aur ek string ("1") ko add kar rahe hain.
# - Python ko samajh nahi aata ki number ko string ke sath kaise jode.
# - Isliye error deta hai: TypeError.

# English Explanation:
# - Here we are trying to add an integer (1) and a string ("1").
# - Python cannot combine these two incompatible data types.
# - Therefore it throws a TypeError.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. int + str directly add nahi ho sakta.
# 2. Python TypeError throw karta hai.
# 3. Solution:
#       print(1 + int("1"))
#       OR
#       print(str(1) + "1")
# -------------------------------------------------------------
