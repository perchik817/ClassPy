class Animal:
    def __init__(self, animal, kind, height, weight):
        self.animal = animal
        self.kind = kind
        self.height = height
        self.weight = weight

    def __str__(self):
        return f'Animal: {self.animal}\n' \
               f'Kind: {self.kind}\n' \
               f'Height: {self.height}\n' \
               f'Weight: {self.weight}\n'

class Reptiles(Animal):
    def __init__(self, animal, kind, height, weight, area, temperature):
        super(Reptiles, self).__init__(animal, kind, height, weight)
        self.area = area
        self.temperature = temperature

    def temp(self, t):
        if t < 4 :
            print(f'This is a cold-blooded animal\n')
        else:
            print(f'This is a warm-blooded animal\n')

    def __str__(self):
        return super(Reptiles, self).__str__()+f'Area: {self.area}\n' \
                                               f'Temperature: {self.temperature}'

class Mammals(Animal):
    def __init__(self, animal, kind, height, weight, population, color):
        super(Mammals, self).__init__(animal, kind, height, weight)
        self.population = population
        self.color = color

    def pop(self, p):
        if p < 400700:
            print(f'This population is too small - {self.population}')
        else:
            print(f'This population is big - {self.population}')

    def __str__(self):
        return super(Mammals, self).__str__()+f'Population: {self.population}\n' \
                                              f'Color: {self.color}'


# a = str(input('Write the name of the animal: '))
# k = str(input('Kind of the animal: '))
# h = float(input('Height of the animal: '))
# w = float(input('Weight of the animal: '))
# ani = Animal(a, k, h, w)
# print(f'class Animal:\n'
#       f'{ani}\n')
# print('-'*17)

# ar = str(input('Where does this animal live? '))
# t = float(input('What is a blood-temperature of the animal? '))
# rep = Reptiles(a, k, h, w, ar, t)
# print(f'class Reptiles:\n'
#       f'{rep}')
# print(rep.temp(t))
# print('-'*17)

# pn = float(input('What is the number of population (mln)? '))
# c = str(input('What is the color of the animal? '))
# mam = Mammals(a, k, h, w, pn, c)
# print(f'class Mammals:\n'
#       f'{mam}')
# print(mam.pop(pn))
