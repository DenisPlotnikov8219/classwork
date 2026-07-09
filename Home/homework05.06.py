material_type = input("Введите тип учебного материала: ")
if not material_type:
    print("Ошибка: тип материала не может быть пустым! ")
cost = float(input("Введите стоимость материала:"))
if cost <= 0:
    print("Ошибка: стоимость должна быть положительным числом. Попробуйте ещё раз.")
category = input("Введите категорию материала: ")
if not category:
    print("Ошибка: категория не может быть пустой!")
print(f"Материал успешно добавлен!")
print(f"Тип: {material_type}")
print(f"Стоимость: {cost}")
print(f"Категория: {category}")
