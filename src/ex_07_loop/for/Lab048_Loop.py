# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop and range() in Python
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how to use loops to repeat actions and explore how
# the range() function controls iteration.

# -------------------------------------------------------------
# ✅ 1. Without Loop (Manual Repetition)
# This is repetitive and inefficient.
# print("Hello World")
# print("Hello World")
# print("Hello World")
# ...
# Instead, we’ll use a loop.

# -------------------------------------------------------------
# ✅ 2. For Loop with range()
# Syntax: range(start, stop, step)
# - start → where to begin (inclusive)
# - stop  → where to end (exclusive)
# - step  → how much to increment by

for i in range(1, 10, 1):
    print(i)

# -------------------------------------------------------------
# ✅ 3. Example: Print "Hello World" 10 times
for i in range(10):
    print("Hello World")

# -------------------------------------------------------------
# ✅ 4. Explanation
# range(1, 10, 1) → starts at 1, stops before 10, step = 1
# range(10) → starts at 0, stops before 10, step = 1

# -------------------------------------------------------------
# ✅ 5. Reverse Counting Example
for i in range(10, 0, -1):
    print("Countdown:", i)

print("🚀 Blast Off!")
