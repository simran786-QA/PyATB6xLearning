# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – Multiple Exceptions in One Block
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
# Division ek risky operation hai (zero ya wrong input ho sakta hai).

    c = a / b
    print("Result:", c)

# -------------------------------------------------------------
# Step 3: Handle multiple exceptions
# -------------------------------------------------------------
# Multiple errors ko ek hi except block me handle kiya gaya hai.

except (TypeError, NameError, ValueError, ZeroDivisionError):
    print("Error: Type, Name, Value ya Zero Division issue aaya hai")
