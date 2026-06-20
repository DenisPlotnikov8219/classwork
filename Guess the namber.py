import random



print("Компьютер загадал число от 1 до 99")
for i in range(5):

    number = random.randint(1, 99)
    attempts = 0

    result = 0
    while True:
        guess = int(input("Назови число: "))
        attempts += 1
        if attempts == 5:
            print("Вы проиграли.")
        if guess < number:
            print("Слишком мало! Попробуй больше.")
            print(f"счет: PC {attempts}: ")
        elif guess > number:
            print("Слишком много! Попробуй меньше.")
            print(f"счет: PC {attempts}: ")
        else:
            print(f"Поздравляю! Ты угадал число {number} за {attempts} попыток.")

            print(f"Итоговый счет: PC {attempts}: ")

            break