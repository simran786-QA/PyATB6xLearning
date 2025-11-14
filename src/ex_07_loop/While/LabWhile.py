# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: While Loop – Basic Counter Example
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how the `while` loop works by repeating code
# until a specific condition becomes False.

# -------------------------------------------------------------
# ✅ Example Code
count = 0                      # Initialization (start point)
while count < 5:               # Condition check
    print("Count is:", count)  # Loop body
    count += 1                 # Update (increment the counter)

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - The loop starts with `count = 0`.
# - The condition `count < 5` is checked before every iteration.
# - As long as it’s True → the body executes.
# - After each run, `count += 1` increases the value by 1.
# - When `count` becomes 5, the condition `count < 5` becomes False → loop stops.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - Loop की शुरुआत `count = 0` से होती है।
# - Condition `count < 5` check होती है हर बार loop चलने से पहले।
# - जब तक condition True रहती है, तब तक loop चलता रहता है।
# - हर बार `count += 1` करके value बढ़ती है।
# - जब `count` 5 हो जाता है, condition False हो जाती है और loop रुक जाता है।

# -------------------------------------------------------------
# ✅ Output:
# Count is: 0
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | count | Condition (count < 5) | Action         | Output        |
# |--------|----------------------|----------------|----------------|
# | 0      | True                 | print & +1     | Count is: 0    |
# | 1      | True                 | print & +1     | Count is: 1    |
# | 2      | True                 | print & +1     | Count is: 2    |
# | 3      | True                 | print & +1     | Count is: 3    |
# | 4      | True                 | print & +1     | Count is: 4    |
# | 5      | False                | Exit loop      | —              |

# -------------------------------------------------------------
# 💡 Real-World QA Analogy:
# Imagine you are running 5 automated tests.
# The `while` loop keeps executing test cases (Count 0 → 4)
# until all have finished (Count = 5), then stops automatically.
# -------------------------------------------------------------
