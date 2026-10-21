from random import randint

#1
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def perimeter(self):
#         return 2 * (self.width + self.height)
#
#     def area(self):
#         return self.width * self.height
#
#     def info(self):
#         print(f"Прямокутник {self.width}х{self.height}")
#         print(f"Периметр: {self.perimeter()}")
#         print(f"Площа: {self.area()}")
#
# Rectangle(5, 3).info()
# Rectangle(10, 4).info()

#2
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def __str__(self):
#         return f"{self.name}: [{", ".join(map(str, self.grades))}]; середнє: {self.average()}"
#
#     def add_grade(self, grade):
#         if grade < 1 or grade > 12:
#             print("Оцінка ", grade, " не додається")
#             return
#         self.grades.append(grade)
#
#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         else:
#             return sum(self.grades) / len(self.grades)

# student = Student("Ivan Petrenko")
# student.add_grade(10)
# student.add_grade(12)
# student.add_grade(15)
# student.add_grade(9)
# print(student)

#3
# students = []
#
# def add_student(name):
#     student = Student(name)
#     for i in range(randint(1, 5)):
#         student.add_grade(randint(0, 15))
#
#     students.append(student)
#     return student
#
# student1 = add_student("Ivan Petrenko1")
# student2 = add_student("Ivan Petrenko2")
# student3 = add_student("Ivan Petrenko3")
# student4 = add_student("Ivan Petrenko4")
# student5 = add_student("Ivan Petrenko5")
#
# best = []
# bestAverage = 0
# for student in students:
#     average = student.average()
#     if average > bestAverage:
#         best = [student.name]
#         bestAverage = average
#     elif average == bestAverage:
#         best.append(student.name)
#     print(student)
#
# print(f"Найкращий(-і) результат(и): {", ".join(map(str, best))} -- {bestAverage}")

#4
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            print("+", amount)
            self.balance += amount
        else:
            print("Помилка: сума депозиту має бути більшою за нуль")

    def withdraw(self, amount):
        if amount <= 0:
            print("Помилка: сума спису має бути більшою за нуль")
            return
        if amount > self.balance:
            print("Помилка: сума спису не може бути більшою за поточний баланс")
            return
        print("-", amount)
        self.balance -= amount

    def info(self):
        print(f"Гаманець за іменем {self.owner}: {self.balance} грн")

bank1 = BankAccount("Ivan", 1000)
bank1.deposit(500)
bank1.deposit(-500)
bank1.withdraw(500)
bank1.withdraw(-1000)

bank2 = BankAccount("Petya", 2000)
bank2.withdraw(3000)
bank2.deposit(1000)
bank2.withdraw(3000)

bank1.info()
bank2.info()