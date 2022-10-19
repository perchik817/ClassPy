types = ["Максим", "Андрей", "Егор", ]
print(f'список менторов: {types}')
userAns=int(input('Хотите начать? (если да, нажмите 0, нет - 1)'))
first='1. добавить ментора '
second='2. удалить ментора'
third='3. изменить ментора'
while userAns==0:
    userChoice=int(input(f'Выберите команду:\n{first}\n{second}\n{third}\n'))
    if userChoice==1:
        name=str(input('Введите имя ментора: '))
        types.append(name)
    elif userChoice==2:
        delete=str(input('Какого ментора вы хотите удалить? '))
        types.remove(delete)
    elif userChoice==3:
        ask = str(input('Какого ментора вы хотите поменять? '))
        if ask in types:
            newel = str(input('Введите новое имя: '))
            types.remove(ask)
            types.append(newel)
    else:
        print('Такой команды нет. Попробуйте снова.')
    print(f'список менторов: {types}')
    userAns = int(input('Хотите начать? (если да, нажмите 0, нет - 1)'))