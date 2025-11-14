# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop – Difference between 'continue' and 'pass'
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how 'continue' and 'pass' behave inside a loop.

# -------------------------------------------------------------
# ✅ Example 1: Using "continue"
# "continue" → Skips the *current iteration* and moves to the next one.
for i in range(5):
    if i == 3:
        continue  # Skip printing when i == 3
    print("Number:", i)

# 🧩 Output:
# Number: 0
# Number: 1
# Number: 2
# (skips 3)
# Number: 4

# -------------------------------------------------------------
# ✅ Example 2: Using "pass"
# "pass" → Does *nothing*, acts as a placeholder for empty code.
for i in range(5):
    if i == 3:
        pass  # Placeholder — doesn’t affect loop flow
    print("Number:", i)

# 🧩 Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4

# -------------------------------------------------------------
# 🧠 Difference Summary:

# continue → Skips execution for that iteration.
# pass     → Does nothing, just a syntactical placeholder.

# -------------------------------------------------------------
# ✅ Real-world QA Example:
# "continue" can be used to skip failed or invalid test cases.
# "pass" can be used to define TODO test logic (to implement later).
