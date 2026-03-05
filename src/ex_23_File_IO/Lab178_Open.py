# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: File Handling – File Modes and Context Manager
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Different file opening modes (commented examples)
# -------------------------------------------------------------
# 'r'  -> Read mode (file must exist)
# 'w'  -> Write mode (creates new file or overwrites existing)
# 'r+' -> Read and write mode
# 'w+' -> Write and read mode (overwrites file)
# 'b'  -> Binary mode

# t = open('testdata.txt', 'r')
# t = open('testdata.txt', 'w')
# t = open('testdata.txt', 'r+')
# t = open('testdata.txt', 'w+')
# t = open('testdata.txt', 'b')
# t.close()


# -------------------------------------------------------------
# Step 2: Using context manager (with statement)
# -------------------------------------------------------------
# with automatically closes the file after execution.

with open('testdata.txt', 'r') as f:
    data = f.read()


# -------------------------------------------------------------
# Step 3: Print file content
# -------------------------------------------------------------
# The content read from the file is printed.

print(data)


# -------------------------------------------------------------
# Hindi Explanation:
# - open() function file ko different modes me open karta hai.
# - r = read mode, w = write mode, r+ = read/write.
# - w+ file ko overwrite kar deta hai.
# - with statement context manager use karta hai.
# - with block khatam hone par file automatically close ho jati hai.
#
# English Explanation:
# - open() opens a file using different modes.
# - r = read, w = write, r+ = read/write.
# - w+ overwrites the file.
# - with statement uses a context manager.
# - The file automatically closes after the block finishes.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. Files can be opened in multiple modes.
# 2. Manual close() is required when using open().
# 3. with statement automatically closes files.
# 4. read() fetches the entire file content.
# -------------------------------------------------------------