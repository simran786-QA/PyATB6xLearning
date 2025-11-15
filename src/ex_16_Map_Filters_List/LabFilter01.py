# -------------------------------------------------------------
# Step 1: List of Numbers
# -------------------------------------------------------------
# Hindi:
# Yahan humne ek list banayi hai jisme 1 se 6 tak numbers hain.
#
# English:
# Here we created a list containing numbers from 1 to 6.

nums = [1, 2, 3, 4, 5, 6]


# -------------------------------------------------------------
# Step 2: Define function to check even numbers
# -------------------------------------------------------------
# Hindi:
# even_num function check karta hai ki number even hai ya nahi.
# Agar number even hai to True return karega, warna False.
#
# English:
# even_num function checks if a number is even.
# If number is even, it returns True, otherwise False.

def even_num(x):
    return x % 2 == 0


# -------------------------------------------------------------
# Step 3: Use filter() to extract even numbers
# -------------------------------------------------------------
# Hindi:
# filter() unhi values ko rakhta hai jinke liye function True return kare.
# Yahan humne even numbers ko filter kiya hai.
#
# English:
# filter() keeps only values for which the function returns True.
# Here we are filtering even numbers.

print_even_numbers = list(filter(even_num, nums))
print(print_even_numbers)    # Output: [2, 4, 6]


# -------------------------------------------------------------
# Step 4: Student marks list
# -------------------------------------------------------------
# Hindi:
# Yahan students ke marks diye gaye hain.
#
# English:
# Here we have a list of student marks.

list_student = [50, 51, 100]


# -------------------------------------------------------------
# Step 5: Define function to keep marks greater than 50
# -------------------------------------------------------------
# Hindi:
# keep() function sirf tab True return karta hai jab marks > 50 ho.
#
# English:
# keep() function returns True only when marks > 50.

def keep(x):
    if x > 50:
        return True


# -------------------------------------------------------------
# Step 6: Use filter() to get students scoring above 50
# -------------------------------------------------------------
# Hindi:
# filter() unhi students ko return karega jinke marks 50 se zyada honge.
#
# English:
# filter() returns only the students who scored more than 50.

all_student = list(filter(keep, list_student))
print(all_student)   # Output: [51, 100]
