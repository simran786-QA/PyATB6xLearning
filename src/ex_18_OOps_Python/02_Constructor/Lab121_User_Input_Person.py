# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Python Class with Constructor and Instance Attributes
# -------------------------------------------------------------

# Step 1: Define the Class
class Person:
    # ---------------------------------------------------------
    # A. Class Attributes (initially None)
    name = None
    age = None
    phone = None
    occupation = None

    # ---------------------------------------------------------
    # B. Constructor (__init__) → automatically runs when object is created
    def __init__(self):
        print("Let's take the user input, Please share the name, age, phone, and occupation")

        # Taking user inputs and assigning them to instance variables
        self.name = input("Enter the name: ")
        self.age = input("Enter the age: ")
        self.phone = input("Enter the phone: ")
        self.occupation = input("Enter the occupation: ")

    # ---------------------------------------------------------
    # C. Behaviour / Method → Display all stored details
    def display_values(self):
        print("Name is:", self.name,
              "| Age is:", self.age,
              "| Phone is:", self.phone,
              "| Occupation:", self.occupation)


# -------------------------------------------------------------
# Step 2: Create an Object (instance) of the Person class
amit = Person()  # Constructor runs automatically here
amit.display_values()  # Display the details entered by the user
# -------------------------------------------------------------
