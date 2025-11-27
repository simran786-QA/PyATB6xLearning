# -------------------------------------------------------------
# Step 1: Create Decorator - add_security
# -------------------------------------------------------------

def add_security(func):

    def wrapper():
        print("1. Before the function is called.")
        print("2. Wear Helmet, Dashcam, Gloves, Knee Guards, Carry License")
        func()
        print("3. After the function is called.")
        print("4. Secure Driving Completed. Remove all items safely.")

    return wrapper   # FIXED: return function, NOT wrapper()


# -------------------------------------------------------------
# Step 2: Apply Decorator to Functions
# -------------------------------------------------------------

@add_security
def drive_ola_scooter():
    print("I am driving Ola scooter")


@add_security
def drive_zypp_scooter():
    print("Driving Zypp scooter")


# -------------------------------------------------------------
# Step 3: Call Functions
# -------------------------------------------------------------
drive_ola_scooter()
drive_zypp_scooter()
