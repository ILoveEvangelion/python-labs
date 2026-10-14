import random

def generateGrades(count):
    if count <= 0:
        print("Кількість оцінок має бути більше нуля")
        return []

    grades = []
    for i in range(count):
        grades.append(random.randint(1, 12))
    return grades

def averageGrades(grades):
    return sum(grades) / len(grades)

def gradeLevel(average):
    if average >= 10:
        return "високий"
    elif average >= 7:
        return "достатній"
    elif average >= 4:
        return "середній"
    else:
        return "початковий"