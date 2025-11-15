# -------------------------------------------------------------
# Step 1: List of Names
# -------------------------------------------------------------
# This list contains some empty strings that we want to remove.

names = ["QA", "", "Automation", "", "Tester"]


# -------------------------------------------------------------
# Step 2: Function to filter non-empty strings
# -------------------------------------------------------------
# Returns True only when the string is NOT empty.
# (Hindi: Sirf non-empty strings ko hi rakhna hai.)

def is_non_empty(x):
    return x != ""


# -------------------------------------------------------------
# Step 3: Use filter() to remove empty strings
# -------------------------------------------------------------
# filter() will keep only the non-empty values.

filtered_names = list(filter(is_non_empty, names))


# -------------------------------------------------------------
# Step 4: Print filtered list
# -------------------------------------------------------------
# Expected Output: ['QA', 'Automation', 'Tester']

print(filtered_names)
