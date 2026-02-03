# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling – FileNotFoundError
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Try to read a file
# -------------------------------------------------------------
# We are trying to open and read a JSON file.
# This is a risky operation because the file may not exist.

try:
    data = open("test.json").read()


# -------------------------------------------------------------
# Step 2: Handle FileNotFoundError
# -------------------------------------------------------------
# This block executes if the file is not found in the directory.

except FileNotFoundError as fnf:
    print(fnf)


# -------------------------------------------------------------
# Additional Code (Commented)
# -------------------------------------------------------------
# Below is an example of class inheritance.
# It is commented and not executed.

# class A:
#     pass
#
# class B(A):
#     pass


# -------------------------------------------------------------
# Hindi Explanation:
# - try block ke andar file open aur read karne ki koshish ho rahi hai.
# - Agar "test.json" file exist nahi karti,
#   to Python FileNotFoundError throw karta hai.
# - except block error ko catch karta hai aur message print karta hai.
# - Neeche diya gaya class code sirf inheritance ka example hai,
#   jo abhi commented hai.
#
# English Explanation:
# - The try block attempts to open and read a file.
# - If the file does not exist, Python raises FileNotFoundError.
# - The except block catches the exception and prints the error.
# - The commented classes show a simple inheritance example.
# -------------------------------------------------------------
# -------------------------------------------------------------
# Summary:
# 1. File operations can raise FileNotFoundError.
# 2. try-except prevents program crash.
# 3. Error object (fnf) contains detailed error info.
# 4. Commented code does not affect execution.
# -------------------------------------------------------------
