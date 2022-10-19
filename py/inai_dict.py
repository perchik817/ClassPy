inai= {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
courses=[]
inai.pop('bag')
inai['address']='Малдыбаева 34б'
inai['instagram']='inai.kg'
inai['mob.phone']='0559127705'
ask=int(input('Введите кол-во новых предметов: '))
for i in range(ask):
    cours_ask=str(input( 'Названия предмета(-ов):\n'))
    courses.append(cours_ask)
inai['courses']+=courses
for keys, values in inai.items():
     print(f'{keys}:{values}')

