# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Dictionary in Python – Key, Value, Access, and Update
# -------------------------------------------------------------

# Objective:
# Learn how to create, access, and modify a dictionary in Python.
# Understand how dictionaries store data as key-value pairs.

# -------------------------------------------------------------
# Step 1: Create a Dictionary
student_info = {
    "name": "Simran",
    # "age": 25,   # Yeh comment line hai – Python isse ignore karega
    "age": 27,
    "address": "Mumbai"
}

# Hindi Explanation:
# Yahaan humne ek dictionary banayi hai jisme 3 key-value pairs hain:
# "name" → "Simran"
# "age" → 27
# "address" → "Mumbai"
# Commented line ka koi effect nahi hota.

# English Explanation:
# We have created a dictionary named `student_info` with three keys:
# name, age, and address.
# The commented line is ignored by Python.

# -------------------------------------------------------------
# Step 2: Print the Whole Dictionary
print(student_info)

# Hindi:
# Yeh poori dictionary ko print karega.
# Output: {'name': 'Simran', 'age': 27, 'address': 'Mumbai'}

# English:
# Prints all key-value pairs together.

# -------------------------------------------------------------
# Step 3: Access Individual Values using Keys
print(student_info["name"])
print(student_info["age"])
print(student_info["address"])

# Hindi:
# Hum har key ka value square brackets ke andar likhkar access kar sakte hain.
# Example: student_info["name"] → 'Simran'

# English:
# Each value can be accessed by using its key inside brackets [].

# -------------------------------------------------------------
# Step 4: Update an Existing Key’s Value
student_info["age"] = 30
print(student_info)

# Hindi:
# Yeh line "age" key ka value update karegi (27 → 30)
# Dictionary mutable hoti hai, isliye hum values badal sakte hain.

# English:
# Updates the value of "age" to 30.
# Dictionaries are mutable, so their contents can be changed.

# -------------------------------------------------------------
# Final Output:
# {'name': 'Simran', 'age': 27, 'address': 'Mumbai'}
# Simran
# 27
# Mumbai
# {'name': 'Simran', 'age': 30, 'address': 'Mumbai'}

# -------------------------------------------------------------
# Summary:
# - Dictionary stores data in key-value format.
# - You can access data using keys.
# - You can modify existing values.
# - Dictionaries are mutable and very useful for structured data.
# -------------------------------------------------------------
