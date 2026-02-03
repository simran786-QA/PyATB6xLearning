# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – ExceptionGroup (Python 3.11)
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create an ExceptionGroup
# -------------------------------------------------------------
# ExceptionGroup allows grouping multiple exceptions together.
# This feature is available from Python 3.11 onwards.

eg = ExceptionGroup(
    "Multiple Ex",
    [
        ValueError("Invalid Value"),
        TypeError("Type Error "),
        ZeroDivisionError("Can't div Xero")
    ]
)


# -------------------------------------------------------------
# Step 2: Define a function to check division condition
# -------------------------------------------------------------
# If the value of 'a' is 0, we raise the ExceptionGroup.

def check_div(a):
    if a == 0:
        raise eg


# -------------------------------------------------------------
# Hindi Explanation:
# - ExceptionGroup Python 3.11 ka feature hai.
# - Isme hum multiple exceptions ko ek group me rakh sakte hain.
# - Yahan ValueError, TypeError aur ZeroDivisionError
#   ek hi ExceptionGroup me add kiye gaye hain.
# - check_div function me agar a = 0 hua,
#   to poora ExceptionGroup raise hota hai.
#
# English Explanation:
# - ExceptionGroup is a Python 3.11 feature.
# - It allows multiple exceptions to be raised together.
# - Here, ValueError, TypeError, and ZeroDivisionError
#   are grouped under one ExceptionGroup.
# - If a equals 0, the grouped exception is raised.
# ------------------------------------------------------------
# -------------------------------------------------------------
# Summary:
# 1. ExceptionGroup is introduced in Python 3.11.
# 2. It groups multiple exceptions into one.
# 3. raise keyword can raise an ExceptionGroup.
# 4. Useful for handling multiple errors together.
# -------------------------------------------------------------
