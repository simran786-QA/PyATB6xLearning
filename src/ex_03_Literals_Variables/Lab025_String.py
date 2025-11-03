# -------------------------------------------------------------
# 🧠 Lab025_String_Concatenation_and_TypeCasting.py
# Author: Simran Shaikh
# Topic: String Concatenation, Type Casting, and Data Types
# -------------------------------------------------------------

# 🎯 Objective:
# - Learn how to join (concatenate) strings
# - Understand the importance of converting data types before combining
# - Practice real-world examples
# -------------------------------------------------------------

# Step 1️⃣: Create a basic string
name = "This is a Big line"
print("🧩 Value of name:", name)
print("📘 Data type of 'name':", type(name))

# -------------------------------------------------------------
# Step 2️⃣: Concatenation with a Number
# ❌ This will throw an error if we try: print(name + 1)
# Because Python cannot directly combine 'str' and 'int'

# ✅ Correct way — convert number to string using str()
name = name + str(1)
print("\n✅ After concatenation ->", name)
print("📘 New data type of 'name':", type(name))

# -------------------------------------------------------------
# Step 3️⃣: Real-world Example — Full Name Creation
first_name = "Simran"
last_name = "Shaikh"

# Combine using `+`
full_name = first_name + " " + last_name
print("\n👤 Full Name:", full_name)
print("📘 Data type:", type(full_name))

# -------------------------------------------------------------
# Step 4️⃣: Alternate Ways to Combine Strings

# Using comma (adds space automatically)
print("\n🗣️ Using comma in print():")
print("Hello,", first_name, last_name)

# Using f-string (modern and preferred way)
print("\n✨ Using f-string:")
print(f"Hello {first_name} {last_name}, welcome to Python learning!")

# Using format() method
print("\n🧱 Using format() method:")
print("Hello {} {}, great to see you!".format(first_name, last_name))

# -------------------------------------------------------------
# Step 5️⃣: Another Example — Label Printing
version = 3
language = "Python"
print(f"\n💻 You are learning {language} version {version}.")

# -------------------------------------------------------------
# ✅ End of Program
print("\n✅ Program executed successfully by Simran Shaikh.")
