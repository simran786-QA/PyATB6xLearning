# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Instance Method vs Static Method
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create Class with Both Methods
# - Instance Method → needs object & uses self
# - Static Method → belongs to class, no self needed
# -------------------------------------------------------------

class MathOperation:

    # Instance Method (needs object)
    def div(self, a, b):
        return a / b

    # Static Method (does NOT need object)
    @staticmethod
    def sum(a, b):
        return a + b


# -------------------------------------------------------------
# Step 2: Use Instance Method
# Must create an object because div() uses self
# -------------------------------------------------------------
t = MathOperation()
print(t.div(10, 10))     # Output → 1.0

# -------------------------------------------------------------
# Step 3: Use Static Method
# No object required — call directly with class name
# -------------------------------------------------------------
print(MathOperation.sum(10, 10))   # Output → 20

# -------------------------------------------------------------
# Hindi Explanation:
# - div() ek instance method hai, isliye object banana zaroori hai.
# - sum() ek static method hai, isme self nahi hota.
#   Isko class name se hi directly call kar sakte ho.
#
# English Explanation:
# - div() is an instance method, so an object is required.
# - sum() is a static method, so no object is needed.
#   You can call it directly using the class name.
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 4: Summary
# 1. Instance method → requires object (self)
# 2. Static method → no object needed
# 3. Use static methods for utilities/helper logic
# -------------------------------------------------------------
