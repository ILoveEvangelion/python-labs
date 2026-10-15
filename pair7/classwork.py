import os

if not os.path.exists('text.txt'):
    with open('text.txt', 'w', encoding="utf-8") as file:
        file.write("Python - популярна мова програмування.\n")
        file.write("Python використовується для роботи з даними.\n")
        file.write("Файли дозволяють зберігати інформацію\n")
        file.write("Python вимагає практики.\n")
        file.write("Сьогодні ми працюємо з текстовими файлами.\n")

if not os.path.exists('numbers.txt'):
    with open('numbers.txt', 'w', encoding="utf-8") as file:
        file.write("12\n8\n25\n4\n16\n")

if not os.path.exists('students.txt'):
    with open('students.txt', 'w', encoding="utf-8") as file:
        file.write("Ivanenko Anna;91\n")
        file.write("Leshchenko Ivan;76\n")
        file.write("Komarova Sophie;97\n")
        file.write("Bondarenko Illya;84\n")

if not os.path.exists('grades.csv'):
    with open('grades.csv', 'w', encoding="utf-8") as file:
        file.write("Anna;Python;11\n")
        file.write("Anna;Math;10\n")
        file.write("Ivan;Python;6\n")
        file.write("Ivan;Math;5\n")
        file.write("Sophie;Python;11\n")
        file.write("Sophie;Math;12\n")
        file.write("Illya;Python;9\n")
        file.write("Illya;Math;8\n")

# with open("hello.text", "w", encoding="utf-8") as file:
#     file.write("Hello world2!\n")
#     file.write("Hello world3!\n")
#     file.write("Hello world4!\n")

#w - write
#r - read
#a - append
#x - create

# with open("text.text", "r", encoding="utf-8") as file:
#     text = file.read()
# print(f'read() => \n{text} \nlen() => {len(text)}')

# with open("text.txt", "r", encoding="utf-8") as file:
#     line1 = file.readline()
#     otherLines = file.readlines()
#     line2 = file.readline()
# print(line1, otherLines, line2)

# with open("text.txt", "r", encoding="utf-8") as file:
#     otherLines = file.readlines()
# for line in otherLines:
#     print(line)

# with open("text.txt", "r", encoding="utf-8") as file:
#     for n, line in enumerate(file, 1):
#         clean = line.strip()
#         print(f'{n}. {clean}')

# line = "Kurinenko Andriy;2\n"
# clean = line.strip()
# name, grade = clean.split(';')
# print(name, grade)

# students = []
# botanics = []
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         name, grade = line.strip().split(';')
#         students.append([name, grade])
#         if int(grade) >= 90:
#             botanics.append([name, grade])
# print(students)
# print(botanics)
#
# with open("botanics.txt", "w", encoding="utf-8") as file:
#     for student in botanics:
#         file.write(f"{student[0]};{student[1]}\n")

# grades = []
# with open("grades.csv", "r", encoding="utf-8") as file:
#     for line in file:
#         name, subject, grade = line.strip().split(';')
#         grades.append(int(grade))
#         print(f'{name} - {subject} - {grade}')
# print(sum(grades) / len(grades))