# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: While Loop – Basics (Initialization, Condition, Updation)
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how the while loop works in Python and how to control iterations.

# -------------------------------------------------------------
# ✅ Concept:
# A while loop repeatedly executes a block of code *as long as* a condition is True.

# Syntax:
# while condition:
#     # code block
#     (must include an update to avoid infinite loops)

# -------------------------------------------------------------
# ✅ Example 1: Print numbers from 0 to 10 (inclusive)
i = 0  # Initialization
while i <= 10:  # Condition
    print(i)
    i = i + 1   # Updation (increment by 1)

# 🧩 Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# -------------------------------------------------------------
# ✅ Example 2: Print numbers from 0 to 9 (10 excluded)
i = 0  # Initialization
while i < 10:  # Condition
    print(i)
    i = i + 1  # Updation

# 🧩 Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# -------------------------------------------------------------
# 🧠 Real-world Analogy:
# A while loop is like a "waiting room":
# You keep waiting (looping) until your name is called (condition becomes False).

# -------------------------------------------------------------
# ⚠️ Important:
# Always include an *updation step* (like i = i + 1)
# Otherwise, you’ll create an infinite loop 🔁
