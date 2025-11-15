# -------------------------------------------------------------
# Step 1: List of Response Times (in milliseconds)
# -------------------------------------------------------------
# We have response times in milliseconds, and we want to convert
# them into seconds.

response_times_ms = [1200, 1500, 1800]


# -------------------------------------------------------------
# Step 2: Function to convert ms → seconds
# -------------------------------------------------------------
# Returns the value after dividing by 1000.
# (Hindi: Milliseconds ko 1000 se divide karke seconds milte hain.)

def mil_sec(x):
    return x / 1000


# -------------------------------------------------------------
# Step 3: Convert using map() + lambda
# -------------------------------------------------------------
# We use map() with lambda to convert each ms value into seconds.

response_times_s = list(map(lambda x: x / 1000, response_times_ms))


# -------------------------------------------------------------
# Step 4: Print converted response times (in seconds)
# -------------------------------------------------------------
# Expected Output: [1.2, 1.5, 1.8]

print(response_times_s)
