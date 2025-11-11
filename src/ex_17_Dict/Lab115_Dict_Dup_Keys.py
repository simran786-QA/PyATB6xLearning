# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Duplicate Keys in Dictionary & Removing Duplicates from a List
# -------------------------------------------------------------

# Step 1: Dictionary with duplicate keys
p = {"name": "Pramod", "name": "Amit"}
print(p)

# Hindi:
# Yahaan humne ek dictionary banayi hai jisme same key "name" do baar likhi gayi hai.
# Lekin Python me dictionary ke andar keys UNIQUE hoti hain.
# Isliye, jab same key repeat hoti hai, to last wali value purani ko replace kar deti hai.
#
# English:
# Here we created a dictionary where the same key "name" appears twice.
# In Python, dictionary keys must be unique.
# So, when the same key is repeated, the last value overwrites the previous one.

# Output:
# {'name': 'Amit'}

# -------------------------------------------------------------
# Step 2: List with duplicate elements
my_list = [1, 2, 2, 3, 4, 4, 5]

# Hindi:
# Yahaan ek list banayi gayi hai jisme kuch values repeat ho rahi hain.
# Hum is list se duplicates remove karenge.
#
# English:
# This list contains duplicate numbers.
# We'll remove duplicates from it.

# -------------------------------------------------------------
# Step 3: Remove duplicates using 'set'
unique_list = list(set(my_list))
print(unique_list)

# Hindi:
# 'set()' automatically remove kar deta hai duplicates ko,
# lekin order (sequence) maintain nahi karta.
#
# English:
# Using 'set()', duplicates are automatically removed,
# but it does NOT preserve the original order of elements.

# Output Example:
# [1, 2, 3, 4, 5]

# -------------------------------------------------------------
# Step 4: Remove duplicates while preserving order (optional)
unique_ordered_list = []
for item in my_list:
    if item not in unique_ordered_list:
        unique_ordered_list.append(item)

print(unique_ordered_list)

# Hindi:
# Agar aapko original order maintain karna hai,
# to aise loop ka use karke manually duplicates hata sakte hain.
#
# English:
# If you want to keep the original order of the elements,
# you can remove duplicates manually using a loop.

# Output:
# [1, 2, 3, 4, 5]
# -------------------------------------------------------------
