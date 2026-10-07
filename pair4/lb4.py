#numbers = [12, 3, 4, 14, -12, 5, 10, 16, -4]

#positive = set()
#negative = set()
#even = set()
#multiple3 = set()

#for n in numbers:
#    if n > 0:
#        positive.append(n)
#    elif n < 0:
#        negative.append(n)
#    if n % 2 == 0:
#        even.append(n)
#    if n % 3 == 0:
#        multiple3.append(n)

#print("Додатні: ", positive)
#print("Від'ємні: ", negative)
#print("Парні: ", even)
#print("Кратні 3: ", multiple3)
#print("Мінімальне: ", min(numbers), " максимальне: ", max(numbers))
#print("Сумма: ", sum(numbers), "середня арифметична: ", sum(numbers) / len(numbers))

#group1 = {'Anna', 'Ivan', 'Olha'}
#group2 = {'Ivan', 'Maksym', 'Olha'}

#print("Разом: ", ", ".join(group1 & group2))
#print("Тільки перша група: ", ", ".join(group1 - group2))
#print("Тільки друга група:", ", ".join(group2 - group1))
#print("Усі: ", ", ".join(group1 | group2))

#catalog = {"milk": 48, "bread": 25, "tea": 75, "coffee": 150}

#def add(name, price):
#    catalog[name] = price

#def find(name):
#    price = catalog.get(name)
    # Return the value for key if key is in the dictionary, else default.
    # (з документації метода .get, я так зрозумів саме це вважалось під "безпечним пошуком"
#    if price is None:
#        print("Товару ", name, "не знайдено")
#    else:
#        print(name, " - ", price, " грн")

#def range(low, high):
#    for name, price in catalog.items():
#        if low <= price <= high:
#            print(name, " - ", price, " грн")

#add("juice", 777)
#add("eggs", -99)

#print(catalog)

#find("tea")

#print("Ціновий діапазон: 40..100 грн")
#range(40, 100)

groupInfo = ('10-IT', '2026/2027')

journal = {}
sortedJournal = {}

bestAverage = (0, "")

def addStudent(name, grades):
    if len(grades) != 5:
        print("Негідника (", name, ") проблатили!!!")
        return
    for grade in grades:
        if 12 < grade or grade < 1:
            print("Неможлива оцінка у ", name)
            return
    journal[name] = grades

    # В пітоні чомусь не можна тикати змінні не всередині функцій, тому ось так треба зробити щоб можна було
    # Без цього помилка виходить.
    global bestAverage
    if sum(grades) / len(grades) > bestAverage[0]:
        bestAverage = (sum(grades) / len(grades), name)

addStudent("Anna", [10, 11, 12, 9, 10])
addStudent("Ivan", [8, 9, 10, 11, 9])
addStudent("Petro", [5, 6, 7]) # приклад

print(groupInfo[0], " - ", groupInfo[1])

curLowest = 100
curHighest = 0

for journalName, journalGrades in journal.items():
    average = sum(journalGrades) / len(journalGrades)

    # Сортуємо вручну
    # Довго пояснювати, але що я тут роблю цее зберігаю найбільше та найменше число, щоб порівнювати
    # Якщо числе більше ніж найбільше, тоді це, логічно, найбільший, а в нашому випадку, найкращий результат
    # Створюємо новий словник, й першим вставляємо найкращий результат, а потом добавляємо інші після нього
    # Якщо число менше або дорівнює найменшому, просто в кінець його ставимо та й все
    if average > curHighest:
        curHighest = average

        newSortedJournal = dict()
        newSortedJournal[0] = (journalName, average)

        for i, v in sortedJournal.items():
            if v[0] == journalName:
                continue
            newSortedJournal[len(newSortedJournal)] = (v[0], v[1])

        sortedJournal = newSortedJournal
    elif average <= curLowest:
        curLowest = average
        sortedJournal[len(sortedJournal)] = (journalName, average)

for i, v in sortedJournal.items():
    print(v[0], " - ", v[1])

print("Найкращий результат: ", bestAverage[1], " - ", bestAverage[0])
