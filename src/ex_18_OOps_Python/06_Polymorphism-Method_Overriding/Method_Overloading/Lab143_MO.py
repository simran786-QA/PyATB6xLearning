# -------------------------------------------------------------
# Step 1: Define a Class with Method Overriding (Python Style)
# -------------------------------------------------------------
# Python does NOT support traditional method overloading.
# The second method definition replaces the first one.
# Using default parameters helps simulate overloading behavior.

class MathClass:

    # First version (will be overridden)
    def add(self, a, b):
        return a + b

    # Second version (Python keeps ONLY this one)
    def add(self, a, b, c=10):
        return a + b + c


# -------------------------------------------------------------
# Step 2: Create Object and Call Methods
# -------------------------------------------------------------
obj_ref = MathClass()

result1 = obj_ref.add(3, 4, 5)      # Uses a + b + c → 12
result2 = obj_ref.add(3.14, 4.14)   # Uses default c=10 → 17.28

print(result1)
print(result2)


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - Python does NOT support true method overloading.
# - The last add() definition overrides the first automatically.
# - Using a default parameter (c=10) gives flexibility:
#       • add(a, b, c)  → three values
#       • add(a, b)     → uses default c = 10
# - This is Python’s recommended way to mimic method overloading.
