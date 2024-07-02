class Car:
    model = None
    name = None
    make = None

    def __init__(self, o_model, o_name, o_make):
        self.model = o_model
        self.name = o_name
        self.make = o_make

    def start_engine(self):
        print("Starting a car with model" +self.model)
        print("Starting a car with name" +self.name)
        print("Starting a car with make" +self.make)


creta = Car(o_model="SUV", o_name="Creta", o_make="2024")
creta.start_engine()

bmw= Car(o_model="BMW", o_name="2023", o_make="2011")
bmw.start_engine()