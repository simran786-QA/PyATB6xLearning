# -------------------------------------------------------------
# 🧠 Lab026_DataTypes_and_NumberSystems.py
# Author: Simran Shaikh
# Topic: Data Types and Different Number Systems in Python
# -------------------------------------------------------------

# 🎯 Objective:
# Learn about:
# - Basic Python data types
# - Number systems: Decimal, Binary, Octal, Hexadecimal
# - Boolean and Complex numbers
# -------------------------------------------------------------

print("🔹 Welcome to Simran’s Data Type & Number System Lab 🔹\n")

# -------------------------------------------------------------
# 1️⃣ Decimal System (Base 10)
# The most common number system — used in daily life.
age = 89
print("🧮 Decimal Number:", age)
print("➡️ Type:", type(age))

# -------------------------------------------------------------
# 2️⃣ Binary System (Base 2)
# Only uses digits 0 and 1 — mostly used in computer memory and logic.
binary_number = 0b1010  # binary literal for 10 in decimal
print("\n💡 Binary Number: 0b1010")
print("➡️ In Decimal:", binary_number)
print("➡️ Type:", type(binary_number))

# -------------------------------------------------------------
# 3️⃣ Octal System (Base 8)
# Digits from 0 to 7 — used sometimes in Unix file permissions.
octal_number = 0o130  # Octal literal
print("\n🌀 Octal Number: 0o130")
print("➡️ In Decimal:", octal_number)
print("➡️ Type:", type(octal_number))

# -------------------------------------------------------------
# 4️⃣ Hexadecimal System (Base 16)
# Uses digits 0–9 and letters A–F — very common in color codes, memory addresses.
hex_number = 0x12C  # Hex literal
print("\n🎨 Hexadecimal Number: 0x12C")
print("➡️ In Decimal:", hex_number)
print("➡️ Type:", type(hex_number))

# -------------------------------------------------------------
# 5️⃣ Floating-Point Number (Decimal with Fraction)
pi = 3.14
print("\n🔢 Floating-Point Number (pi):", pi)
print("➡️ Type:", type(pi))

# -------------------------------------------------------------
# 6️⃣ String (Sequence of Characters)
name = "Simran"
print("\n💬 String Example:", name)
print("➡️ Type:", type(name))

# -------------------------------------------------------------
# 7️⃣ Boolean (True / False)
is_simran_married = True
print("\n🔘 Boolean Example:", is_simran_married)
print("➡️ Type:", type(is_simran_married))

# -------------------------------------------------------------
# 8️⃣ Complex Number (a + bj)
complex_number = 1 + 7j
print("\n⚙️ Complex Number Example:", complex_number)
print("➡️ Type:", type(complex_number))
print("➡️ Real Part:", complex_number.real)
print("➡️ Imaginary Part:", complex_number.imag)

# -------------------------------------------------------------
# ✅ End of Program
print("\n✅ Program executed successfully by Simran Shaikh.")
