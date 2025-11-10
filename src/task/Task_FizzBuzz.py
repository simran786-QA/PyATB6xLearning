# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: FizzBuzz Test (Logic Building & Loop Practice)
# -------------------------------------------------------------

# 🎯 Objective:
# Print numbers from 1 to 100 with special conditions:
# - If divisible by 3 → Print "Fizz"
# - If divisible by 5 → Print "Buzz"
# - If divisible by both 3 and 5 → Print "FizzBuzz"
# -------------------------------------------------------------

# 🧩 Logic:
# Use a for loop from 1 → 100.
# Check divisibility using the modulo operator (%).
# Apply combined condition first to avoid overlapping matches.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")  # Multiples of both 3 and 5
    elif i % 3 == 0:
        print("Fizz")      # Multiples of 3
    elif i % 5 == 0:
        print("Buzz")      # Multiples of 5
    else:
        print(i)           # Other numbers

# -------------------------------------------------------------
# 🧠 Explanation:
# Modulo (%) gives the remainder.
# Example:
#   9 % 3 = 0  ✅ divisible by 3
#   10 % 5 = 0 ✅ divisible by 5
#   15 % 3 = 0 and 15 % 5 = 0 → FizzBuzz

# -------------------------------------------------------------
# ✅ Sample Output (Partial):
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# -------------------------------------------------------------
# 💡 QA/Automation Relevance:
# - Used to test conditional logic and loops in coding rounds.
# - Great for testing code behavior under multiple conditional flows.
# - Similar pattern used for checking test case outcomes (e.g., pass/fail/status).
# -------------------------------------------------------------
