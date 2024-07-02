class Car:
    name = None

    # private variables and methods can be accessed only within the class
    # protected variables within modules(directory)
    def __init__(self):
        self.public_var = "public" #public variable
        self._protected_var = "protected123" # starts with underscore protected
        self.__private_var = "pass@123" # starts with double underscore private variable

    def __private_method(self):
        print("Protected!")

    def printName(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")


# This is end of the class

alto = Car()
alto.printName()
# alto.__private_var
