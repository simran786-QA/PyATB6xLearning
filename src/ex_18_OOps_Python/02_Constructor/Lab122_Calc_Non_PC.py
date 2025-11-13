# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class Example – Calculator with Methods
# -------------------------------------------------------------

# Step 1: Define the Class
class Calc:
    # Class-level variables (not used directly here)
    a = None
    b = None

    # ---------------------------------------------------------
    # Default Constructor
    def __init__(self):
        print("DC")  # DC → Default Constructor runs when object is created

    # ---------------------------------------------------------
    # Arithmetic Methods
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

# -------------------------------------------------------------
# Step 2: Take User Input
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))

# -------------------------------------------------------------
# Step 3: Create Object of Calc Class
object_ref = Calc()  # Constructor executes automatically → prints "DC"

# -------------------------------------------------------------
# Step 4: Call Class Methods Using the Object
output_sum = object_ref.sum(a, b)
output_sub = object_ref.sub(a, b)
output_mul = object_ref.mul(a, b)
output_div = object_ref.div(a, b)

# -------------------------------------------------------------
# Step 5: Display Results
print("Sum:", output_sum)
print("Sub:", output_sub)
print("Mul:", output_mul)
print("Div:", output_div)
# -------------------------------------------------------------
