# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Find First Non-Repeating Character Using Sets in Python
# -------------------------------------------------------------

# Global set to store non-repeating characters
s = set()

# -------------------------------------------------------------
# Function: first_non_repeating(string)
# -------------------------------------------------------------
# Hindi:
# Yeh function string ke characters ko ek-ek karke check karta hai.
# Agar koi character sirf ek hi baar string me aata hai,
# to hum usse set me add karte hain aur return kar dete hain.
#
# English:
# This function checks each character in the string.
# If any character appears only once,
# we add it to the set and return it immediately.

def first_non_repeating(string):
    for char in string:
        if string.count(char) == 1:    # Character appears only once
            s.add(char)
            return char
    return None    # If no unique character exists


# -------------------------------------------------------------
# Step 1: Function Call and Output
# -------------------------------------------------------------
print(first_non_repeating("swiss"))  # Expected Output: w
print(s)

# Explanation:
# swiss
# s -> appears 3 times (skip)
# w -> appears 1 time → First non-repeating → returned
# i -> also 1 time, but comes after w → not considered first
# -------------------------------------------------------------
