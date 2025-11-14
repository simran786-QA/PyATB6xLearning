# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop with If-Else Condition
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how conditional checks (`if-else`) work inside a `for` loop.

# -------------------------------------------------------------
# ✅ Example: Print the number only when it equals 6, else print "No O/P"

for i in range(0, 10, 1):  # Loop runs from 0 → 9
    if i == 6:
        print(i)
    else:
        print("No O/P")

# -------------------------------------------------------------
# 🧩 Output:
# No O/P
# No O/P
# No O/P
# No O/P
# No O/P
# No O/P
# 6
# No O/P
# No O/P
# No O/P

# -------------------------------------------------------------
# 🧠 Explanation:
# - The loop iterates through numbers 0 to 9.
# - If `i == 6`, the condition becomes True and prints `6`.
# - For all other values, the `else` block executes, printing `"No O/P"`.

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | i  | Condition (i == 6) | Result | Output   |
# |----|--------------------|---------|----------|
# | 0  | False              | Else    | No O/P   |
# | 1  | False              | Else    | No O/P   |
# | 2  | False              | Else    | No O/P   |
# | 3  | False              | Else    | No O/P   |
# | 4  | False              | Else    | No O/P   |
# | 5  | False              | Else    | No O/P   |
# | 6  | True               | If      | 6        |
# | 7  | False              | Else    | No O/P   |
# | 8  | False              | Else    | No O/P   |
# | 9  | False              | Else    | No O/P   |

# -------------------------------------------------------------
# 🧩 Real-world QA Analogy:
# Imagine running multiple test cases (0–9).
# Only one specific test (test case 6) passes, while others fail or skip.
# The `if` condition identifies the passing test and the `else` marks the rest.
