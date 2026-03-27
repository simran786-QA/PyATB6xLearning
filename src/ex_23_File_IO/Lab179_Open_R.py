# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: File Handling – FileNotFoundError Exception Handling
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Try to open and read a file
# -------------------------------------------------------------
# 'with open' automatically handles file closing

try:
    with open('testdata.txt', 'r') as file:
        content = file.read()   # Reads full file content

    # Alternative:
    # content = file.readlines()  # Reads file line-by-line as list

        print(content)

# -------------------------------------------------------------
# Step 2: Handle exception if file not found
# -------------------------------------------------------------
# If file does not exist, FileNotFoundError will occur

except FileNotFoundError as fnfe:
    print("Error:", fnfe)