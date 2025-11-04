# -------------------------------------------------------------
# 🧠 Lab051_Quotient_Remainder.py
# Author: Simran Shaikh
# Topic: Calculate Quotient and Remainder of Two Numbers
# -------------------------------------------------------------

# 🎯 Objective:
# Take two numbers as input from the user and print their quotient and remainder.
# Example:
# num1 = 15, num2 = 2 → Quotient = 7, Remainder = 1

# -------------------------------------------------------------
# Step 1: Take user inputs
num1 = int(input("Enter the first number (Dividend): "))
num2 = int(input("Enter the second number (Divisor): "))

# -------------------------------------------------------------
# Step 2: Validate and perform division
if num2 == 0:
    print("❌ Division by zero is not allowed!")
else:
    quotient = num1 // num2
    remainder = num1 % num2

    # -------------------------------------------------------------
    # Step 3: Display results (formatted)
    print("\n📊 --- Division Results ---")
    print(f"Dividend: {num1}")
    print(f"Divisor : {num2}")
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")

    print("\n✅ Program executed successfully by Simran Shaikh.")
