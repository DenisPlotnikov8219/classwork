
# нарисовать треугольник прямой вершиной вниз влево
n = int(input("Введите число: "))
for i in range(n, 0, -1):
    print("  "*(n-i) + "* "*(i))

# нарисовать треугольник прямой вершиной вверх вправо
n = int(input("Введите число: "))
for i in range(n):
    print("* "*(i+1))

# нарисовать треугольник вершиной вниз
n = int(input("Введите число: "))
if n > 0:
# Верхняя половина (включая центр)
    for i in range((n + 1) // 2):
        print(("  " * i + "* " * (n - i * 2)).rstrip())

n = int(input("Введите число: "))
if n > 0:
    for i in range((n - 1) // 2, -1, -1):
        print(("  " * i + "* " * (n - i * 2)).rstrip())

n = int(input("Введите число: "))
if n > 0:
# Верхняя половина (включая центр)
    for i in range((n + 1) // 2):
        print(("  " * i + "* " * (n - i * 2)).rstrip())
# Нижняя половина (без повторения центральной строки)
    for i in range((n - 1) // 2 - 1, -1, -1):
        print(("  " * i + "* " * (n - i * 2)).rstrip())

# Нарисовать треугольник прямой вершиной вниз вправо
n = int(input("Введите число: "))
for i in range(n):
    print("* "*(n-i))

# нарисовать треугольник прямой вершиной вниз влево
n = int(input("Введите число: "))
for i in range(n, 0, -1):
    print("  "*(n-i) + "* "*(i))

def show_menu():
    print("\n--- Меню фигур из звёздочек ---")
    print("а")
    print("б")
    print("в")
    print("г")
    print("д")
    print("и")
    print("к")

def main():
    while True:
        show_menu()
        choice = input("Выберите пункт меню (а-к): ").strip()

