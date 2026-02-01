```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – try, except, else, finally
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Take input and perform division inside try block
# -------------------------------------------------------------
# Input conversion and division are risky operations,
# so they are placed inside the try block.

try:
    a = int(input("Enter num 1"))
    b = int(input("Enter num 2"))
    c = a / b


# -------------------------------------------------------------
# Step 2: Handle ValueError
# -------------------------------------------------------------
# This block runs when input cannot be converted to int.

except ValueError:
    print("Value Error")


# -------------------------------------------------------------
# Step 3: Handle ZeroDivisionError
# -------------------------------------------------------------
# This block runs when division by zero occurs.

except ZeroDivisionError:
    print("Div Error")


# -------------------------------------------------------------
# Step 4: else block
# -------------------------------------------------------------
# Runs only if the try block executes successfully
# (no exception raised).

else:
    print(c)


# -------------------------------------------------------------
# Step 5: finally block
# -------------------------------------------------------------
# This block always executes, whether an exception
# occurs or not.

finally:
    print("I will always execute!")


# -------------------------------------------------------------
# Hindi Explanation:
# - try block ke andar input lena aur division kiya gaya hai.
# - Agar input galat type ka ho (string, etc.), ValueError aayega.
# - Agar b = 0 hua, to ZeroDivisionError aayega.
# - else tabhi chalega jab koi error nahi aata.
# - finally har condition mein execute hota hai.
#
# English Explanation:
# - Inputs and division are written inside the try block.
# - ValueError is caught if input conversion fails.
# - ZeroDivisionError is caught if division by zero happens.
# - The else block runs only when no exception occurs.
# - The finally block always runs.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. try block contains risky code.
# 2. Multiple except blocks handle different exceptions.
# 3. else runs only when try succeeds.
# 4. finally always executes, error ho ya na ho.
# -------------------------------------------------------------
```
