# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Remove Duplicate Values from a Dictionary
# -------------------------------------------------------------

# Step 1: Create a dictionary with some duplicate values
my_dict = {"a": 1, "b": 2, "c": 1, "d": 3}
# Expected Output: {'a': 1, 'b': 2, 'd': 3}

# Hindi:
# Yahaan humne ek dictionary banayi hai jisme kuch values repeat ho rahi hain.
# Jaise value '1' do keys ('a' aur 'c') ke saath aayi hai.
#
# English:
# Here we have a dictionary that contains duplicate values.
# For example, value '1' appears with both keys 'a' and 'c'.

# -------------------------------------------------------------
# Step 2: Initialize a set to store unique values
unique_value = set()
result = {}

# Hindi:
# Hum ek empty set bana rahe hain jisme hum unique (alag-alag) values store karenge.
# Ek empty dictionary 'result' bhi banai hai jisme final filtered data aayega.
#
# English:
# We create an empty set to keep track of unique values.
# We also create an empty dictionary 'result' to store the final output.

# -------------------------------------------------------------
# Step 3: Iterate through the original dictionary
for key, value in my_dict.items():
    # If the value is not already in the set, add it and keep that key-value pair
    if value not in unique_value:
        result[key] = value
        unique_value.add(value)

# Hindi:
# Har key-value pair ke liye hum check karte hain ki kya value pahle se set me hai.
# Agar nahi hai, to us value ko set me add karte hain aur dictionary me store karte hain.
# Agar value repeat hai, to usse ignore kar dete hain.
#
# English:
# For each key-value pair, we check if the value already exists in the set.
# If not, we add it to the set and include that pair in the result dictionary.
# If it’s already there, we skip it.

# -------------------------------------------------------------
# Step 4: Print the final dictionary without duplicate values
print(result)  # Output: {'a': 1, 'b': 2, 'd': 3}

# Hindi:
# Output me sirf unique values ke corresponding keys hi aayengi.
# Yahaan 'c':1 remove ho gaya kyunki '1' pahle hi 'a' ke saath aa chuka tha.
#
# English:
# The output will only show keys with unique values.
# Here, 'c':1 is removed because value 1 already appeared with key 'a'.
# -------------------------------------------------------------
