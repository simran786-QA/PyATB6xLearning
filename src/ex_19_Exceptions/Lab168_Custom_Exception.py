# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Custom Exception Handling – User Defined Exception
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create a custom exception class
# -------------------------------------------------------------
# This custom exception will be used for invalid age scenarios.

class InvalidAgeException(Exception):
    pass


# -------------------------------------------------------------
# Step 2: Function to check zero division
# -------------------------------------------------------------
# If the value of a is 0, we manually raise ZeroDivisionError.

def check_zero_div(a):
    if a == 0:
        raise ZeroDivisionError("Can't divide with zero")


# -------------------------------------------------------------
# Step 3: Function to validate drinking age
# -------------------------------------------------------------
# If age is less than 18, raise custom InvalidAgeException.

def can_you_drink(age):
    if age < 18:
        raise InvalidAgeException("Invalid age of drinking")


# -------------------------------------------------------------
# Step 4: Function calls
# -------------------------------------------------------------
# This call will raise InvalidAgeException.
can_you_drink(17)

# This call will execute successfully (no exception).
can_you_drink(25)


# -------------------------------------------------------------
# Hindi Explanation:
# - InvalidAgeException ek custom exception class hai.
# - check_zero_div function mein agar value 0 hui,
#   to ZeroDivisionError manually raise hota hai.
# - can_you_drink function age check karta hai.
# - Agar age 18 se kam hui, to InvalidAgeException throw hoti hai.
# - 17 ke case mein exception aayega, 25 ke case mein nahi.
#
# English Explanation:
# - InvalidAgeException is a user-defined exception.
# - check_zero_div raises ZeroDivisionError when input is zero.
# - can_you_drink validates the age for drinking.
# - If age < 18, a custom exception is raised.
# - Age 17 raises an error, age 25 passes successfully.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Custom exceptions are created by inheriting Exception class.
# 2. raise keyword is used to throw exceptions manually.
# 3. Multiple validations can use different exception types.
# 4. Custom exceptions improve clarity and control in programs.
# -------------------------------------------------------------
