from random import *

def sort(values):
    lowest = 1000
    highest = 0
    sortedValues = []

    for valueTuple in values:
        nameToCheck, valueToCheck = valueTuple
        if valueToCheck > lowest:
            if valueToCheck > highest:
                highest = valueToCheck

                newSortedValues = []
                newSortedValues.append((nameToCheck, valueToCheck))
                for itemToCheck in sortedValues:
                    newSortedValues.append(itemToCheck)

                sortedValues = newSortedValues
            else:
                newSortedValues = []
                inserted = False
                for itemToCheck in sortedValues:
                    if not inserted and valueToCheck > itemToCheck[1]:
                        newSortedValues.append((nameToCheck, valueToCheck))
                        newSortedValues.append(itemToCheck)
                        inserted = True
                    else:
                        newSortedValues.append(itemToCheck)

                sortedValues = newSortedValues
        else:
            lowest = valueToCheck
            sortedValues.append((nameToCheck, valueToCheck))

    return sortedValues

#1
# try:
#     a = float(input("a = "))
#     b = float(input("b = "))
#     op = input("операція (+-*/): ")
#
#     if op == "+":
#         print(a + b)
#     elif op == "-":
#         print(a - b)
#     elif op == "*":
#         print(a * b)
#     elif op == "/":
#         if b == 0:
#             raise ZeroDivisionError("на нуль ділити не можна")
#         print(a / b)
#     else:
#         print("Невідома операція")
# except ValueError:
#     print("a та b повинні бути числами")
# except ZeroDivisionError as e:
#     print("Помилка: ", e)

#2
# def input_grade(prompt):
#     while True:
#         try:
#             grade = int(input(prompt))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Оцінка має бути в діапазоні 1..12")
#             print("Прийнято: ", grade)
#             return grade
#         except ValueError as e:
#             print("Помилка: ", e)
#
# input_grade("Введіть оцінку: ")

#3
# alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
# def randomName():
#     # щоб смішно було, зробив рандомну генерацію імен
#     name = ""
#     for j in range(randint(3, 10)):
#         name += alphabet[randint(0, 25)]
#     return name
#
# students = []
# for i in range(randint(3, 10)):
#     students.append(randomName())
#
# grades = {
#     "Математика": 1,
#     "Укр.Мова": 89,
#     "Інформатика": 67,
#     "Укр.Література": 99,
#     "НеЗнаю": 22
# }
#
# search = input("1 - учень, 2 - предмет: ")
# if search == "1":
#     try:
#         index = int(input("Індекс: "))
#         print("Учень: ", students[index])
#     except IndexError:
#         print("Такого учня не існує")
#     except ValueError:
#         print("Індекс повинен бути цілим числом")
# elif search == "2":
#     try:
#         predmet = input("Предмет: ")
#         print("Оцінка з предмету ", predmet, ": ", grades[predmet])
#     except KeyError:
#         print("Такого предмета не існує")
# else:
#     print("Такого типу пошуку не існує")

#4
processed = []
errors = 0
try:
    with open("students.txt", "r", encoding="utf-8") as f:
        for index, line in enumerate(f, 1):
            values = line.strip().split(";")
            if len(values) != 2:
                errors += 1
                print("Помилка: У рядку ", index, " неправильна кількість параметрів, або відсутній роздільник ;")
                continue
            name, grade = values
            try:
                grade = int(grade)
                if grade < 0 or grade > 100:
                    raise ValueError("Оцінка має бути в діапазоні 0..100")
                processed.append((name, grade))
            except ValueError as e:
                print("Помилка у рядку ", index, ": ", e)
                errors += 1
                continue

    processed = sort(processed)
    with open("result.txt", "w", encoding="utf-8") as f:
        for item in processed:
            f.write(f"{item[0]};{item[1]}\n")

    print("result.txt створено!!")
    print("Помилкових рядків: ", errors, "; Корректно записано: ", len(processed))
except FileNotFoundError:
    print("Файлу з даними студентів не знайдено")