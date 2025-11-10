# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Page Load Verification using While Loop and Timer
# -------------------------------------------------------------

# 🎯 Objective:
# Simulate a web page load check that waits up to 5 seconds.
# If the page loads within 5 seconds → Success ✅
# Otherwise → Timeout ❌

# -------------------------------------------------------------
import time
import random

# Initialize variables
wait_time = 0
page_loaded = False


# -------------------------------------------------------------
# 🧩 Function to simulate API/page response
def api_response():
    """
    Simulates page loading status.
    Randomly returns True (page loaded) or False (still loading).
    """
    return random.choice([False, True])


# -------------------------------------------------------------
# 🕐 Start the page load checking loop
while wait_time < 5:
    page_loaded = api_response()
    if page_loaded:
        print(f"✅ Page loaded successfully in {wait_time + 1} seconds.")
        break
    else:
        print(f"⏳ Checking... (second {wait_time + 1})")
        time.sleep(1)  # Wait for 1 second
        wait_time += 1

# -------------------------------------------------------------
# ❌ Handle timeout case
if not page_loaded:
    print("❌ Timeout! Page failed to load within 5 seconds.")

# -------------------------------------------------------------
# 🧠 Explanation:
# 1️⃣ We simulate page load using `api_response()` (random True/False).
# 2️⃣ The loop checks every second for up to 5 seconds.
# 3️⃣ If it loads early → break immediately.
# 4️⃣ If not → timeout message is printed.

# -------------------------------------------------------------
# ✅ Example Output (varies per run):
# ⏳ Checking... (second 1)
# ⏳ Checking... (second 2)
# ✅ Page loaded successfully in 3 seconds.

# OR

# ⏳ Checking... (second 1)
# ⏳ Checking... (second 2)
# ⏳ Checking... (second 3)
# ⏳ Checking... (second 4)
# ⏳ Checking... (second 5)
# ❌ Timeout! Page failed to load within 5 seconds.
# -------------------------------------------------------------
# 💡 QA Use Case:
# - Common in Selenium or API-based frameworks to wait for conditions.
# - Simulates dynamic wait logic before marking test as failed.
# -------------------------------------------------------------
