class Person:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(self.name)

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
    def info(self):
        print(self.name, " : ", self.group)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    def info(self):
        print(self.name, " : ", self.subject)

# person = Person("Vadym")
# student = Student("Lisa", "N/A")

people = [Person("Vadym"), Student("Lisa", "N/A"), Teacher("Ivan", "IT")]
for person in people:
    person.info()

person = Person("Vadym")
print(isinstance(person, Person))