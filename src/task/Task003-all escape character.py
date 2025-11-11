# ============================================================
# 🧮 Lab017_Escape_Characters.py
# 👩‍💻 Author: Simran Shaikh
# 🎯 Goal: Demonstrate all Escape Characters in Python
# ============================================================

# Escape characters start with a backslash (\)
# They help in formatting strings and adding special characters inside text

# -----------------------------
# \n -> New Line
# -----------------------------
print("Hello Simran\nWelcome to Python Lab")
# Output:
# Hello Simran
# Welcome to Python Lab

# -----------------------------
# \t -> Tab Space
# -----------------------------
print("Name:\tSimran")
print("Role:\tQA Engineer")
# Output:
# Name:   Simran
# Role:   QA Engineer

# -----------------------------
# \\ -> Backslash itself
# -----------------------------
print("Path Example: C:\\Users\\Simran\\Documents")
# Output:
# Path Example: C:\Users\Simran\Documents

# -----------------------------
# \' -> Single Quote inside Single Quotes
# -----------------------------
print('It\'s a wonderful day!')
# Output:
# It's a wonderful day!

# -----------------------------
# \" -> Double Quote inside Double Quotes
# -----------------------------
print("Simran said, \"Python is amazing!\"")
# Output:
# Simran said, "Python is amazing!"

# -----------------------------
# \b -> Backspace (removes previous character)
# -----------------------------
print("Helloo\b Python")
# Output:
# Hello Python

# -----------------------------
# \r -> Carriage Return (cursor moves to start of line)
# -----------------------------
print("Simran\rPython")
# Output (depends on terminal):
# Python

# -----------------------------
# \f -> Form Feed (page break — rarely used)
# -----------------------------
print("Line1\fLine2")
# Output:
# Line1
#      Line2  (new page or space depending on console)

# -----------------------------
# \ooo -> Octal value (rarely used)
# -----------------------------
print("This is an octal char: \110\145\154\154\157")
# Output:
# This is an octal char: Hello

# -----------------------------
# \xhh -> Hexadecimal value (rarely used)
# -----------------------------
print("Hex example: \x48\x65\x6C\x6C\x6F")
# Output:
# Hex example: Hello

# ============================================================
# Summary in Hindi 🇮🇳
# ------------------------------------------------------------
# \n -> नई लाइन में ले जाता है
# \t -> टैब स्पेस देता है
# \\ -> बैकस्लैश प्रिंट करता है
# \' , \" -> कोटेशन मार्क्स दिखाने में मदद करता है
# \b -> पिछले अक्षर को हटाता है
# \r -> लाइन की शुरुआत पर लौटाता है
# \f -> पेज ब्रेक या स्पेस बनाता है
# \ooo , \xhh -> अक्षरों के कोड वैल्यू दिखाने के लिए
# ============================================================

print("\n✅ All Escape Characters Demonstrated Successfully by Simran 🌸")
