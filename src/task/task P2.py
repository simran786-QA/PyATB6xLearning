# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Calculator using Parameterized Constructor in Python
# -------------------------------------------------------------

class Calculator:
    # ---------------------------------------------------------
    # Step 1: Parameterized Constructor
    # ---------------------------------------------------------
    def __init__(self, a, b):
        # Hindi:
        # Yahaan par hum constructor me do parameters le rahe hain: a aur b
        # Jab object create karenge, tab ye values pass hongi.
        #
        # English:
        # The constructor accepts two numbers: a and b.
        # These are stored as instance variables when the object is created.
        self.a = a
        self.b = b
        print(f"Calculator created with values a = {a}, b = {b}")

    # ---------------------------------------------------------
    # Step 2: Methods for Arithmetic Operations
    # ---------------------------------------------------------

    def add(self):
        # No arguments, returns sum
        return self.a + self.b

    def subtract(self):
        # Returns subtraction
        return self.a - self.b

    def multiply(self):
        # Returns multiplication
        return self.a * self.b

    def divide(self):
        # Handles division safely (avoid division by zero)
        if self.b == 0:
            return "Division by zero not allowed"
        return self.a / self.b

    # ---------------------------------------------------------
    # Step 3: Display all Results (Print Function)
    # ---------------------------------------------------------
    def display_results(self):
        print("---- Calculator Results ----")
        print("Sum:", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication:", self.multiply())
        print("Division:", self.divide())
        print("-----------------------------")


# -------------------------------------------------------------
# Step 4: Create Object and Pass Values via Constructor
# -------------------------------------------------------------

# Hindi:
# Object create karte waqt hi values pass karenge (parameterized constructor).
# English:
# We pass numbers directly while creating the object.

calc1 = Calculator(10, 5)
calc1.display_results()

# Another Example
calc2 = Calculator(12, 3)
calc2.display_results()
