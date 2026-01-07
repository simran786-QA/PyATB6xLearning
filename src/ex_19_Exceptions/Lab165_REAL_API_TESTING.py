# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Exception Handling with requests (API / URL handling)
# -------------------------------------------------------------

import requests

# -------------------------------------------------------------
# Step 1: Take URL input from user
# -------------------------------------------------------------
# User provides the URL which will be tested using HTTP GET.

try:
    url = input("Enter the url: ")

    # ---------------------------------------------------------
    # Step 2: Send HTTP GET request with timeout
    # ---------------------------------------------------------
    # timeout=3 means request will wait max 3 seconds.

    response = requests.get(url, timeout=3)

    # ---------------------------------------------------------
    # Step 3: Print response status code
    # ---------------------------------------------------------
    print("Status Code:", response.status_code)


# -------------------------------------------------------------
# Step 4: Handle Connection Error
# -------------------------------------------------------------
# This error occurs when URL is wrong or internet is down.

except requests.exceptions.ConnectionError:
    print("Connection Error: Wrong URL or connection failed!")


# -------------------------------------------------------------
# Step 5: Handle Timeout Error
# -------------------------------------------------------------
# This error occurs when server response is too slow.

except requests.exceptions.Timeout:
    print("Timeout Error: Not able to load the URL within time.")


# -------------------------------------------------------------
# Step 6: Handle any other unexpected exception
# -------------------------------------------------------------
# Generic exception block for safety.

except Exception as e:
    print("Unexpected Error:", e)


# -------------------------------------------------------------
# Hindi Explanation:
# - try block me API request bheji ja rahi hai.
# - Agar URL galat hua ya internet issue hua → ConnectionError.
# - Agar response 3 sec me nahi aaya → Timeout error.
# - Koi aur issue aaya to generic Exception handle hoga.
#
# English Explanation:
# - The try block sends an HTTP request.
# - ConnectionError occurs for wrong URL or network issue.
# - Timeout occurs when response is slow.
# - Generic exception handles unexpected errors.
# -------------------------------------------------------------


# -------------------------------------------------------------
# Summary:
# 1. requests.get() is used to call APIs or URLs.
# 2. timeout prevents infinite waiting.
# 3. ConnectionError handles wrong URLs/network issues.
# 4. Timeout handles slow server responses.
# 5. Exception handling makes API tests stable.
# -------------------------------------------------------------
