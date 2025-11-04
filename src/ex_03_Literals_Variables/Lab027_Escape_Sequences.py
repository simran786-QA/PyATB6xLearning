# -------------------------------------------------------------
# 🧠 Lab027_Escape_Sequences.py
# Author: Simran Shaikh
# Topic: Escape Sequences in Python Strings
# -------------------------------------------------------------

# 🎯 Objective:
# Learn how special characters (escape sequences) are used inside strings
# to format text and add special behaviors like new lines, tabs, etc.
# -------------------------------------------------------------

print("🔹 Welcome to Simran’s Escape Sequence Demonstration 🔹\n")

# -------------------------------------------------------------
# 1️⃣ \n → New Line
# Moves text to the next line
print("Example 1: Using \\n (New Line)")
print("Hello\nWorld")  # Output in two lines
print("--------------------------")

# -------------------------------------------------------------
# 2️⃣ \t → Tab Space
# Adds a horizontal tab (like pressing the Tab key once)
print("Example 2: Using \\t (Tab Space)")
print("Hello\tWorld")
print("Name\t\tAge\tCity")   # Perfect for table-style output
print("Simran\t24\tPune")
print("--------------------------")

# -------------------------------------------------------------
# 3️⃣ \b → Backspace
# Removes (or overwrites) one character before it
print("Example 3: Using \\b (Backspace)")
print("Hello\bWorld")  # Removes 'o'
print("Data\bScience")  # Removes 'a'
print("--------------------------")

# -------------------------------------------------------------
# 4️⃣ \\ → Prints a backslash itself
# Because a single '\' is treated as an escape character
print("Example 4: Using \\\\ (Backslash)")
print("This is a backslash: \\")
print("--------------------------")

# -------------------------------------------------------------
# 5️⃣ \' and \" → Include quotes inside strings
# Helps when your string already uses the same type of quote
print("Example 5: Using \\' and \\\" (Quotes)")
print('She said: \'Python is amazing!\'')
print("He replied: \"Yes, absolutely!\"")
print("--------------------------")

# -------------------------------------------------------------
# 6️⃣ \r → Carriage Return (moves cursor to line start)
# The text after \r overwrites from the beginning
print("Example 6: Using \\r (Carriage Return)")
print("Hello World\rHi")  # 'Hi' overwrites 'He'
print("--------------------------")

# -------------------------------------------------------------
# 7️⃣ \f → Form Feed (rarely used)
# Moves to next "page" in text printers (not much visible in consoles)
print("Example 7: Using \\f (Form Feed)")
print("Python\fProgramming")
print("--------------------------")

# -------------------------------------------------------------
# 8️⃣ Real-World Example — Neatly formatted output
print("Example 8: Real-World Usage\n")
print("Name\tSubject\tMarks")
print("Simran\tMaths\t95")
print("Aisha\tScience\t90")
print("John\tEnglish\t88")

# -------------------------------------------------------------
# ✅ End of Program
print("\n✅ Program executed successfully by Simran Shaikh.")
