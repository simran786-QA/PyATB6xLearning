# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: VWO Login using .env file (dotenv + OOPs)
# -------------------------------------------------------------

from dotenv import load_dotenv
import os


# -------------------------------------------------------------
# Step 1: Create Class with Constructor
# -------------------------------------------------------------
class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        # Store user-provided values
        self.email = email_arg
        self.password = password_arg

    # ---------------------------------------------------------
    # Step 2: Validate Login Using .env Credentials
    # ---------------------------------------------------------
    def login_confirm(self):
        load_dotenv()  # Load .env file

        correct_email = os.getenv("USERNAME")
        correct_password = os.getenv("PASSWORD")

        if self.email == correct_email and self.password == correct_password:
            print("Allowed, Login Success")
        else:
            print("Login Failed")


# -------------------------------------------------------------
# Step 3: Take User Input
# -------------------------------------------------------------
email = input("Enter the VWO login email: ")
password = input("Enter the VWO login password: ")

# -------------------------------------------------------------
# Step 4: Create Object and Validate Login
# -------------------------------------------------------------
vwo_object_ref = VWOLoginPage(email, password)
vwo_object_ref.login_confirm()

# -------------------------------------------------------------
# Step 5: Print OS Name (Optional Info)
# -------------------------------------------------------------
print(os.name)
