# -------------------------------------------------------------
# Step 1: Define a Class Demonstrating Method Overriding Behavior
# -------------------------------------------------------------
# NOTE:
# Python does NOT support real method overloading.
# The second definition of make_http_request() OVERRIDES the first one.
# Default parameters are used to simulate optional arguments.

class Browser:

    # First version (this gets overridden)
    def make_http_request(self, url):
        print("Hi, Let's make the HTTP request without auth", url)

    # Second version (Python keeps only this one)
    def make_http_request(self, url, auth=None):
        print("Hi, Let's make the HTTP request with auth", url, auth)


# -------------------------------------------------------------
# Step 2: Create Object and Call Method
# -------------------------------------------------------------
t = Browser()
t.make_http_request("google.com", "admin")   # Uses the final method definition


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - Python keeps ONLY the last method with the same name.
# - Default parameters (auth=None) help create flexible method behavior.
# - This simulates overloading:
#       • make_http_request(url)
#       • make_http_request(url, auth)
# - Real overloading like Java/C++ is NOT supported in Python.

