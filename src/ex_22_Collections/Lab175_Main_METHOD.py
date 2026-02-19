# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Entry Point – __name__ == "__main__"
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define main function
# -------------------------------------------------------------
# This function contains the main execution logic.

def main():
    print("Main called!")


# -------------------------------------------------------------
# Step 2: Entry point check
# -------------------------------------------------------------
# __name__ is a special built-in variable in Python.
# If the file is executed directly, __name__ becomes "__main__".
# If the file is imported as a module, this block will not run.

if __name__ == "__main__":  # Python entry point
    main()


# -------------------------------------------------------------
# Hindi Explanation:
# - main() function program ka starting logic rakhta hai.
# - __name__ ek special variable hai.
# - Jab file direct run hoti hai, __name__ = "__main__" hota hai.
# - Tab main() function call hota hai.
# - Agar file import hui ho, to ye block execute nahi hota.
#
# English Explanation:
# - main() holds the primary execution logic.
# - __name__ is a special Python variable.
# - When the script runs directly, __name__ equals "__main__".
# - The main() function executes only in that case.
# - When imported as a module, this block is skipped.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. __name__ == "__main__" defines the program entry point.
# 2. Prevents auto execution when file is imported.
# 3. Improves modular and reusable code structure.
# 4. Common best practice in Python programs.
# -------------------------------------------------------------
