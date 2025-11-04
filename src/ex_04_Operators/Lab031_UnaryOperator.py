# -------------------------------------------------------------
# 🧠 Lab054_Unary_Operators.py
# Author: Simran Shaikh
# Topic: Unary Operators in Python (एकवाची ऑपरेटर्स)
# -------------------------------------------------------------

# 🎯 Objective:
# Understand the use of unary plus (+) and unary minus (-) operators.

# -------------------------------------------------------------
# Step 1: Unary + and -
age = +65   # Unary plus (value remains positive)
age2 = -65  # Unary minus (value becomes negative)

print("📘 Example 1: Unary Operators")
print(f"age  = {age}")   # Output: 65
print(f"age2 = {age2}")  # Output: -65

# -------------------------------------------------------------
# Step 2: Using unary with a variable counter
print("\n📗 Example 2: Increment/Decrement Logic")

how_many_lambo_pramod = -1  # Initially, Pramod has -1 Lambo (imaginary debt 😅)
print(f"Initial Lambos: {how_many_lambo_pramod}")

# Increase count by 1 (same as how_many_lambo_pramod += 1)
how_many_lambo_pramod = how_many_lambo_pramod + 1

print(f"Updated Lambos after success 🏎️: {how_many_lambo_pramod}")

print("\n✅ Program executed successfully by Simran Shaikh.")
