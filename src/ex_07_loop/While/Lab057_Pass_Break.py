# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop with Multiple Conditions (if - else - pass)
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to handle multiple conditions inside a loop using logical OR (`or`)
# and how to use the `pass` statement to "do nothing" when a condition is False.

# -------------------------------------------------------------
# ✅ Example:
# Print numbers only when they are 5 or 6.
# For all other numbers, do nothing (skip silently).

for i in range(0, 10, 1):  # Loop runs from 0 → 9
    if i == 6 or i == 5:
        print(i)
    else:
        pass  # No action for other numbers

# -------------------------------------------------------------
# 🧩 Output:
# 5
# 6

# -------------------------------------------------------------
# 🧠 Explanation:
# - The loop iterates from 0 to 9.
# - The `if` condition checks if `i` is equal to 5 **or** 6.
# - If True → prints the number.
# - If False → executes `pass` (i.e., no operation is performed).

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | i  | Condition (i == 5 or i == 6) | Result | Output                 |
# |----|------------------------------|---------|------------------------|
# | 0  | False                        | Pass    | Nothing printed        |
# | 1  | False                        | Pass    | Nothing printed        |
# | 2  | False                        | Pass    | Nothing printed        |
# | 3  | False                        | Pass    | Nothing printed        |
# | 4  | False                        | Pass    | Nothing printed        |
# | 5  | True                         | If      | 5                      |
# | 6  | True                         | If      | 6                      |
# | 7  | False                        | Pass    | Nothing printed        |
# | 8  | False                        | Pass    | Nothing printed        |
# | 9  | False                        | Pass    | Nothing printed        |

# -------------------------------------------------------------
# 💡 Note:
# The `pass` statement is useful when you want to write syntactically correct
# code but don’t want to perform any action yet (acts as a placeholder).

# -------------------------------------------------------------
# 🧩 Real-world QA Analogy:
# Imagine you are executing 10 test cases.
# Only test cases 5 and 6 are currently implemented and should execute.
# The others are skipped (no output), represented by the `pass` keyword.
