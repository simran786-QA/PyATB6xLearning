# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Person Class with Attributes, Behaviors & Constructor
# -------------------------------------------------------------

class Person:
    # ---------------------------------------------------------
    # Step 1: Define Attributes (Instance Variables)
    # ---------------------------------------------------------
    def __init__(self, name, age, gender, occupation, city):
        # Hindi:
        # Yeh constructor hai (special function jo object create hone par call hota hai)
        # Aur hum yahan 5 attributes assign kar rahe hain.
        #
        # English:
        # This is the constructor — it’s called automatically when the object is created.
        # Here, we assign 5 attributes to the instance.
        self.name = name
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.city = city

    # ---------------------------------------------------------
    # Step 2: Define 5 Behaviors (Methods)
    # ---------------------------------------------------------

    # Method with No Argument & No Return
    def greet(self):
        print(f"Hello, my name is {self.name}. Nice to meet you!")

    # 1 Method with Argument but No Return
    def update_city(self, new_city):
        self.city = new_city
        print(f"{self.name} has moved to {self.city}.")

    # 2 Method with Argument & Return Value
    def increase_age(self, years):
        self.age += years
        return self.age

    # 3 Method with No Argument but Return Value
    def get_occupation(self):
        return self.occupation

    # 4 Print Function — Displays All Instance Variable Values
    def print_info(self):
        print("---- Person Details ----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Occupation:", self.occupation)
        print("City:", self.city)
        print("------------------------")


# -------------------------------------------------------------
# Step 3: Create an Object and Use All Behaviors
# -------------------------------------------------------------
person1 = Person("Simran Shaikh", 26, "Female", "QA Engineer", "Mumbai")

# Call all behaviors one by one
person1.greet()                      # No Arg, No Return
person1.update_city("Pune")          # Arg, No Return
new_age = person1.increase_age(2)    # Arg, Return
print("Updated Age:", new_age)
print("Current Occupation:", person1.get_occupation())  # No Arg, Return
person1.print_info()                 # Display all instance data
