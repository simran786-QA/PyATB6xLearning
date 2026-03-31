# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: File Handling – Append Mode ('a')
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Open file in append mode
# -------------------------------------------------------------
# 'a' mode adds data at the end of the file (creates file if not exists)

with open('TestData.txt', 'a') as file:

    # ---------------------------------------------------------
    # Step 2: Write data into file
    # ---------------------------------------------------------
    file.write("Hello How are you")

# -------------------------------------------------------------
# Note:
# File will automatically close due to 'with' statement
# -------------------------------------------------------------