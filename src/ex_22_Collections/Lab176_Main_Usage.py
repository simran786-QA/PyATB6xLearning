# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Entry Point – Multiple Function Execution
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Define functions
# -------------------------------------------------------------
# These are simple functions that print their names.

def f1():
    print("f1")

def f2():
    print("f2")

def f3():
    print("f3")


# -------------------------------------------------------------
# Step 2: Define main function
# -------------------------------------------------------------
# main() acts as the central execution point.

def main():
    print("main from 176")


# -------------------------------------------------------------
# Step 3: Entry point check
# -------------------------------------------------------------
# This ensures the code runs only when the file is executed directly.

if __name__ == "__main__":
    main()
    f1()
    f2()
    f3()


# -------------------------------------------------------------
# Hindi Explanation:
# - f1(), f2(), f3() alag-alag functions hain jo print karte hain.
# - main() primary function hai jo pehle call hota hai.
# - __name__ == "__main__" check karta hai ki file direct run ho rahi hai ya nahi.
# - Agar direct run hui, to main(), f1(), f2(), f3() sequentially execute honge.
#
# English Explanation:
# - f1(), f2(), and f3() are simple functions.
# - main() is the primary execution function.
# - The __name__ == "__main__" block runs only when executed directly.
# - Functions execute sequentially in the given order.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Multiple functions can be called from the entry point.
# 2. main() helps organize program flow.
# 3. __name__ check prevents unwanted execution during import.
# 4. Execution order follows top-to-bottom inside the block.
# -------------------------------------------------------------
