x = int(input())
season_1 = {12, 1, 2}
season_2 = {3, 4, 5}
season_3 = {6, 7, 8}
season_4 = {9, 10, 11}

#a=1

while x != 0:
   
    if x in range(1, 13):
        if x in season_1:
            print('zima')
            break
        elif x in season_2:
            print('vesna')
            break
        elif x in season_3:
            print('leto')
            break
        elif x in season_4:
            print('osen')
            break
        
    else:
        break
