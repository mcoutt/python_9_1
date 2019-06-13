import random

user1 = input("Play - X, Введите свое имя, игрок №1:")
while True:
    if user1 == '': user1 = input("Введите свое имя, игрок №1:")
    else: break

while True:
    user2 = input("Будет с Вами играть 2 игрок? Yes or No:")
    if user2 == '' or not user2[0].lower() in ['y','n']: print("Некорректный ввод")
    else: break

if user2.lower() == 'y':
    #Игрок
    user2 = input("Play - 0, Введите имя, игрок №2:")
    while True:
        if user2 == '': user2 = input("Введите свое имя, игрок №2:")
        else:break

if user2.lower() == 'n':
    user2 = 'PC'
#Поле, как список
P = [1,2,3,4,5,6,7,8,9]
print('Активное поле:','\n',P[0:3],'\n',P[3:6],'\n',P[6:9])

win = 1
while win < 10:
    print('Игрок',user1)
    while True:
      x1 = int(input("введите номер поля для установки Х:"))
      if  x1 not in P: print("не коректный номер для поля")
      else: break
    P = ['X' if x == x1 else x for x in P]
    print('Активное поле:','\n',P[0:3],'\n',P[3:6],'\n',P[6:9])
    if P[0] == P[1] == P[2] or P[3] == P [4] == P[5] or P[6] == P[7] == P[8] or P[0] == P[4] == P[8] or \
            P[2] == P[4] == P[6] or P[0] == P[3] == P[6] or P[1] == P[4] == P[7] or P[2] == P[5] == P[8]:
        print('\n', P[0:3], '\n', P[3:6], '\n', P[6:9])
        print('Мы имеем победителя!...Игрок:', user1)
        break
    else:
        S = list.copy(P)
        S = list(filter(lambda a: a != 'X', S))
        S = list(filter(lambda a: a != '0', S))
        if not S:
            print('Победила дружба . Ничья')
            break
        else:
            if user2 == 'PC':
                y1 = random.choice(S)
            else:
                print('Игрок', user2)
                while True:
                   y1 = int(input("введите номер поля для установки 0:"))
                   if y1 not in P: print("не коректный номер для поля")
                   else: break
            P = ['0' if x == y1 else x for x in P]
            print('Активное поле:', '\n', P[0:3], '\n', P[3:6], '\n', P[6:9])
            if P[0] == P[1] == P[2] or P[3] == P[4] == P[5] or P[6] == P[7] == P[8] or P[0] == P[4] == P[8] or \
                    P[2] == P[4] == P[6] or P[0] == P[3] == P[6] or P[1] == P[4] == P[7] or P[2] == P[5] == P[8]:
                print('\n', P[0:3], '\n', P[3:6], '\n', P[6:9])
                print('Мы имеем победителя!...Игрок:', user2)
                break
win +=1







