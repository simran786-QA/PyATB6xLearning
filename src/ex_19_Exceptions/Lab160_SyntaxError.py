# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Error Handling – SyntaxError
# -------------------------------------------------------------

# Step 1: Incorrect while loop syntax
# -------------------------------------------------------------
# Uncomment the line below to see the error:

# while True print("Hello World!")

# Error Produced:
# SyntaxError: invalid syntax


# -------------------------------------------------------------
# Hindi Explanation:
# - Python me while loop ke baad colon (:) lagana mandatory hota hai.
# - Yahan "while True" ke baad colon missing hai.
# - Is wajah se Python code ko samajh nahi pata
# - Aur SyntaxError throw karta hai.

# English Explanation:
# - In Python, a colon (:) is required after while condition.
# - The statement "while True print(...)" is missing a colon.
# - Python cannot parse the statement correctly.
# - Hence, it raises a SyntaxError.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Correct Syntax (Example):
# -------------------------------------------------------------
# while True:
#     print("Hello World!")
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. SyntaxError occurs when Python syntax rules are violated.
# 2. Loops and conditions must end with a colon (:).
# 3. Missing colon causes SyntaxError.
# 4. Always check indentation and colons in loops and conditions.
# -------------------------------------------------------------
