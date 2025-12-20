# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – ZeroDivisionError
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Take input from the user
# -------------------------------------------------------------
# We are taking two numbers from the user.

a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))


# -------------------------------------------------------------
# Step 2: Perform division inside try block
# -------------------------------------------------------------
# If b is 0, Python will raise ZeroDivisionError.

try:
    c = a / b
    print("Result:", c)


# -------------------------------------------------------------
# Step 3: Handle ZeroDivisionError using except
# -------------------------------------------------------------
except ZeroDivisionError:
    print("Error: Division by zero is not allowed (b must not be 0)")


# -------------------------------------------------------------
# Hindi Explanation:
# - User se do numbers liye ja rahe hain.
# - Division operation try block ke andar hai.
# - Agar b = 0 hua, to Python ZeroDivisionError throw karega.
# - except block error ko handle karta hai aur program crash nahi hota.

# English Explanation:
# - Two numbers are taken from the user.
# - Division is performed inside the try block.
# - If the denominator is zero, Python raises ZeroDivisionError.
# - The except block catches the error and prints a user-friendly message.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. try block is used to write risky code.
# 2. except block handles runtime errors.
# 3. ZeroDivisionError occurs when dividing by zero.
# 4. Exception handling prevents program crash.
# -------------------------------------------------------------
