# -------------------------------------------------------------
# 🧠 Lab028_String_Types_and_Raw_Strings.py
# Author: Simran Shaikh
# Topic: Single, Double Quotes & Raw Strings
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how Python treats single-quoted, double-quoted, and raw string literals.
# -------------------------------------------------------------

# Single and Double Quotes behave the same for strings
c = 'C'
c1 = "C"

print("Single quote string:", c)
print("Double quote string:", c1)

# -------------------------------------------------------------
# Problem with Escape Sequences in File Paths
# -------------------------------------------------------------
# When you write something like 'C:\new_folder\note.txt',
# Python interprets \n as a new line — which causes issues.

print("\nExample 1: Normal string with backslash")
dir_path = "C:\pramod\n.txt"  # ❌ This will NOT print correctly
print(dir_path)

# Output may look strange due to '\n' being treated as a newline character

# -------------------------------------------------------------
# ✅ Solution: Use RAW STRING (prefix with 'r' or 'R')
# -------------------------------------------------------------
# Raw strings tell Python to treat backslashes as literal characters,
# not as escape sequences.

print("\nExample 2: Using Raw String (r'...')")
dir_path_raw = r"C:\pramod\n.txt"
print(dir_path_raw)

# The path is printed exactly as written — no escape characters processed.

# -------------------------------------------------------------
# Another Example with Double Backslashes
# -------------------------------------------------------------
print("\nExample 3: Using Double Backslashes (for Windows path)")
dir_path_double = "C:\\pramod\\n.txt"
print(dir_path_double)

# -------------------------------------------------------------
# Real Project Path Example
print("\nExample 4: Real Project File Path")
file_path = r"/Users/simran/PycharmProjects/PyATB6xLearning/src/ex_03_Literals_Variables/Lab028_String_Types_and_Raw_Strings.py"
print(file_path)

# -------------------------------------------------------------
# Tip: Raw strings are ideal for:
# - File paths (Windows)
# - Regular expressions
# - URLs containing backslashes

# ✅ End of Program
print("\n✅ Program executed successfully by Simran Shaikh.")
