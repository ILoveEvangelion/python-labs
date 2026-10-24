import os

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

class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        print("name: ", self.name)

#1
class Student(Person):
     def __init__(self, name, group):
         super().__init__(name)
         self.group = group
         self.grades = []

     def add_grade(self, grade):
         if grade < 1 or grade > 12:
             print("Оцінка має бути в діапазоні 1..12")
             return
         self.grades.append(grade)

     def average(self):
         if len(self.grades) == 0:
             return 0
         return sum(self.grades) / len(self.grades)

     def info(self):
         print("name: ", self.name, ", group: ", self.group)

# Student("Ivan", "IT-17").info()
# Student("Mikhail", "IT-17").info()

#2
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        print("name: ", self.name, ", subject: ", self.subject)

# people = [Person("Вадим"), Student("Ліза", "N/A"), Teacher("Іван", "IT")]
# for person in people:
#     person.info()

#3
class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        for v in self.students:
            if v.name == student.name:
                print("Цей студент уже присутній")
                return

        self.students.append(student)

    def remove_student(self, name):
        for v in self.students:
            if v.name == name:
                self.students.remove(v)

    def find_student(self, name):
        for v in self.students:
            if v.name == name:
                return v
        return None

    def add_grade_to_student(self, name, grade):
        added = False
        for v in self.students:
            if v.name == name:
                added = True
                v.add_grade(grade)
                return

        if not added:
            print("Такого учня не існує!!!")

    def show_rating(self):
        values = []
        for s in self.students:
            values.append((s.name, s.average()))

        sortedValues = sort(values)
        for v in sortedValues:
            print(v[0], ": ", v[1])

    def show_students(self):
        for v in self.students:
            v.info()

# ourCourse = Course("IT", Teacher("Іван", "IT"))
# ourCourse.add_student(Student("Вадим", "IT-17"))
# ourCourse.add_student(Student("Вадим", "IT-17"))
# ourCourse.remove_student("Вадим")
# ourCourse.add_student(Student("Вадим", "IT-17"))
# ourCourse.add_student(Student("Ліза", "IT-17"))
# ourCourse.add_student(Student("Максим", "IT-17"))
# ourCourse.add_student(Student("даттебайо", "IT-17"))
# ourCourse.show_students()

#4
ourCourse = Course("IT", Teacher("Іван", "IT"))
if os.path.exists("course_data.txt"):
    with open("course_data.txt", "r") as f:
        for line in f:
            studentData, gradeData = line.strip().split(";")
            name, group = studentData.split(",")
            grades = [int(g) for g in gradeData.split(",")]
            ourCourse.add_student(Student(name, group))
            for g in grades:
                ourCourse.add_grade_to_student(name, g)

while True:
    cmd = input("Введіть команду для виконання: (1-7, 0 для виходу): ")
    if cmd == "0":
        break
    elif cmd == "1":
        ourCourse.show_students()
    elif cmd == "2":
        name, group = input("Введіть ім'я та группу студента через кому: ").strip().split(",")
        ourCourse.add_student(Student(name.strip(), group.strip()))
    elif cmd == "3":
        name = input("Введіть ім'я студента для видалення: ").strip()
        ourCourse.remove_student(name)
    elif cmd == "4":
        name = input("Введіть ім'я студента для знаходження: ").strip()
        student = ourCourse.find_student(name)
        if student:
            student.info()
        else:
            print("Такого студента не існує!!!")
    elif cmd == "5":
        name = input("Введіть ім'я студента для виставлення оцінки: ").strip()
        grade = int(input("Введіть оцінку для виставлення учневі: "))
        ourCourse.add_grade_to_student(name, grade)
    elif cmd == "6":
        ourCourse.show_rating()
    elif cmd == "7":
        with open("course_data.txt", "w") as f:
            for student in ourCourse.students:
                f.write(f"{student.name},{student.group};{",".join(map(str, student.grades))}")
            print("Дані успішно записані!!!")
