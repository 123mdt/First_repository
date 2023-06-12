class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometr_reading = 0
    
    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometr(self):
        print(f"This car has {self.odometr_reading} miles in it")
    
    def update_odometr(self, mileage):
        if mileage >= self.odometr_reading:
            self.odometr_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increament_odometr(self, miles):
        self.odometr_reading += miles
        

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name())