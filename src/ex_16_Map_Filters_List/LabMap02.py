# -------------------------------------------------------------
# Step 1: List of Names
# -------------------------------------------------------------
# We have a list of names that we want to convert to uppercase.

name = ["simran", "shaikh", "qa", "simmi"]


# -------------------------------------------------------------
# Step 2: Function to convert string to uppercase
# -------------------------------------------------------------
# Returns the uppercase version of the given string.
# (Hindi: Yeh function string ko uppercase me convert karta hai.)

def upper_case(string):
    return string.upper()


# -------------------------------------------------------------
# Step 3: Apply map() to convert all names to uppercase
# -------------------------------------------------------------
# map() applies upper_case() to every item in the list.

upper_names = list(map(upper_case, name))


# -------------------------------------------------------------
# Step 4: Print the uppercase names
# -------------------------------------------------------------
# Expected Output: ['PRAMOD', 'DUTTA', 'QA', 'LUCKY']

print(upper_names)
