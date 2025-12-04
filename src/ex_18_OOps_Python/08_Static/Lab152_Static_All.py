# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Static Methods
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create Class with Static Method
# A static method belongs to the class, not the object.
# It does NOT use 'self' or 'cls'.
# -------------------------------------------------------------

class O:

    # Static Method (No self, No cls)
    @staticmethod
    def sum(a, b):
        return a + b


# -------------------------------------------------------------
# Step 2: Call Static Method
# Note: No need to create an object; call using class name
# -------------------------------------------------------------

result = O.sum(4, 5)
print(result)   # Output: 9

# -------------------------------------------------------------
# Hindi Explanation:
# Static method class ka hota hai, object ka nahi.
# Isme 'self' nahi hota, isliye object banane ki zarurat nahi hoti.
# Direct O.sum(a, b) se call kar sakte ho.
#
# English Explanation:
# A static method belongs to the class itself.
# It does not require an object because it does not use 'self'.
# You can call it directly using ClassName.method().
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 3: Summary
# 1. @staticmethod is used to declare static methods.
# 2. No object required to call static functions.
# 3. Useful for utility/helper functions.
# -------------------------------------------------------------
