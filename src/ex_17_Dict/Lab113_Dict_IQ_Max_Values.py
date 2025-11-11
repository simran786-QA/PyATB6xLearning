# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Dictionary Keys, Values & Finding Missing Keys
# -------------------------------------------------------------

# Step 1: Create the first dictionary
dict1 = {"a": 1, "b": 2, "c": 3}

# Hindi:
# Yahaan humne ek dictionary banayi hai jisme keys 'a', 'b', 'c' hain,
# aur unke corresponding values 1, 2, 3 hain.
#
# English:
# Here we created a dictionary with keys 'a', 'b', 'c'
# and values 1, 2, and 3 respectively.

# -------------------------------------------------------------
# Step 2: Display all keys and values
print(dict1.keys())     # Output: dict_keys(['a', 'b', 'c'])
print(dict1.values())   # Output: dict_values([1, 2, 3])

# Hindi:
# .keys() function hume sabhi keys dikhata hai.
# .values() function hume sabhi values dikhata hai.
#
# English:
# The .keys() method returns all the keys of the dictionary.
# The .values() method returns all the values of the dictionary.

# -------------------------------------------------------------
# Step 3: Create another dictionary for comparison
dict2 = {"a": 1, "b": 2}

# Hindi:
# Dusri dictionary me sirf do keys hain — 'a' aur 'b'.
# Hum check karenge ki dict1 me kaunsi keys hain jo dict2 me missing hain.
#
# English:
# The second dictionary contains only two keys — 'a' and 'b'.
# We’ll find out which keys from dict1 are missing in dict2.

# -------------------------------------------------------------
# Step 4: Find missing keys using set difference
missing_keys = set(dict1.keys() - dict2.keys())
print(missing_keys)     # Output: {'c'}

# Hindi:
# Jab hum (dict1.keys() - dict2.keys()) likhte hain,
# to Python dono key sets ka difference nikalta hai.
# Matlab: dict1 me jo keys hain, par dict2 me nahi hain.
#
# English:
# The expression (dict1.keys() - dict2.keys()) gives the set difference.
# It shows keys that exist in dict1 but not in dict2.

# -------------------------------------------------------------
# Step 5: Summary
# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"a": 1, "b": 2}
# Missing key = {'c'}

# Hindi:
# Iska output {'c'} hai kyunki sirf 'c' key dict1 me hai, dict2 me nahi.
#
# English:
# The result {'c'} means only the key 'c' is present in dict1 but not in dict2.
# -------------------------------------------------------------
