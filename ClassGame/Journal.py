

student = []
student_marks = []

def ls_student(ls):
    while True:
        var = int(input(" 1 - Добавить студента: , 2 - Удалить студента: , 3 - Показать информацию: , 4 - Добавить оценку: , 5 - справить оценку: \n"))
        if var == 1:
            name = input(" 1 - Ввкдите имя студента: ")
            student.append(name)
            student_marks.append([])
        elif var == 2:
            index = input(" 2 - Удалить студента: ")
            if 1<=index<=len(student):
                student.pop(index-1)
                student_marks.pop(index-1)
            else:
                print("В списках не значится.")
        elif var == 3:
            for i in range (len(student)):
                print(f"{i+1}. {student[i]}: {student_marks[i]}")
        elif var == 4:
            index = input(" 1 - Ввкдите номер студента: ")
            if index < 1 or index> len(student):
                print("Некорpектно")
        else:
            index_marks = int(input("Какую оценку поменять: "))
            if len(student_marks[index-1]) < index_marks:
                print("Некорpектно")
            else:
                mark = int(input("Введить оценку: "))
                student_marks[index-1][index_marks] = mark

    else:
        break


