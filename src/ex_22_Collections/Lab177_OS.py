# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: File Handling with OS Module – Absolute Path Reading
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Import os module
# -------------------------------------------------------------
# os module helps in creating platform-independent file paths.

import os


# -------------------------------------------------------------
# Step 2: Get current working directory
# -------------------------------------------------------------
# os.getcwd() returns the directory from where the script runs.

print(os.getcwd())


# -------------------------------------------------------------
# Step 3: Create full file path
# -------------------------------------------------------------
# os.path.join() safely combines folder path and file name.

full_path = os.path.join(os.getcwd(), "pramod.txt")

# Example of hardcoded absolute path (commented).
# full_path = os.path.join("/Users/promode/PycharmProjects/PyATB6xLearning/src/ex_22_Collections","pramod.txt")

print(full_path)


# -------------------------------------------------------------
# Step 4: Open and read the file
# -------------------------------------------------------------
# File is opened in read mode ('r') and content is printed.

file = open(full_path, 'r')
print(file.read())


# -------------------------------------------------------------
# Hindi Explanation:
# - os.getcwd() current folder ka path deta hai.
# - os.path.join() file path ko safe tarike se combine karta hai.
# - full_path me pramod.txt ka complete path store hota hai.
# - open(full_path, 'r') file ko read mode me open karta hai.
# - file.read() pura content print karta hai.
#
# English Explanation:
# - os.getcwd() gives the current working directory.
# - os.path.join() builds a safe absolute file path.
# - full_path stores the complete path of pramod.txt.
# - open(...,'r') opens the file in read mode.
# - file.read() prints the file content.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. os.path.join() avoids OS-specific path issues.
# 2. Absolute paths improve reliability.
# 3. File is opened in read mode to fetch content.
# 4. Useful for automation scripts and file processing.
# -------------------------------------------------------------
