
```python
# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – raise Exception
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define a function for login validation
# -------------------------------------------------------------
# This function checks whether the user is authorized or not.

def vwo_login(user):
    # ---------------------------------------------------------
    # Step 2: Check user condition
    # ---------------------------------------------------------
    # If the user is not "admin", raise a custom exception.
    if user != "admin":
        raise Exception("Unauthorized Access!!")

    # ---------------------------------------------------------
    # Step 3: Return success message
    # ---------------------------------------------------------
    return "Welcome Admin"


# -------------------------------------------------------------
# Step 4: Function call
# -------------------------------------------------------------
# Uncommenting the below line will raise an Exception.
# print(vwo_login("pramod"))

# Valid user call
print(vwo_login("admin"))


# -------------------------------------------------------------
# Hindi Explanation:
# - vwo_login naam ka function banaya gaya hai.
# - Agar user "admin" nahi hai, to manually Exception raise hoti hai.
# - raise keyword se hum khud ka error throw kar sakte hain.
# - Agar user "admin" hai, to welcome message return hota hai.
#
# English Explanation:
# - A function named vwo_login is created.
# - If the user is not "admin", a custom Exception is raised.
# - The raise keyword is used to throw an exception manually.
# - If the user is valid, a success message is returned.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. raise keyword is used to throw custom exceptions.
# 2. Exceptions are used to control invalid scenarios.
# 3. This approach improves security and validation logic.
# 4. Program stops execution when an exception is raised.
# -------------------------------------------------------------
```
