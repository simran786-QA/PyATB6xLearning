# -------------------------------------------------------------
# 🧠 Lab024_Strings_and_Their_Functions.py
# Author: Simran Shaikh
# Topic: Understanding Strings, Types, and String Methods
# -------------------------------------------------------------

# 🎯 Objective:
# - Understand string data type
# - Practice basic string operations and built-in functions
# -------------------------------------------------------------

# Step 1️⃣: Input from user
value = input("Enter any value: ")
print("\n🔹 You entered:", value)
print("📘 Data type:", type(value))  # Always <class 'str'> because input() returns a string

# -------------------------------------------------------------
# Step 2️⃣: Understanding what strings are
name = "Simran"          # Double quotes
char_single = 'S'        # Single quotes - still string
char_double = "S"        # Double quotes - same result

print("\n 🧩 string example: ")
print(f"name: {name} char_single: {char_single} char_double: {char_double}"
)
print(type(name))
print(type(char_single))
print(type(char_double))
# ----------------------------------------------------------
# Step 3️⃣: String Length & Case Conversion
print('\n string Lenght and case Operations; ')
print(f"lenght of '{name}' --> {len(name)}")
print(f"uppercase of '{name}' --> {name.upper()}")
print(f"lowercase of '{name}' --> {name.lower()}")
print(f"capitalized '{name}' --> {name.capitalize()}")
print(f"title of '{name}' --> {name.title()}")

# -------------------------------------------------------------
# Step 4️⃣: More Useful String Methods
quote = "python is awesome & powerful & fun !"
print("\n more string functions:")
print("original string:", repr(quote))
print ("after strip():" , quote.strip())# Removes spaces from both ends
print("After replace():", quote.replace("Fun", "Amazing"))
print("After split():", quote.split())            # Splits string into list of words
print("After find('is'):", quote.find("is"))      # Finds the first index of 'is'
print("After count('n'):", quote.count("n"))      # Counts occurrences of 'n'

# -------------------------------------------------------------
# Step 5️⃣: String Concatenation and Formatting
fname = "Simran"
lname = "Shaikh"
age = 24

print("\n🔗 String Concatenation:")
print("Hello " + fname + " " + lname + "!")        # Manual concatenation
print(f"Hi, I’m {fname} {lname}, and I’m {age} years old.")  # Using f-string
print("Name: {} {}, Age: {}".format(fname, lname, age))       # Using format() method

# -------------------------------------------------------------
# Step 6️⃣: Multiline String Example
intro = """\n📝 About Me:
Hello! My name is Simran Shaikh.
I’m learning Python programming for QA Automation.
I love exploring logic, testing, and building creative solutions.
"""
print(intro)

# -------------------------------------------------------------
# ✅ End of Program
print("✅ Program executed successfully by Simran Shaikh")
