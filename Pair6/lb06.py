from math import *
from random import *
from statistics import *
from datetime import *
import student_utils as utils
from tkinter import *

#1
# choice = input("Виберіть калькуляцію: ")
# if choice == "круг":
#     r = float(input("Введіть радіус: "))
#     S = round(pi * pow(r, 2), 2)
#     print("Площа круга: ", S)
# elif choice == "трикутник":
#     cath1, cath2 = map(float, input("Введіть катети через пробіл: ").split())
#     hypotenuse = sqrt(pow(cath1, 2) + pow(cath2, 2))
#     print("Довжина гіпотенузи: ", hypotenuse)
# elif choice == "упаковка":
#     n = int(input("Введіть кількість предметів: "))
#     k = int(input("Введіть вмістовність упаковки: "))
#     print("Потрібно упаковок: ", ceil(n / k))
# else:
#     print("Такого не існує")

#2
# n = int(input("N = "))
# if n > 0:
#     grades = []
#     level4Count = 0
#     for i in range(n):
#         grade = randint(1, 12)
#         grades.append(grade)
#         if grade >= 10:
#             level4Count += 1
#
#     print(grades)
#     print("Min: ", min(grades))
#     print("Max: ", max(grades))
#     print("Середня: ", sum(grades) / n)
#     print("Медіан: ", median(grades))
#     print("Кількість оцінок 10-12: ", level4Count)
# else:
#     print("n має бути натуральним числом.")

#3
# year, month, day = map(int, input("Введіть рік, місяць та день події через пробіл: ").split())
# today = datetime.today()
# chosen = datetime(year, month, day)
#
# diff = today - chosen
# if diff.days > 0:
#     print("Подія відбулася ", diff.days, " днів назад.")
# elif diff.days < 0:
#     print("Подія відбудеться через ", diff.days, " днів.")
# else:
#     print("Подія.. СЬОГОДНІ!!!!!!")

#4
latestLabels = []
def showZvit():
    for label in latestLabels:
        label.destroy()

    students = {}
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    for i in range(randint(1, 10)):
        # щоб смішно було, зробив рандомну генерацію імен
        name = ""
        for j in range(randint(3, 10)):
            name += alphabet[randint(0, 25)]
        studentGrades = utils.generateGrades(randint(5, 10))
        studentAverage = utils.averageGrades(studentGrades)
        studentLevel = utils.gradeLevel(studentAverage)

        students[name] = (studentGrades, studentAverage, studentLevel)

    row = 1
    for i, v in students.items():
        label = Label(
            window,
            text=f"Студент {i}: {v[0]} -- середня: {v[1]} -- рівень: {v[2]}",
            font=("Arial", 12),
            bg="black",
            fg="white")
        label.grid(row=row, column=0, padx=10, pady=2)
        row += 1
        latestLabels.append(label)

window = Tk()
window.title("Звіт")
window.geometry("750x400")
window.resizable(False, False)
window["bg"] = "black"

title = Label(window, text=f"Студенти якогось-там-{randint(17,22)}", font=("Arial", 18))
title.grid(row=0, column=0, pady=10)

showButton = Button(window, text = "Показати звіт!!", activebackground="gray", command=showZvit)
showButton.grid(row=12, column=0, pady=10)

window.mainloop()