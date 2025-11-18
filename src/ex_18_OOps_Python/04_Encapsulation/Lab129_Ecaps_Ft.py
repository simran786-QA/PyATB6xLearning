# Web Automation - Selenium
# Page Object Model Example (Without Real Selenium Yet)

class VWOLoginPage:

    def __init__(self, email_arg, password_arg):
        # Assign input values to object attributes
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        # Simple validation (In real POM - this will be Selenium logic)
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed, Login Success")
        else:
            print("Login Failed")


# Dummy test data (Usually from Excel, CSV, JSON, or ENV)
pramod = VWOLoginPage("pramod@gmail.com", "Pass123")

# Call the login check method
pramod.login_confirm()
