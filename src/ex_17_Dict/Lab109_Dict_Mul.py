# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Working with List of Dictionaries (Nested Dictionary Example)
# -------------------------------------------------------------

# Objective:
# Understand how to store multiple students' details using dictionaries inside a list,
# and how to access nested (inner) values using list index and dictionary keys.

# -------------------------------------------------------------
# Step 1: Create Dictionaries for Three Students

student_info1 = {
    "name": "Simran",
    # "age": 65,  # Commented line (Python ignores this)
    "age": 27,
    "address": {
        "home_address": "Pune",
        "office_address": "Mumbai"
    }
}

student_info2 = {
    "name": "Amit",
    "age": 29,
    "address": {
        "home_address": "Goa",
        "office_address": "Bangalore"
    }
}

student_info3 = {
    "name": "Murthy",
    "age": 35,
    "address": {
        "home_address": "Podili",
        "office_address": "Vizag"
    }
}

# Hindi:
# Yahaan humne 3 dictionary banayi hain — har ek ek student ki information store kar rahi hai.
# Har dictionary me "name", "age", aur ek nested dictionary "address" ke andar do address hain:
# home_address aur office_address.

# English:
# We created 3 dictionaries — each representing one student's information.
# Each dictionary includes "name", "age", and a nested dictionary under "address"
# containing both "home_address" and "office_address".

# -------------------------------------------------------------
# Step 2: Store All Dictionaries in a List

student_list = [student_info1, student_info2, student_info3]

# Hindi:
# Ab humne teeno dictionaries ko ek hi list ke andar daal diya hai.
# Isse hum ek hi variable (student_list) se sabhi students ko manage kar sakte hain.

# English:
# Now all student dictionaries are stored inside a list,
# allowing us to manage them together in a single variable.

# -------------------------------------------------------------
# Step 3: Print the Entire List

print(student_list)

# Hindi:
# Ye puri list print karega — jisme teeno students ka data ek saath dikhega.
# Lekin output thoda complex lagega kyunki nested structure hai.

# English:
# This prints the full list containing all 3 student dictionaries.
# The output may look complex due to nesting.

# Example Output:
# [
#   {'name': 'Simran', 'age': 27, 'address': {'home_address': 'Pune', 'office_address': 'Mumbai'}},
#   {'name': 'Amit', 'age': 29, 'address': {'home_address': 'Goa', 'office_address': 'Bangalore'}},
#   {'name': 'Murthy', 'age': 35, 'address': {'home_address': 'Podili', 'office_address': 'Vizag'}}
# ]

# -------------------------------------------------------------
# Step 4: Access a Specific Value (Nested Dictionary Access)

print(student_list[2]["address"]["office_address"])

# Hindi:
# `student_list[2]` ka matlab hai teesra student (Murthy).
# Uske andar se `["address"]["office_address"]` likhne se
# hum uska office address access kar sakte hain.
# Output hoga: Vizag

# English:
# `student_list[2]` means we’re accessing the 3rd student (Murthy).
# Then, `["address"]["office_address"]` gets the office address from the nested dictionary.
# Output: Vizag

# -------------------------------------------------------------
# Summary:
# ✅ List ke andar multiple dictionaries store kar sakte hain.
# ✅ Dictionary ke andar ek aur dictionary rakh sakte hain (Nested Dictionary).
# ✅ Access karne ke liye — list index + dictionary key ka use hota hai.
# ✅ Real automation testing ya API data parsing me ye pattern bahut common hai.
# -------------------------------------------------------------
