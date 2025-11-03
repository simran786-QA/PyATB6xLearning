# -------------------------------------------------------------
# 🧠 Lab050_Multi_Number_Operations.py
# Author: Simran Shaikh
# Topic: Arithmetic Operations on 3 Numbers
# -------------------------------------------------------------

# 🎯 Objective:
# Take 3 numbers as input and perform Addition, Subtraction, Multiplication, and Division.

# -------------------------------------------------------------
# Step 1: Take inputs from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# -------------------------------------------------------------
# Step 2: Perform Operations

# Addition
sum_result = num1 + num2 + num3

# Subtraction
sub_result = num1 - num2 - num3

# Multiplication
mul_result = num1 * num2 * num3

# Division (avoid divide by zero)
if num2 == 0 or num3 == 0:
    div_result = "❌ Division by zero is not allowed!"
else:
    div_result = (num1 / num2) / num3

# -------------------------------------------------------------
# Step 3: Display Results (formatted output)
print("\n📊 --- Calculation Results ---")
print(f"1️⃣ Addition:       {num1} + {num2} + {num3} = {sum_result:.2f}")
print(f"2️⃣ Subtraction:    {num1} - {num2} - {num3} = {sub_result:.2f}")
print(f"3️⃣ Multiplication: {num1} × {num2} × {num3} = {mul_result:.2f}")
print(f"4️⃣ Division:       ({num1} / {num2}) / {num3} = {div_result}")

print("\n✅ Program executed successfully by Simran Shaikh.")
