# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Count Vowels in a String
# -------------------------------------------------------------

# Step 1: Input String
input_string = "hello, world!"

# Hindi:
# Hum ek string le rahe hain — "hello, world!"
# Ab hume isme kitne vowels (a, e, i, o, u) hain, ye count karna hai.
#
# English:
# We are taking a string "hello, world!"
# We’ll count how many vowels (a, e, i, o, u) are present in it.

# -------------------------------------------------------------
# Step 2: Define vowels
vowels = "aeiou"

# Hindi:
# Humne ek string banayi hai jisme saare vowels hain.
# Iska use hum comparison ke liye karenge.
#
# English:
# We define a string containing all vowels.
# This will help us check if each character is a vowel or not.

# -------------------------------------------------------------
# Step 3: Initialize variables
vowels_count = 0     # to count number of vowels
result = list()      # to store vowels found in the string

# -------------------------------------------------------------
# Step 4: Loop through each character in the string
for char in input_string:
    if char in vowels:                  # check if character is a vowel
        vowels_count = vowels_count + 1 # increase the count
        result.append(char)             # store the vowel in result list

# Hindi:
# Loop ke andar hum har character check karte hain.
# Agar wo vowel hai, to usse count badha dete hain aur list me store karte hain.
#
# English:
# Inside the loop, we check each character.
# If it’s a vowel, we increase the count and add it to the list.

# -------------------------------------------------------------
# Step 5: Print Results
print(vowels_count)
print(result)

# Output:
# 3
# ['e', 'o', 'o']

# Hindi:
# Iska matlab string me total 3 vowels hain: 'e', 'o', aur 'o'.
#
# English:
# This means the string contains 3 vowels: 'e', 'o', and 'o'.
# -------------------------------------------------------------
