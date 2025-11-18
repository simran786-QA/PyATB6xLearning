class TestExample:
    def __init__(self):
        self.driver = "Chrome"         # Public
        self._config = "STAG"          # Protected
        self.__api__key = "ABC12345"   # Private

    def show(self):
        print(f"Driver: {self.driver}")
        print(f"Config: {self._config}")
        print(f"API Key: {self.__api__key}")

    def __private_method1(self):   # Private method
        pass

    def __private_method2(self):   # Private method
        pass

    def work(self):
        self.__private_method1()
        self.__private_method2()


# Object creation
obj = TestExample()
obj.show()
obj.work()

# Access Levels:
# print(obj.driver)         # ✅ Public — accessible
# print(obj._config)        # ⚠️ Protected — accessible but discouraged
# print(obj.__api__key)     # ❌ Private — AttributeError
