# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: OS Module – Working with Operating System
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Import os module
# -------------------------------------------------------------
# os module provides functions to interact with the operating system.

import os


# -------------------------------------------------------------
# Step 2: Print OS name
# -------------------------------------------------------------
# os.name tells which operating system is being used.

print(os.name)


# -------------------------------------------------------------
# Step 3: Get current working directory
# -------------------------------------------------------------
# os.getcwd() returns the current directory path.

print(os.getcwd())


# -------------------------------------------------------------
# Step 4: Create a directory (commented)
# -------------------------------------------------------------
# os.mkdir("AI") creates a new directory named "AI".
# Commented to avoid accidental folder creation.

# print(os.mkdir("AI"))


# -------------------------------------------------------------
# Step 5: List files and folders in current directory
# -------------------------------------------------------------
# os.listdir() shows all files and folders.

print(os.listdir())


# -------------------------------------------------------------
# Step 6: Remove and rename file (commented)
# -------------------------------------------------------------
# os.remove("AI.txt") deletes the file.
# os.rename("AI.txt", "testdata.txt") renames the file.

# print(os.remove("AI.txt"))
# print(os.rename("AI.txt","testdata.txt"))


# -------------------------------------------------------------
# Step 7: Access environment variables
# -------------------------------------------------------------
# os.environ.get("PATH") returns the PATH environment variable.

print(os.environ.get("PATH"))


# -------------------------------------------------------------
# Hindi Explanation:
# - os module system ke sath interaction ke liye use hota hai.
# - os.name se OS ka type pata chalta hai (nt / posix).
# - os.getcwd() current working directory batata hai.
# - os.listdir() current folder ke sab files/folders dikhata hai.
# - os.mkdir(), os.remove(), os.rename() file/folder operations ke liye hote hain.
# - os.environ.get("PATH") system ka PATH variable deta hai.
#
# English Explanation:
# - The os module is used to interact with the operating system.
# - os.name identifies the OS type.
# - os.getcwd() returns the current working directory.
# - os.listdir() lists files and folders.
# - mkdir, remove, rename handle file/folder operations.
# - os.environ.get("PATH") fetches environment variables.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. os module is used for OS-level operations.
# 2. It helps manage files, directories, and environment variables.
# 3. Commented commands prevent accidental changes.
# 4. Useful for automation and system scripts.
# -------------------------------------------------------------
