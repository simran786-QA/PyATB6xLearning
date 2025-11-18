class Bank:

    def __init__(self, account_number, balance):
        self.balance = balance                  # Public
        self.__account_number = account_number  # Private

    def check_balance(self):
        print(self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_me_account_number(self, is_auth):
        if is_auth is True:
            print(self.__account_number)
        else:
            print("Not Allowed!")


# Object
icici = Bank(9876543210, 100)

icici.deposit(100)              # Adding money
icici.check_balance()           # Display balance

# Private var - not accessible directly
# print(icici.__account_number) # ❌

icici.show_me_account_number(True)   # Allowed only if authenticated
