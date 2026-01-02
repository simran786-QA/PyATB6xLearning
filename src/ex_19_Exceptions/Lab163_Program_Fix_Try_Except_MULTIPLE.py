# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – Multiple Except Blocks
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Take input from the user
# -------------------------------------------------------------
# User se do numbers input liye ja rahe hain.

try:
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))

# -------------------------------------------------------------
# Step 2: Perform division
# -------------------------------------------------------------
# Division ek risky operation hai.

    c = a / b
    print("Result:", c)

# -------------------------------------------------------------
# Step 3: Handle exceptions using separate except blocks
# -------------------------------------------------------------
# Har error ke liye alag-alag except block use kiya gaya hai.

except ValueError:
    print("Error: Invalid input (number expected)")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
