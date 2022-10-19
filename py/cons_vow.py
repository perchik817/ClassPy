while 1:
    word = str(input('напишите слово: '))
    print(f'общее колличество - {len(word)}')
    vowels = 'AаЕеЁёИиОоУуЫыЭэЮюЯяAaEeIiOoUuYy'
    consotans = 'БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщBbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZZ'
    count_v = 0
    count_c = 0

    for i in word:
        if i in vowels:
            count_v += 1
        elif i in consotans:
            count_c += 1

    print(f'Гласных - {count_v}\n'
          f'Согласных - {count_c} ')

    print(f'Гласные/Согласные - {round(count_v * 100 / len(word), 2)}% {round(count_c * 100 / len(word), 2)}%')

    print('-' * 20)

    exit = int(input('1-continue 0-exit'))

    if exit == 1:
        continue
    else:
        break