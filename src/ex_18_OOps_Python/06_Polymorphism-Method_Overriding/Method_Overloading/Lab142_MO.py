# -------------------------------------------------------------
# Step 1: Create MathClass with add() Method
# -------------------------------------------------------------
# Note: Python DOES NOT support method overloading by redefining
# the same method name. The last defined method always overrides
# the previous one.
class MathClass:
    def add(self, a, b):
        return a + b

    # This second definition REPLACES the first one
    def add(self, a, b):
        return a + b


# -------------------------------------------------------------
# Step 2: Create Object & Call add() with int and float
# -------------------------------------------------------------
obj_ref = MathClass()

result1 = obj_ref.add(3, 4)
print(result1)      # Output: 7

result2 = obj_ref.add(3.14, 4.14)
print(result2)      # Output: 7.28


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - Python does NOT support traditional method overloading.
# - When two methods share the same name, the LAST one overrides the earlier.
# - add() works for int and float because Python is dynamically typed.


