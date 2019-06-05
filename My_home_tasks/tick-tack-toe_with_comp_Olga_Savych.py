import random
Lboard=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
LComp=[1,2,3,4,5,6,7,8,9]
print('-------------')
print('| 1 | 2 | 3 |')
print('-------------')
print('| 4 | 5 | 6 |')
print('-------------')
print('| 7 | 8 | 9 |')
print(' ')
print('Давайте начнем игру Крестики-нолики! Вы ходите первым.')
print(' ') 
Stext1='Спасибо! Вы поставили Х в поле %s'
Stext3='Компьютер поставил O в поле %s'
Istep=1
Icount=0
Cell_x=0
Cell_o=0

for Istep in range(1,20):
    try:
        Cell_x=int(input('Укажите номер ячейки от 1 до 9 куда поставить X. Доступные ячейки: '+str(LComp)+' '))      
    except ValueError:
           print ('Вы ввели не число')
    else:
        if Cell_x>=1 and Cell_x<=9 and Lboard[Cell_x-1]==' ':
            Icount+=1
            Lboard[Cell_x-1]='X'
            LComp.remove(Cell_x)
            print (Stext1%Cell_x)                           
            print('-------------')
            print('| '+Lboard[0]+' | '+Lboard[1]+' | '+Lboard[2]+' |')
            print('-------------')
            print('| '+Lboard[3]+' | '+Lboard[4]+' | '+Lboard[5]+' |')
            print('-------------')
            print('| '+Lboard[6]+' | '+Lboard[7]+' | '+Lboard[8]+' |')
            print(' ')
            if (Lboard[0]=='X' and Lboard[1]=='X' and Lboard[2]=='X')\
            or (Lboard[0]=='X' and Lboard[3]=='X' and Lboard[6]=='X')\
            or (Lboard[2]=='X' and Lboard[5]=='X' and Lboard[8]=='X')\
            or (Lboard[3]=='X' and Lboard[4]=='X' and Lboard[5]=='X')\
            or (Lboard[6]=='X' and Lboard[7]=='X' and Lboard[8]=='X')\
            or (Lboard[1]=='X' and Lboard[4]=='X' and Lboard[7]=='X')\
            or (Lboard[0]=='X' and Lboard[4]=='X' and Lboard[8]=='X')\
            or (Lboard[2]=='X' and Lboard[4]=='X' and Lboard[6]=='X'):                    
                print ('Игра окончена! Вы победили!')
                break
            else:
                pass
            if Icount==9:
                print('Игра окончена. Ничья.')
                break
        elif Cell_x>=1 and Cell_x<=9 and Lboard[Cell_x-1]!=' ':
                print ('Ячейка занята')
        else:
                print ('Ваше значение находится за пределами допустимого диапазона')

    Cell_o=random.choice(LComp)
    Icount+=1
    Lboard[Cell_o-1]='O'
    LComp.remove(Cell_o)
    print (Stext3%Cell_o)     
    print('-------------')
    print('| '+Lboard[0]+' | '+Lboard[1]+' | '+Lboard[2]+' |')
    print('-------------')
    print('| '+Lboard[3]+' | '+Lboard[4]+' | '+Lboard[5]+' |')
    print('-------------')
    print('| '+Lboard[6]+' | '+Lboard[7]+' | '+Lboard[8]+' |')
    print(' ')
    if (Lboard[0]=='O' and Lboard[1]=='O' and Lboard[2]=='O')\
    or (Lboard[0]=='O' and Lboard[3]=='O' and Lboard[6]=='O')\
    or (Lboard[2]=='O' and Lboard[5]=='O' and Lboard[8]=='O')\
    or (Lboard[3]=='O' and Lboard[4]=='O' and Lboard[5]=='O')\
    or (Lboard[6]=='O' and Lboard[7]=='O' and Lboard[8]=='O')\
    or (Lboard[1]=='O' and Lboard[4]=='O' and Lboard[7]=='O')\
    or (Lboard[0]=='O' and Lboard[4]=='O' and Lboard[8]=='O')\
    or (Lboard[2]=='O' and Lboard[4]=='O' and Lboard[6]=='O'):
        print ('Игра окончена! Победил компьютер!')
        break
    else:
        pass
    if Icount==9:
        print('Игра окончена. Ничья.')
        break  
