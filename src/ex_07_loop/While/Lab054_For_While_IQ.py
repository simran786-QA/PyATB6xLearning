# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop with If-Else and Expression Result Table (ERT)
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how conditional checks work inside a for loop
# and how to trace each iteration using an Expression Result Table.

# -------------------------------------------------------------
# ✅ Example: Print numbers from 0–9, replace 5 with "Five"
for i in range(0, 10):  # Loop runs from 0 → 9 (10 times)
    if i == 5:
        print("Five")
    else:
        print(i)

# -------------------------------------------------------------
# 🧩 Output:
# 0
# 1
# 2
# 3
# 4
# Five
# 6
# 7
# 8
# 9

# -------------------------------------------------------------
# 🧠 Explanation:
# The loop variable `i` changes each iteration.
# When i == 5 → the if condition is True → prints "Five"
# For all other numbers → prints i as it is.

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | i  | Condition (i == 5) | Result | Output  |
# |----|--------------------|---------|----------|
# | 0  | False              | else    | 0        |
# | 1  | False              | else    | 1        |
# | 2  | False              | else    | 2        |
# | 3  | False              | else    | 3        |
# | 4  | False              | else    | 4        |
# | 5  | True               | if      | Five     |
# | 6  | False              | else    | 6        |
# | 7  | False              | else    | 7        |
# | 8  | False              | else    | 8        |
# | 9  | False              | else    | 9        |

# -------------------------------------------------------------
# 🧩 Real-world QA Analogy:
# Think of this like running 10 automated test cases.
# When test #5 fails (special case), you log a custom message (“Five”).
# Otherwise, you simply log the test ID.
