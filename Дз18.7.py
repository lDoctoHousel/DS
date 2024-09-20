import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}

# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Вывести информацию по всем оценкам для определенного ученика
        5. Вывести средний балл по каждому предмету по определенному ученику
        6. Вывести средний балл по каждому ученику по определенному предмету
        7. Удалить данные по ученикам
        8. Удалить данные по предметам
        9. Удалить данные по оценкам
        10. Редактировать данные по предметам
        11. Добавление нового ученика
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == 4:
        print('4. Вывести информацию по всем оценкам для определенного ученика')
        student = input('Введите имя ученика: ')
        print(f'''Ученик: {student} 
Оценка: {students_marks[student]}''')

    elif command == 5:
        print('5. Вывести средний балл по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        for class_ in classes:
            if student in students_marks:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            else:
                print('Этого ученика в списке нет')

    elif command == 6:
        print('5. Вывести средний балл по каждому ученику по определенному предмету')
        class_ = input('Введите название предмета: ')
        for student in students:
            print(student)
            if class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            else:
                print('Этого предмета в списке нет')

    elif command == 7:
        print('7. Удалить данные по ученикам')
        end_student = input('Введите ученика, который хотите удалить: ')
        if end_student in students_marks:
            del students_marks[end_student]
            print(students_marks)
        else:
            print('Этого ученика в списке нет')

    elif command == 8:
        print('8. Удалить данные по предметам')
        end_class = input('Введите предмет, который хотите удалить: ')
        if end_class in classes:
            classes.remove(end_class)
            print(classes)
        else:
            print('Этого предмета в списке нет')

    elif command == 9:
        print('9. Удалить данные по оценкам')
        student = input('Введите имя: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                end_mark = int(input('Введите оценку, которую хотите удалить: '))
                if end_mark in (students_marks[student][class_]):
                    (students_marks[student][class_]).remove(end_mark)
                    print(students_marks[student][class_])
                else:
                    print('Этой оценки в списке нет')
            else:
                print('Этого предмета в списке нет')
        else:
            print('Этого ученика в списке нет')

    elif command == 10:
        print('10. Редактировать данные по предметам')
        new_class = input('Новое название предмета: ')
        students_marks[new_class] = []
        classes.append(new_class)
        print('Новый предмет добавлен')

        student = input('Введите имя: ')
        if student in students:
            class_ = input('Введите предмет: ')
            if class_ in classes:
                classes.remove(class_)
                print(classes)
            else:
                print('Этого предмета в списке нет')
        else:
            print('Этого ученика в списке нет')

    elif command == 11:
        print('11. Добавление нового ученика')
        new_student = input('Введите имя нового ученика: ')
        students_marks[new_student] = {
            'Математика': [],
            'Русский язык': [],
            'Информатика': [],
            }
        students.append(new_student)
        print('Новый ученик добавлен')
        print(students_marks)

    elif command == 12:
        print('12. Выход из программы')
        break