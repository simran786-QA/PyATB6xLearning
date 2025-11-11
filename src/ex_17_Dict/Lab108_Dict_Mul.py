# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: List of Dictionaries in Python (Nested Dictionary Example)
# -------------------------------------------------------------

# Objective:
# Understand how to store multiple dictionaries inside a list,
# and how to access nested values using indexing and keys.

# -------------------------------------------------------------
# Step 1: Create Two Student Dictionaries

student_info1 = {
    "name": "Simran",
    # "age": 25,   # Yeh comment line hai (Python ignore karega)
    "age": 27,
    "address": {
        "home_address": "Pune",
        "office_address": "Mumbai"
    }
}

student_info2 = {
    "name": "Amit",
    # "age": 65,   # Ignored line
    "age": 29,
    "address": {
        "home_address": "Goa",
        "office_address": "Bangalore"
    }
}

# Hindi Explanation:
# Humne do dictionary banayi hain — `student_info1` aur `student_info2`
# Har ek dictionary ke andar ek aur dictionary hai (`address` key ke andar)
# Jise hum "Nested Dictionary" bolte hain.

# English Explanation:
# Two student dictionaries are created.
# Each has a nested dictionary under the key `address`
# containing both `home_address` and `office_address`.

# -------------------------------------------------------------
# Step 2: Store Both Dictionaries in a List

student_list = [student_info1, student_info2]

# Hindi:
# Dono students ko ek list ke andar store kiya gaya hai.
# List ke andar multiple dictionaries ho sakti hain.

# English:
# Both dictionaries are stored in a list.
# A list can hold multiple dictionaries.

# -------------------------------------------------------------
# Step 3: Print the Entire List
print(student_list)

# Output Example:
# [{'name': 'Simran', 'age': 27, 'address': {'home_address': 'Pune', 'office_address': 'Mumbai'}},
#  {'name': 'Amit', 'age': 29, 'address': {'home_address': 'Goa', 'office_address': 'Bangalore'}}]

# -------------------------------------------------------------
# Step 4: Access the First Dictionary
print(student_list[0])

# Hindi:
# student_list[0] ka matlab hai — pehli dictionary ko access karna.
# (List indexing 0 se start hoti hai)

# English:
# Accessing the first dictionary in the list using index 0.

# -------------------------------------------------------------
# Step 5: Access a Specific Value from the First Dictionary
print(student_list[0]["name"])

# Hindi:
# Yeh pehli dictionary ke "name" key ka value print karega.
# Output: Simran

# English:
# Prints the value of the key "name" in the first dictionary.

# -------------------------------------------------------------
# Step 6: Access a Nested Dictionary Value
print(student_list[0]["address"]["office_address"])

# Hindi:
# Pehle student ke andar ek nested dictionary hai jiska key hai "address".
# Uske andar se "office_address" ka value nikaalne ke liye:
# student_list[0]["address"]["office_address"]

# Output: Mumbai

# English:
# Accessing a nested value by chaining keys and indices.
# It prints the office address of the first student.

# -------------------------------------------------------------
# Summary:
# ✅ Dictionaries can store key-value pairs.
# ✅ Lists can hold multiple dictionaries.
# ✅ You can access nested values using index + key.
# ✅ This structure is very useful for representing JSON-like data.

# -------------------------------------------------------------
