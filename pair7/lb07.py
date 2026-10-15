import os

# можна буде в наступний раз використовувати функцію від пайтона?
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
# dani s protocola ne pravdyvi
# with open("text.txt", "r", encoding="utf-8") as file:
#     linesCount = 0
#     wordsCount = 0
#     symbolsCount = 0
#     longestLine = (0, 0)
#
#     for line in file:
#         line = line.strip()
#
#         linesCount += 1
#         if len(line) > longestLine[1]:
#             longestLine = (linesCount, len(line))
#
#         words = line.split()
#
#         wordsCount += len(words)
#         for word in words:
#             symbolsCount += len(word)
#
#     print("Рядків: ", linesCount)
#     print("Слів: ", wordsCount)
#     print("Символів: ", symbolsCount)
#     print(f"Найдовший рядок: #{longestLine[0]}, {longestLine[1]} символів")

#2
# fragment = input("Фрагмент: ").lower()
# with open("text.txt", "r", encoding="utf-8") as file:
#     foundFragment = False
#     for i, line in enumerate(file, 1):
#         clean = line.strip().lower()
#         if fragment in clean:
#             foundFragment = True
#             print(i, ": ", line)
#
#     if not foundFragment:
#         print("збігів немає")

#3
if not os.path.exists("result.txt"):
    sortedGrades = []
    with open("students.txt", "r", encoding="utf-8") as file:
        grades = []
        for line in file:
            name, grade = line.strip().split(';')
            grade = int(grade)
            grades.append((name, grade))

        sortedGrades = sort(grades)

    with open("result.txt", "w", encoding="utf-8") as file:
         # Клянусь, результат та студентів файли я не трогав, але чогось
         # у "Ivanenko Anna" (перша строка) добавляє 6 символів зпочатку. Я не знаю з чим це зв'язано взагалі,,,
         # Надіюсь це не помилка!!! Я копіював текст вручну, бо класрум не давав самі файли взяти
         for item in sortedGrades:
             file.write(f"{item[0]};{item[1]}\n")

#4
if not os.path.exists("report.txt"):
    grades = dict()
    sortedGrades = []
    gradeAmount = []

    best = []
    highestAverage = 0

    with open("grades.csv", "r", encoding="utf-8") as file:
        for line in file:
            name, subject, value = line.strip().split(';')
            if grades.get(name):
                grades[name].append(int(value))
            else:
                grades[name] = [int(value)]

        gradeAverages = []
        for name, values in grades.items():
            average = sum(values) / len(values)
            gradeAverages.append((name, average))
            if average > highestAverage:
                highestAverage = average
                best = [name]
            elif average == highestAverage:
                best.append(name)

        sortedGrades = sort(gradeAverages)
        counter = 0
        for item in sortedGrades:
            sortedGrades[counter] = (item[0], item[1], len(grades.get(item[0])))
            counter += 1

    with open("report.txt", "w", encoding="utf-8") as file:
        for item in sortedGrades:
            file.write(f"{item[0]} -- оцінок: {item[2]} -- середня: {item[1]}\n")
        file.write(f"Найкращий результат: {" та ".join(best)}, -- {highestAverage}")