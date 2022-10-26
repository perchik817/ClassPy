# ромбовидное наследие
# class Car:
#     def __init__(self, title, volume, color, year):
#         self.title = title
#         self.volume = volume
#         self.color = color
#         self.year = year
#     def __str__(self):
#         return f'Title: {self.title}'
# class GazCar(Car):
#
# class ElectricCar(Car):
#
# class HybridCar(GazCar, ElectricCar):
#
# class Engie:
#     def __init__(self, volume, title, mileage):
#         self.volume = volume
#         self.title = title
#         self.mileage = mileage
#     def drive(self):
#         return f'this engie an drive for moto and car'
#     @property
#     def __str__(self):
#         return f'Title: {self.title}\n' \
#                f'Volume: {self.volume}\n' \
#                f'Mileage: {self.mileage}'
# class Moto(Engie):
#     def __init__(self, volume, title, mileage):
#         super(Moto, self).__init__(volume, title, mileage)
#     def __str__(self):
#         return super(Moto, self).__str__
#
#
# moto_1 = Moto(1.6, "xtouota", 6000)
# print(moto_1)
#
# class Auto(Engie):
#     def __init__(self, volume, title, mileage):
#         super(Auto, self).__init__(volume, title, mileage)
#     def __str__(self):
#         return super(Auto, self).__str__
#
#
# auto_1 = Auto(5.0, 'v6', 10000)
# print(auto_1)