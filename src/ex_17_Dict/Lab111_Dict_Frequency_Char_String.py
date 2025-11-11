# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Frequency of Characters in a String
# -------------------------------------------------------------

# Step 1: Take input from user
string = input("\nEnter the input e.g automation\n")

# Hindi:
# Yahan hum user se ek string input le rahe hain, jaise "automation".
# Hum har character ki frequency (kitni baar aaya hai) count karenge.
#
# English:
# Here, we take a string input from the user (e.g., "automation").
# We will count how many times each character appears in that string.

# Example Input:
# automation
# Expected Output:
# {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}

# -------------------------------------------------------------
# Step 2: Create an empty dictionary to store counts
char_count = {}

# Step 3: Loop through each character in the string
for char in string:
    char_count[char] = char_count.get(char, 0) + 1

# Hindi:
# Har character ke liye hum dictionary me entry check karte hain.
# Agar character pehli baar mil raha hai to get(char, 0) 0 return karega.
# Fir usme +1 kar ke count badhaya jaata hai.
#
# English:
# For each character in the string, we check if it already exists in the dictionary.
# If not, get(char, 0) returns 0 by default.
# Then we add 1 to increase the count.

# Example Working for "automation":
# Step-by-step dictionary update:
# {'a': 1}
# {'a': 1, 'u': 1}
# {'a': 1, 'u': 1, 't': 1}
# {'a': 1, 'u': 1, 't': 1, 'o': 1}
# {'a': 1, 'u': 1, 't': 1, 'o': 1, 'm': 1}
# {'a': 1, 'u': 1, 't': 1, 'o': 1, 'm': 1, 'a': 2} → 'a' already present, count +1
# {'a': 2, 'u': 1, 't': 1, 'o': 1, 'm': 1, 'i': 1}
# {'a': 2, 'u': 1, 't': 2, 'o': 1, 'm': 1, 'i': 1}
# {'a': 2, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'i': 1, 'n': 1}

# -------------------------------------------------------------
# Step 4: Print the final frequency dictionary
print(char_count)

# Hindi:
# Ant me, hum dictionary print karte hain jisme har character ka count hota hai.
#
# English:
# Finally, we print the dictionary that contains the frequency of each character.

# -------------------------------------------------------------
# Summary:
# ✅ Input: User-entered string (e.g. automation)
# ✅ Output: Dictionary showing character frequency
# ✅ Used: get() method to simplify counting logic
# ✅ Practical Use: Helpful in text analysis, log processing, and QA validations
# -------------------------------------------------------------

