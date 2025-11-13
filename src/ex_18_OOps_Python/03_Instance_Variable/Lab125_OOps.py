# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Global Keyword and Function Scope in Python
# -------------------------------------------------------------

# Step 1: Define a Global Variable
count = 0

# Hindi:
# Yeh global variable hai — program ke kisi bhi function ke bahar declare kiya gaya hai.
# English:
# This is a global variable — declared outside any function, accessible throughout the program.

# -------------------------------------------------------------
# Step 2: Define a Function to Increment the Count
def increment():
    global count  # Declare that we want to use the global 'count' variable
    count = count + 1

# Hindi:
# 'global count' likhne ka matlab hai hum function ke andar ek nayi local copy nahi,
# balki bahar wale (global) variable ko modify kar rahe hain.
#
# English:
# Using 'global count' tells Python that we’re modifying the existing global variable,
# not creating a new local one.

# -------------------------------------------------------------
# Step 3: Call the Function Multiple Times
increment()
increment()
increment()

# -------------------------------------------------------------
# Step 4: Print Final Value of count
print(count)  # Output: 3

# Hindi:
# Humne increment() teen baar call kiya, isliye count ki value 0 se badh kar 3 ho gayi.
#
# English:
# Since we called increment() three times, the global variable count increased from 0 to 3.
# -------------------------------------------------------------
