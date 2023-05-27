class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def drive(self, distance):
        self.mileage += distance

    def get_info(self):
        return f"Car: {self.make} {self.model}\n" \
               f"Year: {self.year}\n" \
               f"Mileage: {self.mileage} km"

# Пример использования класса Car
car = Car("Toyota", "Camry", 2020, 50000)
print(car.get_info())

car.drive(100)
print(car.get_info())
