# -------------------------------------------------------------
# Concept: Hybrid Inheritance in Python
# -------------------------------------------------------------
# Hybrid inheritance is a combination of multiple inheritance +
# multilevel inheritance.
#
# Structure:
#         Base
#       /      \
#      A        B      (Multiple Inheritance)
#       \      /
#          C           (Hybrid Inheritance)


# -------------------------------------------------------------
# Step 1: Base Class
# -------------------------------------------------------------
class Base:
    def base_method(self):
        print("Base method")


# -------------------------------------------------------------
# Step 2: Level-1 Child Classes (A and B inherit from Base)
# -------------------------------------------------------------
class A(Base):
    def a_method(self):
        print("A method")


class B(Base):
    def b_method(self):
        print("B method")


# -------------------------------------------------------------
# Step 3: Hybrid Child Class (C inherits from A & B)
# -------------------------------------------------------------
class C(A, B):
    def c_method(self):
        print("C method")


# -------------------------------------------------------------
# Step 4: Create Object & Call Methods
# -------------------------------------------------------------
obj = C()
obj.base_method()   # From Base
obj.a_method()      # From A
obj.b_method()      # From B
obj.c_method()      # From C


# -------------------------------------------------------------
# Output
# -------------------------------------------------------------
# Base method
# A method
# B method
# C method


# -------------------------------------------------------------
# Summary
# -------------------------------------------------------------
# - Demonstrates hybrid inheritance (mix of multiple + multilevel).
# - Class C inherits:
#     ✔ base_method() from Base → through A/B
#     ✔ a_method() from A
#     ✔ b_method() from B
#     ✔ c_method() from itself
# - Shows Python’s Method Resolution Order (MRO).


# -------------------------------------------------------------
# Commit Message
# -------------------------------------------------------------
# feat: added hybrid inheritance example using Base → A/B → C
# - Demonstrated mix of multilevel + multiple inheritance
# - Verified method access across hierarchy

