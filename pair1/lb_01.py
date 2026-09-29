# Я думаю, ви не перевіряєте вручну, але для удобності зробив на базі функцій!!!

import math

def a1():
    n = int(input("Введіть ціле число: "))
    if n % 2 == 0:
        print("Число є парним")
    else:
        print("Число є непарним")

def b1():
    age = int(input("Введіть свій вік: "))
    if age >= 18:
        print("Ви повнолітні!")
    else:
        print("Ви неповнолітні!")

def c1():
    r = int(input("Введіть радіус кола: "))
    area = math.pi * r ** 2
    length = r * math.pi * 2
    print("Площа кола: ", area)
    print("Довжина кола: ", length)

def d1():
    a, b = map(int, input("Введіть два числа: ").split())
    print("Найбільше число: ", max(a, b))

def n2():
    x, y = map(int, input("Введіть x, y через пробіл").split())
    if x > 0:
        if y > 0:
            print("Точка знаходиться в першій чверті")
        else:
            print("Точка знаходиться в четвертій чверті")
    else:
        if y > 0:
            print("Точка знаходиться в другій чверті")
        else:
            print("Точка знаходиться в третій чверті")

def n3():
    # Я не знаю як грамматично правильно, тому я просто прийму, що
    # якщо число закінчуюється 1, то тоді "рік"
    # якщо 2, 3, або 4 то тоді "роки"
    # в інших випадках "років"
    age = int(input("Введіть свій вік: "))
    if age > 120:
        print("Вам не може бути 120 років.")
        return

    # так як 1 / 10 дає остачу 1, замість порівняння тексту, зробимо ось так
    if age % 10 == 1:
        print("Вам ", age, " рік")
    elif age % 10 in [2, 3, 4]:
        print("Вам ", age, " роки")
    else:
        print("Вам ", age, " років")

def additional():
    p1 = 17
    p2 = 120
    k = 10

    n = int(input("Введіть кількість квитків: "))
    buyIndividually = n % k

    result = 0
    result += (n - buyIndividually) * p2 / 10
    result += buyIndividually * p1

    print("Загальна вартість квитків: ", result)

def choose():
    choice = input("Введіть завдання, яке хочете перевірити: ")
    if choice == "n1":
        anotherChoice = input("Введіть завдання, яке хочете перевірити (a, b, c, d): ")
        if anotherChoice == "a":
            a1()
        elif anotherChoice == "b":
            b1()
        elif anotherChoice == "c":
            c1()
        elif anotherChoice == "d":
            d1()
        else:
            print("Такого не існує.")
    elif choice == "n2":
        n2()
    elif choice == "n3":
        n3()
    elif choice == "add":
        additional()
    else:
        print("Такого не існує.")

    again = input("Далі? ")
    if again == str.lower("так"):
        choose()

choose()
