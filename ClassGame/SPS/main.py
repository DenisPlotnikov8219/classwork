# import random
#
# for i in range(5):
#     num = random.randint(1,3)
#     print(num, end=" ")

import random

game_type = int(input("акой режим игры? 1-игрок, 2-компьютер"))
if game_type==2

result_wip_pc = 0
result_win_pl = 0

while True:
    win_pc = 0
    win_pl = 0

    while True:
        pc = random.randint(1,3)
        if pc == 1:
            print("камень")
        if pc ==2:
            print("ножницы")
        if pc ==3:
            print("бумага")



        while True:
            pl = int(input("Введите число: "))
            if pl == 1:
                print("камень")
                break
            elif pl ==2:
                print("ножницы")
                break
            elif pl ==3:
                print("бумага")
                break
            else:
                print("не то")


        if pc<pl or pc == 3 and pl == 1:
            print("Компьютер победил")
            win_pc += 1
        elif pc == pl:
            print("Ничья")
        else:
            print("Игрок победил")
            win_pl += 1

        if win_pc == 3:
            print(f"Компьютер победил со счетом {win_pc}:{win_pc}")
            break
        elif win_pl == 3:
            print(f"Игрок победил со счетом {win_pc}:{win_pc}")
            break
    print(f"Итоговый счет: PC {result_win_pc}: PL{result_win_pl}")
    a = input("ы хотите сыграть еще?" (/N))
    if a != "Y":
        break
else:
    result_wip_pl1 = 0
    result_win_pl2 = 0

    while True:
        win_pl1 = 0
        win_pl2 = 0

        while True:

            while True:
                pl2 = int(input("Введите число: "))
                if pl2 == 1:
                    print("камень")
                    break
                elif pl2 == 2:
                    print("ножницы")
                    break
                elif pl2 == 3:
                    print("бумага")
                    break
                else:
                    print("не то")

            if pl1 < pl2 or pl1 == 3 and pl2 == 1:
                print("Компьютер победил")
                win_pl1 += 1
            elif pl1 == pl2:
                print("Ничья")
            else:
                print("Игрок победил")
                win_pl2 += 1

            if win_pl1 == 3:
                print(f"Компьютер победил со счетом {win_pl1}:{win_pl2}")
                break
            elif win_pl2 == 3:
                print(f"Игрок победил со счетом {win_pl1}:{win_pl2}")
                break
        print(f"Итоговый счет: PC {result_win_pl1}: PL{result_win_pl2}")
        a = input("ы хотите сыграть еще?"( / N))
        if a != "Y":
            break