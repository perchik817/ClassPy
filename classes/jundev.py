# 1) Создать супер класс JunDev задать ему атрибуты создать для него 2 метода,
# к классу JunDev создать 1 объект
#
# 2) Создать класс MidDev отнаследовать атрибуты и методы от JunDev, так же
# добавить 3 атрибута , 1метод к Mid Dev и создать объект
#
# 3) Создать класс SenDev отнаследовать атрибуты и методы от MidDev, так же
# добавить 3 атрибута , 1метод к Mid Dev и создать объект

# Создать метод каким языком программирования владеет каждый прогер
#   если в методе указан язык Python PHP HTML CSS то выводит сообщение
#   "ты молодец"
#   если в методе указан язык QBasic
#   "Ты не молодец"

class JunDev:
    def __init__(self, name, age, w_e):
        self.name = name
        self.age = age
        self.w_e = w_e

    def prog_lang(self, lg):
        if lg == 'Python':
            print('good')
        elif lg == 'Php':
            print('good')
        else:
            print('bad')

    def married(self, y_n):
        return f'Married: {y_n}'

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n'\
               f'Work expierene: {self.w_e}'

class MidDev(JunDev):
    def __init__(self, name, age, w_e, company, computer, headphones):
        super().__init__(name, age, w_e)
        self.company = company
        self.computer = computer
        self.headphones = headphones

    def prog_lan1g(self, lg1):
        if lg1 == 'Python':
            print('good')
        elif lg1 == 'Php':
            print('good')
        else:
            print('bad')

    def married2(self, n_y):
        return f'Married: {n_y}'

    def mouse(self, y_n):
        return f'Uses mouse: {y_n}'

    def __str__(self):
        return super(MidDev, self).__str__()+f'\nCompany: {self.company}\n' \
                                             f'Computer: {self.computer}\n' \
                                             f'Headphones: {self.headphones}'


junDev_obj = JunDev("John", 22, 2)
print(junDev_obj)
print(junDev_obj.married(False))

print(junDev_obj.prog_lang(str(input('wwww'))))
print("^^||"*10)
midDev_obj = MidDev("Sarah", 27, 5, "Abiyir", "Mac M1 Pro", "AirPods")
print(midDev_obj)
print(midDev_obj.married2(True))
print(midDev_obj.mouse(False))
print(midDev_obj.prog_lan1g('www'))

