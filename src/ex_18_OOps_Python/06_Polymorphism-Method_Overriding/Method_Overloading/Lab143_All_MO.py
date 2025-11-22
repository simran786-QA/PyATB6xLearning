# -------------------------------------------------------------
# Step 1: Define Person Class with Overridden Methods
# -------------------------------------------------------------
# Python DOES NOT support traditional method overloading.
# The last defined method with the same name overrides the previous one.
class Person:
    def say_name(self, name):
        print("Hi", name)

    # This method OVERRIDES the previous one automatically
    def say_name(self, name, lastname="Dutta"):
        print("Hi,", name, lastname)


# -------------------------------------------------------------
# Step 2: Create Object and Call Method
# -------------------------------------------------------------
t = Person()
t.say_name("Pramod")     # Uses second method → "Hi, Pramod Dutta"


# -------------------------------------------------------------
# SUMMARY
# -------------------------------------------------------------
# - Python does NOT support method overloading.
# - The second say_name() definition overrides the first.
# - Default parameter (lastname="Dutta") allows single argument calls.
# - Output uses the most recent definition of say_name().


