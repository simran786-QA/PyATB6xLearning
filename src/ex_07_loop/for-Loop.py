# --------------------------------------------
# 🧠 Lab022_For_Loop_Basics.py
# Author: Simran Shaikh
# Topic: For Loop and range() function
# --------------------------------------------

# 🔹 Objective: Print Hello World multiple times using a loop.

# Example without loop (manual repetition)
# print("Hello World")
# print("Hello World")
# print("Hello World")
# ...
# Tedious and repetitive!

# ✅ Using a loop
# range(start, stop, step)
# start -> where to begin (inclusive)
# stop  -> where to stop (exclusive)
# step  -> how much to increase each time

for i in range(1, 11, 1):  # Loop runs from 1 to 10
    print(f"{i}. Hello World")
