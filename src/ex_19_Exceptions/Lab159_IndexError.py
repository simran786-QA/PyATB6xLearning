# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Error Handling – IndexError (List index out of range)
# -------------------------------------------------------------

# Step 1: Create a simple list
my_list = [1, 2, 3]

# Step 2: Try accessing an index that does NOT exist
# -------------------------------------------------------------
# Uncomment to see the error:
# print(my_list[4])

# Expected Error:
# IndexError: list index out of range

# -------------------------------------------------------------
# Hindi Explanation:
# - List me sirf 3 elements hai: index 0, 1, 2.
# - Python me indexing 0 se start hoti hai.
# - Jab hum my_list[4] access karte hain, wo index exist nahi karta.
# - Isliye Python IndexError deta hai.

# English Explanation:
# - The list has only 3 elements at index positions 0, 1, and 2.
# - Python starts counting from 0.
# - my_list[4] tries to access the 5th element which does not exist.
# - Therefore, Python throws IndexError.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. IndexError occurs when you try to access an invalid index.
# 2. List length = 3 → valid indexes are 0, 1, 2.
# 3. Accessing my_list[4] is out of range → causes IndexError.
# 4. Always check list length before accessing indexes.
# -------------------------------------------------------------
