# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – Multiple Exceptions & finally
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Take user input and perform risky operation
# -------------------------------------------------------------
# We are taking two numbers and performing division.
# This code can raise ValueError or ZeroDivisionError.

try:
    a = int(input("Enter num 1: "))
    b = int(input("Enter num 2: "))
    c = a / b
    print("Result:", c)


# -------------------------------------------------------------
# Step 2: Handle ValueError
# -------------------------------------------------------------
# This block runs when input is not a valid integer.

except ValueError:
    print("Value Error: Please enter only numbers")


# -------------------------------------------------------------
# Step 3: Handle ZeroDivisionError
# -------------------------------------------------------------
# This block runs when user enters 0 as divisor.

except ZeroDivisionError:
    print("Division Error: Cannot divide by zero")


# -------------------------------------------------------------
# Step 4: finally block
# -------------------------------------------------------------
# This block ALWAYS executes (error aaye ya na aaye).

finally:
    print("I will always execute!")


# -------------------------------------------------------------
# Hindi Explanation:
# - try block me risky code likhte hain.
# - Agar input galat hua (string), ValueError aayega.
# - Agar b = 0 hua, ZeroDivisionError aayega.
# - finally block hamesha execute hota hai.
#
# English Explanation:
# - The try block contains code that may cause errors.
# - ValueError occurs for invalid numeric input.
# - ZeroDivisionError occurs when dividing by zero.
# - finally block runs no matter what.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Multiple except blocks handle different errors.
# 2. ValueError → wrong input type.
# 3. ZeroDivisionError → divide by zero.
# 4. finally block always executes.
# 5. Exception handling makes the program safe and stable.
# -------------------------------------------------------------
