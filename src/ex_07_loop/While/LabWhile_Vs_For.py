# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: While Loop – Running Multiple Test Cases
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to use a `while` loop to repeat an action
# (like running test cases) until a condition becomes False.

# -------------------------------------------------------------
# ✅ Example Code
test_id = 0  # Initialization → Start with first test case

while test_id < 10:  # Condition → Run while test_id is less than 10
    print("Running the testcase ->", test_id)
    test_id = test_id + 1  # Increment → Move to the next test case

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - The loop starts with `test_id = 0`.
# - As long as `test_id < 10`, the loop keeps running.
# - Each iteration prints which test case is running.
# - The counter increases by 1 after every iteration.
# - When `test_id` becomes 10, the condition fails → loop stops.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - Loop की शुरुआत `test_id = 0` से होती है।
# - जब तक `test_id < 10` True रहता है, loop चलता रहेगा।
# - हर बार एक नया test case number print होगा।
# - `test_id = test_id + 1` से count बढ़ता जाता है।
# - जब `test_id` 10 हो जाता है, condition False हो जाती है → loop रुक जाता है।

# -------------------------------------------------------------
# ✅ Output:
# Running the testcase -> 0
# Running the testcase -> 1
# Running the testcase -> 2
# Running the testcase -> 3
# Running the testcase -> 4
# Running the testcase -> 5
# Running the testcase -> 6
# Running the testcase -> 7
# Running the testcase -> 8
# Running the testcase -> 9

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | test_id | Condition (test_id < 10) | Action         | Output                         |
# |----------|--------------------------|----------------|---------------------------------|
# | 0        | True                     | print & +1     | Running the testcase -> 0       |
# | 1        | True                     | print & +1     | Running the testcase -> 1       |
# | 2        | True                     | print & +1     | Running the testcase -> 2       |
# | ...      | ...                      | ...            | ...                             |
# | 9        | True                     | print & +1     | Running the testcase -> 9       |
# | 10       | False                    | Exit loop      | —                               |

# -------------------------------------------------------------
# 💡 Real-World QA Analogy:
# Imagine you are running automation test cases in a loop.
# Each test case has a unique ID (0 to 9).
# Once all test cases finish, the loop automatically stops.
# -------------------------------------------------------------
