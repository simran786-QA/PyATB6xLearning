# -------------------------------------------------------------
# Step 1: Import Time Module
# -------------------------------------------------------------
import time


# -------------------------------------------------------------
# Step 2: Use Time Functions
# -------------------------------------------------------------
# Print current timestamp (seconds since 1970)
print(time.time())

# Sleep the program for 4 seconds
print(time.sleep(4))  # Returns None after pause

# Fetch current local time (hour & minute)
print(time.localtime().tm_hour)
print(time.localtime().tm_min)

# Another sleep for 4 seconds
time.sleep(4)   # Halts the program again for 4 seconds
