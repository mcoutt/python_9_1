def matrix():                                   # создание игрового поля с разметкой
    n = 11                                      # каждая клетка 3х3
    num = 0                                     # нумерация клеток
    pic = [[' '] * n for i in range(n)]         # создаем матрицу (n x n) и заполняем её " "(пробелами)
    for i in range(n):                          # рисуем клетки
        for j in range(n):

            if (i + 1) % 4 == 0:                # каждую четветрую строку заполняем "-"
                pic[i][j] = '-'
            elif (j + 1) % 4 == 0:              # каждый четвертый столбец заполняем "|"
                pic[i][j] = '|'
            elif ((j + 1) % 4 == 3 and (i + 1) % 4 == 1):  # в каждом углу клетки пишем её номер
                num = num + 1
                pic[i][j] = num

    return pic                                  # возвращаем матрицу


# ---------------------------------------------
def gamer(gamer):                               # определение номера игрока, делающего ход и символа, которым заполняется клетка
    print('gamer ', gamer, ' input number: ')   # просим игрока ввести номер клетки игрового поля
    cell_ = input()

    if gamer == 1:                              # если это игрок 1, то он заполняет клетки крестиками "Х"
        sign_ = 'X'
        gamer = 2                               # после определения символя для заполнения, переопределяем игрока
    else:
        sign_ = '0'                             # если это игрок 2, то он заполняет клетки ноликами "0"
        gamer = 1

    return sign_, cell_, gamer                  # возвращаем значения символа заполнения, номера клетки, номера игрока


# ---------------------------------------------
def print_pic(a):                               # выводим значения матрицы
    for row in a:
        for elem in row:
            print(elem, end=' ')
        print()


# ---------------------------------------------
def check_pole(pic, cell, sign):                # проверка поля на уже установленный знак или установка знака
    shot = 1                                    # пока значение не установлено, 1
    check = 1                                   # пока не выбрана пустая клетка и не заполнена, 1
    while shot:                                 # проверка значения на возможность заполнения
        if check:                               # проверка значения на правильность заполнения
            if (int(cell) > 0 or int(cell) < 10):  # всего 9 клеток, по этому значения можно вводить от 1 до 9
                if int(
                        cell) % 3 == 1:         # значения вписываются в центр клеток, поэтому поределяем координаты, куда они будут вставлены
                    j = 1
                    if int(cell) // 3 == 0:
                        i = 1
                    elif int(cell) // 3 == 1:
                        i = 5
                    else:
                        i = 9
                elif int(cell) % 3 == 2:
                    j = 5
                    if int(cell) // 3 == 0:
                        i = 1
                    elif int(cell) // 3 == 1:
                        i = 5
                    else:
                        i = 9
                else:
                    j = 9
                    if int(cell) // 3 == 1:
                        i = 1
                    elif int(cell) // 3 == 2:
                        i = 5
                    else:
                        i = 9
            else:
                check = 0                       # если значение введено не правильно(0<cell<10), выход из цикла

            if pic[i][j] == ' ':                # проверяем, заполнена ли ячейка
                pic[i][j] = sign                # если не заполнена, ставим значение
                shot = 0                        # если значение поставлено, выходим из функции
            else:
                check = 0                       # если клетка уже заполнена, просим ввести значение снова
        else:
            print('wrong number, try agan:')    # просим игрока ввести знвчение заново
            cell = input()
            shot = 1
            check = 1
    return pic

#---------------------------------------------
def cross_out(pic,sign,g_o):
    j = 0
    check_win = 0

    for i in range(11):
        if i % 4 == 1:
            for j in range(11):
                if j % 4 == 1:
                    if pic[i][j] == ' ':
                        check_win = 0
                        break
                    else:
                        check_win = 2

    for i in range(11):                     #проверяем все строки
        if pic[i][j + 1] == pic[i][j + 5] == pic[i][j + 9] == sign:
            pic[i][j] = pic[i][j + 2] = pic[i][j + 4] = pic[i][j + 6] = pic[i][j + 8] = pic[i][j + 10] = '-'
            check_win = 1
    i=0

    for j in range(11):                     #проверяем все столбцы
        if pic[i+1][j] == pic[i + 5][j] == pic[i + 9][j] == sign:
            pic[i][j] = pic[i + 2][j] = pic[i + 4][j] = pic[i + 6][j] = pic[i + 8][j] = pic[i + 10][j] = '|'
            check_win = 1
    j = 0

                                            #проверяем диагональ слева направо сверху вних
    if pic[i + 1][j + 1] == pic[i + 5][j + 5] == pic[i + 9][j + 9] == sign:
        pic[i][j] = pic[i + 2][j + 2] = pic[i + 4][j + 4] = pic[i + 6][j + 6] = pic[i + 8][j + 8] = pic[i + 10][j + 10] = '\\'
        check_win = 1

                                            #проверяем диагональ слева направо снизу вверх
    if pic[i+1][j] == pic[i + 5][j] == pic[i + 9][j] == sign:
        pic[i + 10][j] = pic[i + 8][j + 2] = pic[i + 6][j + 4] = pic[i + 4][j + 6] = pic[i + 2][j + 8] = pic[i][j + 10] = '/'
        check_win = 1

    if sign=='X':
        gam = 1
    else:
        gam = 2

    if check_win == 1:
        g_o = 0
        print ('GAME OWER !!!')
        print ('Gamer ', gam, ' win !!!')
    elif check_win == 2:
        g_o = 0
        print ('GAME OWER !!!')
        print ('combat draw')

    return g_o
# --------------------------------------------

print('NEW GAME')

gam_ = 1
game_ower = 1

a = matrix()                                    # создаем массив(матрицу/поле)
print_pic(a)                                    # выводим значения матрицы
# sign_, cell_, gam = gamer(gam_)
# check_pole(a,cell_,sign_)

while game_ower:                                # пока не заполнены все клетки или кто-то не выиграет game_ower=1
    sign_, cell_, gam = gamer(gam_)             # проверяем номер игрока и определяем симфол для заполнения
    check_pole(a, cell_, sign_)                 # проверяем/заполняем матрицу
    game_ower = cross_out(a,sign_, game_ower)   # проверем линии на возможность зачеркивания
    print_pic(a)                                # выводим матрицу
    gam_ = gam
