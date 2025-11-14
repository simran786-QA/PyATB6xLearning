# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop – Printing Even Numbers Using Modulus Operator
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to use loops with conditional logic to filter specific values
# (in this case, even numbers) from a range of numbers.

# -------------------------------------------------------------
# ✅ Example: Print all even numbers between 0 and 100

for i in range(101):  # Loop from 0 → 100 (inclusive)
    if i % 2 == 0:    # Condition to check even number
        print(i)

# -------------------------------------------------------------
# 🧠 Explanation:
# - The `range(101)` generates numbers from 0 to 100.
# - The `%` (modulus) operator gives the remainder when dividing `i` by 2.
# - If remainder == 0 → number is even.
# - Therefore, only even numbers are printed.

# -------------------------------------------------------------
# ✅ Expression and Result Table (ERT)

# | i  | Condition (i % 2 == 0) | Result | Output                 |
# |----|------------------------|---------|------------------------|
# | 0  | True                   | If      | 0                      |
# | 1  | False                  | Skip    | -                      |
# | 2  | True                   | If      | 2                      |
# | 3  | False                  | Skip    | -                      |
# | 4  | True                   | If      | 4                      |
# | 5  | False                  | Skip    | -                      |
# | ...| ...                    | ...     | ...                    |
# | 100| True                   | If      | 100                    |

# -------------------------------------------------------------
# 💡 Note:
# - `i % 2 == 0` → Even numbers.
# - `i % 2 != 0` → Odd numbers.
# You can easily switch between even/odd by toggling this condition.

# -------------------------------------------------------------
# 🧩 Real-World QA Analogy:
# Imagine you are validating 100 test results.
# You only want to print tests that passed on even-numbered builds (0, 2, 4...).
# This same logic helps you filter out specific test IDs based on conditions.
