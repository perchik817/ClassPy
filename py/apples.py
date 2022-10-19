apple = 10
bad_box = 0
good_box = 0
while apple !=0:
    answer = int(input('bad-1\ngood-2\nanswer - '))
    if answer == 1:
        apple -= 1
        bad_box+=1
        print(f'this is bad apple: {bad_box}\ngeneral apples: {apple}')

    elif answer==2:
        apple-=1
        good_box+=1
        print(f'this is good apple: {good_box}\ngeneral apples: {apple}')

print(f'general bad apples: {bad_box}\n'
      f'general good apples: {good_box}')