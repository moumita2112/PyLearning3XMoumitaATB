class Person:
    # Class Variables / Instance variables
    name = "Moumita"
    age = None
    height= 157

    def walk(self):
        a = 10  # Local Variable
        print("I am am method")
        print("Hi", self.age)
        print("Height", +self.height)


moumita = Person()
moumita.walk()
