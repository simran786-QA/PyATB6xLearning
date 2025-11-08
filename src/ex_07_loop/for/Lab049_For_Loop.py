# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: For Loop with Step Value and range() Function
# -------------------------------------------------------------

# 🎯 Objective:
# Understand how to control loop iteration using the `step` argument in range().
# Learn that `range()` only supports integer steps — not floats.

# -------------------------------------------------------------
# ✅ 1. Basic Example – Increment by 1
print("Increment by 1:")
for i in range(0, 10, 1):
    print(i)

# -------------------------------------------------------------
# ✅ 2. Increment by 2
print("\nIncrement by 2:")
for i in range(0, 10, 2):
    print(i)

# -------------------------------------------------------------
# ✅ 3. Increment by 3
print("\nIncrement by 3:")
for i in range(0, 10, 3):
    print(i)

# -------------------------------------------------------------
# ❌ 4. Invalid Example – Non-integer step
# range() only accepts integer step values.
# Using a float like 1.5 will raise a TypeError.

# Uncomment this block to test the error
# for i in range(0, 10, 1.5):
#     print(i)

# Output:
# TypeError: 'float' object cannot be interpreted as an integer

# -------------------------------------------------------------
# ✅ 5. Workaround using w
