# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Factorial of a Number – Loop and Logic Building
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how to calculate the factorial of a number using loops.
# This logic is often used in automation to test numeric functions or algorithms.

# -------------------------------------------------------------
# 🧪 Example:
# Input  → num = 5
# Output → 5! = 5 × 4 × 3 × 2 × 1 = 120
# -------------------------------------------------------------

# Take input from user
num = int(input("Enter a number to find its factorial: "))

# Initialize factorial variable
fact = 1

# Handle negative numbers
if num < 0:
    print("❌ Factorial is not defined for negative numbers!")

# Handle zero separately (0! = 1)
elif num == 0:
    print("✅ Factorial of 0 is 1")

# Calculate factorial using loop
else:
    for i in range(1, num + 1):
        fact = fact * i
    print(f"✅ Factorial of {num} is: {fact}")

# -------------------------------------------------------------
# 🧠 Explanation:
# - Factorial(n) = n × (n-1) × (n-2) × ... × 1
# - Used in permutations, combinations, and recursion testing.

# -------------------------------------------------------------
# ✅ Example Test Data (ERT)
# | num | Condition             | Output                    |
# |-----|------------------------|----------------------------|
# | -5  | num < 0                | ❌ Factorial not defined    |
# | 0   | num == 0               | ✅ Factorial = 1            |
# | 5   | num > 0                | ✅ Factorial = 120          |

# -------------------------------------------------------------
# 💡 QA Use Case:
# - Logic validation in automation test flows
# - Input boundary testing (negative, zero, positive)
# - Used in coding assessments for automation engineers
# -------------------------------------------------------------
