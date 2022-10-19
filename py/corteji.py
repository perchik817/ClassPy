lesson = ("N" ,"O", "H", "T", "Y", "P", "E", "V", "O", "L", "I",
          True, False, 2, 1, 3, 5, 4, 11, 13, 12.12, 33.222, True, False)
word=[]
number=[]
bollean=[]
for c in lesson:
    if type(c)==str:
        word.append(c)
    elif type(c)==int:
        number.append(c)
    else:
        bollean.append(c)
        for i in bollean:
            if type(i)==float:
                bollean.remove(i)
word.reverse()
number.sort()
cortej_word=tuple(word)
cortej_bool=tuple(bollean)
cortej_num=tuple(number)

print(f'word: {cortej_word}\n'
      f'number: {cortej_num}\n'
      f'bool: {cortej_bool}')

