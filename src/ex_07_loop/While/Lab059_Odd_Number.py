# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop with CONTINUE – Printing Odd Numbers
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to use the `continue` statement in loops to skip specific conditions.
# Here, we’ll print all ODD numbers from 0 to 9.

# -------------------------------------------------------------
# ✅ Example 1: Simple logic using condition only
# for i in range(10):
#     if i % 2 != 0:
#         print(i)

# -------------------------------------------------------------
# ✅ Example 2: Using `continue` to skip even numbers
for number in range(10):  # Loop runs from 0 → 9
    if number % 2 == 0:   # If number is even → skip this iteration
        continue           # Go to the next loop cycle
    else:
        print(number)      # If not even → print (odd number)

# -------------------------------------------------------------
# 🧠 Explanation (English):
# - `range(10)` gives numbers 0 to 9.
# - `number % 2 == 0` means the number is even.
# - When condition is true → `continue` skips remaining code inside loop.
# - Only ODD numbers reach the `print()` statement.

# -------------------------------------------------------------
# 🧠 Explanation (Hindi):
# - `range(10)` → 0 से 9 तक loop चलेगा।
# - अगर `number % 2 == 0` (even number है) → `continue` statement बाकी code को skip कर देता है।
# - इसलिए केवल ODD numbers print होंगे।

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | number | number % 2 == 0 | Action     | Output  |
# |---------|----------------|-------------|----------|
# | 0       | True            | continue    | -        |
# | 1       | False           | print()     | 1        |
# | 2       | True            | continue    | -        |
# | 3       | False           | print()     | 3        |
# | 4       | True            | continue    | -        |
# | 5       | False           | print()     | 5        |
# | 6       | True            | continue    | -        |
# | 7       | False           | print()     | 7        |
# | 8       | True            | continue    | -        |
# | 9       | False           | print()     | 9        |

# -------------------------------------------------------------
# 💡 Real-World QA Analogy:
# Imagine you’re testing 10 builds, but you want to skip all even-numbered builds
# because they’re “internal test” versions.
# The `continue` statement helps you skip them automatically while testing.

# -------------------------------------------------------------
