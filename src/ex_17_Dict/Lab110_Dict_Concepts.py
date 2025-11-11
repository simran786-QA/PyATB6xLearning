# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Dictionary Creation using zip() and Dictionary Merging
# -------------------------------------------------------------

# Step 1: Create a dictionary using zip()

keys = ["name", "role", "experience", "abc"]
values = ["Aman", "SDET", 3]

my_dict = dict(zip(keys, values))
print(my_dict)

# Hindi:
# Yahaan humne do lists banayi hain: 'keys' aur 'values'.
# 'zip(keys, values)' dono lists ke elements ko pair karta hai jaise:
# ("name", "Aman"), ("role", "SDET"), ("experience", 3)
# Phir 'dict()' in pairs ko dictionary me convert karta hai.

# Important:
# Agar keys list lambi hai aur values kam hain,
# to zip() sirf common pairs tak hi dictionary banata hai.
# Yahaan 'abc' ka koi value nahi hai, isliye wo include nahi hua.

# English:
# We have two lists: 'keys' and 'values'.
# 'zip(keys, values)' pairs elements from both lists like:
# ("name", "Aman"), ("role", "SDET"), ("experience", 3)
# The 'dict()' function then converts these pairs into a dictionary.
#
# Note:
# If the keys list is longer than the values list,
# zip() will only create pairs up to the shortest list length.
# Hence, "abc" won’t appear in the final dictionary.

# Output Example:
# {'name': 'Aman', 'role': 'SDET', 'experience': 3}

# -------------------------------------------------------------
# Step 2: Merge Two Dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2
print(merged_dict)

# Hindi:
# Python 3.9 se hum dictionaries ko merge karne ke liye '|' (pipe) operator ka use kar sakte hain.
# Yahan dict1 aur dict2 merge hokar ek nayi dictionary banate hain.
# Agar dono me same key hoti, to right side (dict2) wali value overwrite karti.

# English:
# In Python 3.9 and above, we can merge two dictionaries using the '|' operator.
# dict1 and dict2 are combined into a new dictionary.
# If both dictionaries have the same key, the value from the right-side dictionary (dict2) will overwrite the left one.

# Output Example:
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# -------------------------------------------------------------
# Step 3: Accessing Value from Dictionary

print(merged_dict.get("a"))

# Hindi:
# 'get()' method dictionary se value fetch karta hai.
# Agar key exist nahi karti, to ye 'None' return karega — koi error nahi aayega.

# English:
# The 'get()' method retrieves the value for a given key.
# If the key doesn’t exist, it returns 'None' instead of raising an error.

# Output:
# 1

# -------------------------------------------------------------
# Summary:
# ✅ dict(zip(keys, values)) — Converts paired lists into a dictionary
# ✅ dict1 | dict2 — Merges two dictionaries (Python 3.9+)
# ✅ get(key) — Safely accesses dictionary values without errors
# -------------------------------------------------------------
