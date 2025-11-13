# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Types of Variables in Python (Global, Instance, Local)
# -------------------------------------------------------------

# Step 1: Global Variable
a = 10  # Global variable - Accessible everywhere in the program

# -------------------------------------------------------------
# Step 2: Define Class
class Person:
    b = 11  # Instance (Class-level) variable - belongs to the class

    def print_info(self):
        c = 20  # Local variable - exists only inside this method

        # Print all variable values
        print("Local Variable c:", c)
        print("Instance Variable b:", self.b)
        print("Global Variable a:", a)

# -------------------------------------------------------------
# Step 3: Create Object of Class
object_ref = Person()

# Step 4: Call the Method
object_ref.print_info()

# -------------------------------------------------------------
# The below two lines are commented because:
# print(b) → Error: 'b' belongs to class scope, not global
# print(c) → Error: 'c' is local and not accessible outside method
# -------------------------------------------------------------
# print(b)
# print(c)
