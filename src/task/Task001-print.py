# =============================================
# COMPREHENSIVE PYTHON PRINT() FUNCTION GUIDE
# =============================================

print("=== BASIC PRINTING ===")
# Simple print
print("Hello World!")

# Multiple items
print("Apple", "Banana", "Cherry", "Date")

# Printing variables
name = "Alice"
age = 25
score = 95.5
is_student = True
print("Name:", name, "Age:", age, "Score:", score, "Student:", is_student)

print("\n" + "="*50)
print("=== CUSTOM SEPARATORS (sep parameter) ===")

# Different separator examples
print("Python", "Java", "C++", sep=" | ")           # Output: Python | Java | C++
print("2024", "05", "20", sep="-")                  # Output: 2024-05-20
print("Red", "Green", "Blue", sep=" + ")            # Output: Red + Green + Blue
print(1, 2, 3, 4, sep='')                           # Output: 1234
print("Pramod", 123, "Amit", "John", sep='*')       # Output: Pramod*123*Amit*John

print("\n" + "="*50)
print("=== CUSTOM ENDINGS (end parameter) ===")

# Default behavior (newline)
print("Line 1")
print("Line 2")

# Custom end characters
print("Hello", end=" ")
print("World!")                                      # Output: Hello World!

print("Loading", end="...")
print("Complete")                                    # Output: Loading...Complete

print("This is", end="")
print("connected")                                   # Output: This isconnected

print("Item", end=" -> ")
print("Price")                                       # Output: Item -> Price

# Combined sep and end
print("Python", "Java", "C++", sep=", ", end=" - Programming Languages\n")

print("\n" + "="*50)
print("=== STRING FORMATTING METHODS ===")

name = "John"
age = 30
salary = 50000.75

# 1. f-strings (Python 3.6+)
print(f"My name is {name} and I'm {age} years old")
print(f"Salary: ${salary:,.2f}")
print(f"Next year I'll be {age + 1}")

# 2. .format() method
print("My name is {} and I'm {} years old".format(name, age))
print("Name: {1}, Age: {0}".format(age, name))  # Positional
print("Salary: ${:,.2f}".format(salary))

# 3. % formatting (older style)
print("My name is %s and I'm %d years old" % (name, age))
print("Salary: $%.2f" % salary)

print("\n" + "="*50)
print("=== SPECIAL CHARACTERS & ESCAPE SEQUENCES ===")

# Newline
print("Line 1\nLine 2\nLine 3")

# Tab
print("Name:\tJohn\nAge:\t25\nCity:\tNYC")

# Backslash and quotes
print("Path: C:\\Users\\John\\Documents")
print('He said, "Hello World!"')
print("It's a beautiful day")
print('She said, \"It\'s amazing!\"')

# Raw strings
print(r"C:\Users\John\new_folder")  # Doesn't interpret escape sequences

print("\n" + "="*50)
print("=== PRINTING DIFFERENT DATA TYPES ===")

# Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
print("Fruits list:", fruits)
print("Numbers:", numbers)

# Dictionaries
person = {"name": "Bob", "age": 30, "city": "Boston"}
print("Person details:", person)

# Tuples
coordinates = (10, 20, 30)
print("Coordinates:", coordinates)

print("\n" + "="*50)
print("=== ADVANCED PRINTING TECHNIQUES ===")

# Table-like formatting
print(f"{'NAME':<10} {'AGE':<5} {'CITY':<10} {'SALARY':>10}")
print(f"{'John':<10} {25:<5} {'NYC':<10} ${50000:>9,}")
print(f"{'Alice':<10} {30:<5} {'Boston':<10} ${75000:>9,}")
print(f"{'Bob':<10} {28:<5} {'Chicago':<10} ${62000:>9,}")

# Progress indicator
import time
print("Downloading", end="")
for i in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(" Complete!")

# Mathematical operations in print
a, b = 15, 7
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b:.2f}")

print("\n" + "="*50)
print("=== FILE OUTPUT ===")

# Writing to a file
with open("output.txt", "w") as file:
    print("This line goes to the file", file=file)
    print("Name: John Doe", file=file)
    print("Age: 30", file=file)

print("Data written to output.txt")

# Appending to file
with open("output.txt", "a") as file:
    print("\nAppended line", file=file)

print("Data appended to output.txt")

print("\n" + "="*50)
print("=== COMBINING ALL FEATURES ===")

# Complex example combining everything
students = [
    {"name": "Alice", "scores": [85, 92, 78]},
    {"name": "Bob", "scores": [76, 88, 94]},
    {"name": "Charlie", "scores": [90, 85, 92]}
]

print("STUDENT REPORT", end="\n" + "="*20 + "\n")
for student in students:
    avg_score = sum(student["scores"]) / len(student["scores"])
    print(f"Name: {student['name']:8} | "
          f"Scores: {student['scores']} | "
          f"Average: {avg_score:6.2f}")

print("\n" + "="*50)
print("=== FINAL COMBINED EXAMPLE ===")

# The original example from the question with explanation
print("Original Example: ", end="")
print("Pramod", 123, "Amit", "John", sep='*', end="_")
print(" ← This uses sep='*' and end='_'")

print("\n" + "="*50)
print("=== FLUSH PARAMETER DEMONSTRATION ===")

# Flush example - forces immediate output
print("This appears immediately", flush=True)

print("Countdown:", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
print("Go!", flush=True)

print("\n" + "="*50)
print("=== MULTI-LINE STRINGS ===")

# Multi-line printing
multi_line = """
This is a multi-line string
Line 2
Line 3
    Indented line
"""
print(multi_line)

# Alternative multi-line
print("""Choose an option:
1. Login
2. Register
3. Exit
""")

print("="*50)
print("END OF PRINT FUNCTION DEMONSTRATION")