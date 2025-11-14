# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: range() object and reverse looping
# -------------------------------------------------------------

# 🎯 Objective:
# Understand what happens when you print a range object,
# and how to loop in reverse order using a negative step.
# -------------------------------------------------------------

# ✅ Example 1: Reverse Loop using range()
for i in range(10, 0, -2):
    print(i)
# Output: 10, 8, 6, 4, 2
# Starts from 10, decreases by 2 each time, stops before 0.

# -------------------------------------------------------------
# ✅ Example 2: Printing the range() object directly
num = range(10)
print(num)
# Output: range(0, 10)
# "range" is a built-in Python object — it represents a sequence, but doesn’t store all numbers.
# It’s *lazy*, meaning numbers are generated when needed (like during a loop).

# -------------------------------------------------------------
# ✅ Example 3: Converting range to a list to see all numbers
print(list(num))
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# -------------------------------------------------------------
# 🧠 Real-World Analogy:
# range() is like a playlist link — it *knows* the songs (numbers),
# but doesn’t *download* them until you hit play (loop or list()).
