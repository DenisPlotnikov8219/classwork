# age = int(input("Введите ваш возраст:"))
# if 0 <= age <= 12:
#  category = "ребёнок"
# elif 12 < age <= 18:
#  category = "подросток"
# elif 18 < age <= 60:
#  category = "взрослый"
# elif age > 60:
#  category = "пенсионер"
# else:
#  category = "некорректный возраст"
# print(f"Вы являетесь {category}.")
#


# symbols = {
#  '0': ')',
#  '1': '!',
#  '2': '@',
#  '3': '#',
#  '4': '$',
#  '5': '%',
#  '6': '^',
#  '7': '&',
#  '8': '*',
#  '9': '('
# }
# user_input = input("Введите число от 0 до 9:")
# if user_input in symbols:
#  print(f"Символ: {symbols[user_input]}")
# else:
#  print("Ошибка: введите число от 0 до 9.")
#



# year = int(input("Введите год:"))
#
# if (year% 400 == 0) or (year% 4 == 0 and year% 100!= 0):
#     print(f"{year} год — високосный.")
# else:
#     print(f"{year} год — не високосный.")





# number = input("Введите пятиразрядное число:")
#
# if len(number)!= 5:
#     print("Ошибка: нужно ввести именно пятиразрядное число!")
# else:
#     if number == number[::-1]:
#         print("Число является палиндромом.")
#     else:
#         print("Число не является палиндромом.")



#
#
# summa = float(input("Введите сумму покупки: "))
#
# if 200 <= summa < 300:
#     discount = 0.03
# elif 300 <= summa < 500:
#     discount = 0.05
# elif summa >= 500:
#     discount = 0.07
# else:
#     discount = 0
# total = summa * (1 - discount)
#
# print(f"Сумма покупки: {summa}")
# print(f"Скидка: {discount * 100}%")
# print(f"Сумма к оплате: {total}")


# L = float(input("Введите длину окружности:"))
# P = float(input("Введите периметр квадрата:"))
#
# d = L / 3.14
#
# a = P / 4
#
# if d <= a:
#     print("Окружность может поместиться в квадрат.")
# else:
#     print("Окружность не может поместиться в квадрат.")




# print("Добро пожаловать на тест! Ответьте на 3 вопроса, выбирая вариант от 1 до 3.")
#
# print(" Какой город является столицей Франции?")
# print("1) Берлин")
# print("2) Мадрид")
# print("3) Париж")
# answer1 = int(input("Ваш ответ (1-3): "))
#
# print(" Кто написал «Гамлета»?")
# print("1) Лев Толстой")
# print("2) Уильям Шекспир")
# print("3) Фёдор Достоевский")
# answer2 = int(input("Ваш ответ (1-3):"))
#
# print(" Какая планета самая большая в Солнечной системе?")
# print("1) Земля")
# print("2) Юпитер")
# print("3) Марс")
# answer3 = int(input("Ваш ответ (1-3):"))
#
# score = 0
# if answer1 == 3:
#     score += 2
# if answer2 == 2:
#     score += 2
# if answer3 == 2:
#     score += 2
#
# print(f"Вы набрали {score} баллов из 6 возможных.")



number = input("Введите трёхзначное число:")

#
# if len(number) != 3:
#     print("Ошибка: нужно ввести трёхзначное число!")
# else:
#     digits = list(number)
#
#     if digits[0] == digits[1] or digits[0] == digits[2] or digits[1] == digits[2]:
#         print("В числе есть одинаковые цифры.")
#     else:
#         print("Все цифры в числе разные.")

