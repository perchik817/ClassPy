# полиморфизм
# class English:
#     def __init__(self, lang):
#         self.lang = lang
#
#     def greeting(self):
#         return f'This person can speak in {self.lang}'

# class Deutsch:
#     def __init__(self, lang):
#         self.lang = lang
#
#     def greeting(self):
#         return f'Das ist Man spricht auf {self.lang}'
#
# class Russian:
#     def __init__(self, lang):
#         self.lang = lang
#
#     def greeting(self):
#         return f'Этот человек умеет разговаривать на {self.lang}'
#
# ge = Deutsch('Guten Morgen')
# ru = Russian('Доброе утро')
# en = English('Good morning')
# print(ge.greeting())
# print(en.greeting())
# print(ru.greeting())

# Инкапсуляция
# class Account:
#     def __init__(self, login, password, secretKey):
#         self.login = login
#         self.password = password
#         self.secretKey = secretKey
#
#     def __str__(self):
#         return f'Login: {self.login}\n' \
#                f'Password: {self.password}\n' \
#                f'Secret Key: {self.secretKey}'
# acc_1 = Account('Perchik', 170105, 'dateofbirth')
# print(acc_1)
#
#абстракция и наследие
# class Car:
#     def __init__(self, title, marka, volume):
#         self.title = title
#         self.marka = marka
#         self.volume = volume
#
#     def __str__(self):
#         return f''
#
# class EuropeAuto(Car):
#     def __init__(self, title, marka, volume, airbag, abs, asp):
#         super(EuropeAuto, self).__init__(title, marka, volume)
#         self.airbag