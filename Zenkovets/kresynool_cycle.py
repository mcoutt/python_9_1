gam = 1
a = [[' ', ' ', '1', '|', ' ', ' ', '2', '|', ' ', ' ', '3'],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
     ['-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-'],
     [' ', ' ', '4', '|', ' ', ' ', '5', '|', ' ', ' ', '6'],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
     ['-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-'],
     [' ', ' ', '7', '|', ' ', ' ', '8', '|', ' ', ' ', '9'],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' '],
     [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']]

for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
# print('gamer ', gam ,' input number: ')
# cell = input()
tour = 1
shot = 1

while tour:
    if gam == 1:
        sign = 'X'
    else:
        sign = '0'
    #    print (sign)
    print('gamer ', gam, ' input number: ')
    cell = input()
    while shot:
        if (int(cell) < 1 or int(cell) > 9):
            print('wrong number, try agan:')
            cell = input()
            continue
        else:
            shot = 0
    shot = 1
    while shot:
        if cell == '1':
            if (a[1][1] == 'X' or a[1][1] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
            #                continue
            else:
                shot = 0
                a[1][1] = sign
        elif cell == '2':
            if (a[1][5] == 'X' or a[1][5] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[1][5] = sign
        elif cell == '3':
            if (a[1][9] == 'X' or a[1][9] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
            a[1][9] = sign
        elif cell == '4':
            if (a[5][1] == 'X' or a[5][1] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[5][1] = sign
        elif cell == '5':
            if (a[5][5] == 'X' or a[5][5] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[5][5] = sign
        elif cell == '6':
            if (a[5][9] == 'X' or a[5][9] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[5][9] = sign
        elif cell == '7':
            if (a[9][1] == 'X' or a[9][1] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[9][1] = sign
        elif cell == '8':
            if (a[9][5] == 'X' or a[9][5] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[9][5] = sign
        elif cell == '9':
            if (a[9][9] == 'X' or a[9][9] == '0' or int(cell) < 1 or int(cell) > 9):
                print('wrong number, try agan:')
                cell = input()
                continue
            else:
                shot = 0
                a[9][9] = sign

    shot = 1
    if gam == 2:
        gam = 1
    else:
        gam = 2

    if (a[1][1] == a[1][5] == a[1][9] == sign):
        a[2][0] = a[2][2] = a[2][4] = a[2][6] = a[2][8] = a[2][10] = '-'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[5][1] == a[5][5] == a[5][9] == sign):
        a[5][0] = a[5][2] = a[5][4] = a[5][6] = a[5][8] = a[5][10] = '-'
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[9][1] == a[9][5] == a[9][9] == sign):
        a[9][0] = a[9][2] = a[9][4] = a[9][6] = a[9][8] = a[9][10] = '-'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][1] == a[5][1] == a[9][1] == sign):
        a[0][1] = a[2][1] = a[4][1] = a[6][1] = a[8][1] = a[10][1] = '|'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][5] == a[5][5] == a[9][5] == sign):
        a[0][5] = a[2][5] = a[4][5] = a[6][5] = a[8][5] = a[10][5] = '|'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][9] == a[4][9] == a[9][9] == sign):
        a[0][9] = a[2][9] = a[4][9] = a[6][9] = a[8][9] = a[10][9] = '|'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][1] == a[5][5] == a[9][9] == sign):
        a[0][0] = a[2][2] = a[4][4] = a[6][6] = a[8][8] = a[10][10] = '\\'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][9] == a[5][5] == a[9][1] == sign):
        a[10][0] = a[8][2] = a[6][4] = a[4][6] = a[2][8] = a[0][10] = '/'
        print('GAME OWER')
        print('gamer ', gam, ' WIN !!!')
        tour = 0
    elif (a[1][1] != ' ' and a[1][5] != ' ' and a[1][9] != ' ' and a[5][1] != ' ' and a[5][5] != ' ' and a[5][
        9] != ' ' and a[9][1] != ' ' and a[9][5] != ' ' and a[9][9] != ' '):
        print('GAME OWER')
        print('combat draw')

    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()
