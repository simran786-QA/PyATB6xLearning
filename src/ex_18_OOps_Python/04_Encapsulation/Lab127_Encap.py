# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Car Class with Parameterized Constructor & Behaviors
# -------------------------------------------------------------

class Car:
    # ---------------------------------------------------------
    # Step 1: Attributes
    # ---------------------------------------------------------
    name = None
    make = None
    model = None

    # ---------------------------------------------------------
    # Step 2: Parameterized Constructor
    # ---------------------------------------------------------
    def __init__(self, o_name, o_make, o_model):
        # Store the values in instance variables
        self.name = o_name
        self.make = o_make
        self.model = o_model

    # ---------------------------------------------------------
    # Step 3: Behavior (Method)
    # ---------------------------------------------------------
    def start_engine(self):
        print("Starting a car with the name", self.name)
        print("Starting a car with the make", self.make)
        print("Starting a car with the model", self.model)

# -------------------------------------------------------------
# Step 4: Create Objects + Call Methods
# -------------------------------------------------------------

lambo = Car("Lambo", "V6", "2023")
lambo.start_engine()

mg_hector = Car("Hector", "1.5 Turbo", "2024")
mg_hector.start_engine()
