def generate_sequence():

    while True:
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
            if start > end:
                print("Начало диапазона не может быть больше конца. Попробуйте снова.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    while True:
        choice = input("Выберите тип последовательности (все, чётные, нечётные): ").strip().lower()
        if choice in ['все', 'чётные', 'нечётные']:
            break
        else:
            print("Неверный выбор. Введите 'все', 'чётные' или 'нечётные'.")

    if choice == 'все':
        sequence = list(range(start, end + 1))
    elif choice == 'чётные':
        sequence = list(range(start + (start % 2), end + 1, 2))
    else:
        sequence = list(range(start + (start % 2), end + 1, 2))

    print(f"Последовательность: {sequence}")

generate_sequence()