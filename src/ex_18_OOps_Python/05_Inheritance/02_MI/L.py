# -------------------------------------------------------------
# Concept: Method Resolution Order (MRO) in Multiple Inheritance
# -------------------------------------------------------------
# When two parent classes have the same method name,
# Python will call the method from the parent that appears FIRST
# in the inheritance list. (Left-to-Right MRO)


# -------------------------------------------------------------
# Step 1: Create Parent Classes
# -------------------------------------------------------------
class Father1:
    def money(self):
        print("F1 Money")


class Father2:
    def money(self):
        print("F2 Money")


# -------------------------------------------------------------
# Step 2: Create Child Class with Multiple Inheritance
# -------------------------------------------------------------
# class Child(Father1, Father2):  # Calls F1.money()
class Child(Father2, Father1):    # Calls F2.money()
    def give_money(self):
        print("Son")
        self.money()  # Resolved using MRO


# -------------------------------------------------------------
# Step 3: Create Object and Execute
# -------------------------------------------------------------
c = Child()
c.give_money()


# -------------------------------------------------------------
# Output
# -------------------------------------------------------------
# Son
# F2 Money


# -------------------------------------------------------------
# Summary
# -------------------------------------------------------------
# - Demonstrated multiple inheritance with same-name methods.
# - Python uses MRO (Method Resolution Order) to decide which
#   parent's method to call.
# - Since Child(Father2, Father1) → Father2.money() is executed.
# - Useful for understanding ambiguity resolution in inheritance.


# -------------------------------------------------------------
# Commit Message
# -------------------------------------------------------------
# feat: added example demonstrating MRO in multiple inheritance
# - Created Father1 and Father2 with same method name
# - Implemented Child class to show MRO effect
# - Added printed output to verify method resolution
