
students = []
students_marks=[]

while True:
    var = int(input('''1 - добавить ст, 
    2 - Удалить студента, 
    3 - Вывести информацию о студенте,
    4 - Добавить оценку студента,
    5 - Изменить оценку студента \n'''))
    if var==1:
        name = input("Введите имя студента: ")
        students.append(name)
        students_marks.append([])
    elif var==2:
        index = int(input("Введите номер студента для удаления: "))
        if 1<=index<=len(students):
            students.pop(index-1)
            students_marks.pop(index-1)
        else:
            print("Такого студента нет")
    elif var==3:
        for i in range (len(students)):
            print(f"{i+1}. {students[i]}: {students_marks[i]}")
    elif var==4:
        index = int(input("Введите номер студента: "))
        if index<1 or index>len(students):
            print("Не корректный номер студента")
        else:
            mark = int(input("Введите оценку: "))
            students_marks[index-1].append(mark)
    elif var == 5:
        index = int(input("Введите номер студента: "))
        if index < 1 or index > len(students):
            print("Не корректный номер студента")
        else:
            index_mark = int(input("Какую оценку поменять "))
            if len(students_marks[index-1])< index_mark:
                print("Такой оценки нет ")
            else:
                mark = int(input("Введите оценку: "))
                students_marks[index-1][index_mark]=mark
    else:
        break


