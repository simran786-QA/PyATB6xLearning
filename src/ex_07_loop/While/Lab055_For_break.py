# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Using 'break' in For Loop
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how the 'break' statement works in Python loops.
# 'break' immediately exits the loop when a condition is met.

# -------------------------------------------------------------
# ✅ Example: Stop printing numbers once i == 5
for i in range(0, 10):  # Loop from 0 → 9 (10 times)
    print(i)
    if i == 5:
        break  # Exit the loop when i = 5

# -------------------------------------------------------------
# 🧩 Output:
# 0
# 1
# 2
# 3
# 4
# 5

# -------------------------------------------------------------
# 🧠 Explanation:
# - The loop starts from i = 0 and increments by 1.
# - When i becomes 5 → condition (i == 5) is True → 'break' executes.
# - The loop stops immediately and does NOT continue further.

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | i  | Condition (i == 5) | Result  | Output | Action  |
# |----|--------------------|----------|---------|----------|
# | 0  | False              | Continue | 0       | Next i   |
# | 1  | False              | Continue | 1       | Next i   |
# | 2  | False              | Continue | 2       | Next i   |
# | 3  | False              | Continue | 3       | Next i   |
# | 4  | False              | Continue | 4       | Next i   |
# | 5  | True               | Break    | 5       | Stop loop|

# -------------------------------------------------------------
# 🧩 Real-world QA Analogy:
# Imagine running test cases sequentially.
# When a **critical failure (i == 5)** occurs, you **stop execution**
# — similar to using 'break' in test automation to prevent further tests
# from running after a major failure.
