# -------------------------------------------------------------
# Step 1: Function with Default Parameter
# -------------------------------------------------------------
# Default parameter = "QA"
# Hindi: Agar koi naam pass nahi karoge, to default value "QA" use hogi.
# English: If no name is given, "QA" will be used as the default.

def greet_with_default_param(name="QA"):
    print("Hi,", name)


# -------------------------------------------------------------
# Step 2: Calling the Function
# -------------------------------------------------------------
# Passing different names + using default value.

greet_with_default_param("Pramod")     # Output: Hi, Pramod
greet_with_default_param("Amit")       # Output: Hi, Amit
greet_with_default_param()             # Output: Hi, QA
