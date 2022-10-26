class Person:
    def __init__(self, name, age, edu):
        self.name = name
        self.age = age
        self.edu = edu
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Education: {self.edu}'
