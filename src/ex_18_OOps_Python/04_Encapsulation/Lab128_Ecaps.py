# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: VWO Login Page – Class, Constructor & Validation
# -------------------------------------------------------------

class VWOLoginPage:

    # ---------------------------------------------------------
    # Step 1: Parameterized Constructor
    # ---------------------------------------------------------
    def __init__(self, email_arg, password_arg):
        # Store user inputs into instance variables
        self.email = email_arg
        self.password = password_arg

    # ---------------------------------------------------------
    # Step 2: Behavior to Validate Login
    # ---------------------------------------------------------
    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "pass123":
            print("Allowed to Login")
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
