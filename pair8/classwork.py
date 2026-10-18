# try:
#     age = int(input("age: "))
#     print("Your age is: ", age)
# except ValueError:
#     print("no fuck you")

# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     result = a / b
#     print(result)
# except ValueError:
#     print("a and b must be integers")
# except ZeroDivisionError:
#     print("b cannot be zero")
# finally:
#     print("done")

# while True:
#     try:
#         grade = int(input("grade: "))
#         if grade < 1 or grade > 12:
#             raise ValueError("grade must be between 1 and 12")
#         print("grade set: ", grade)
#         break
#     except ValueError as e:
#         print(f"error: {e}")

# def intInput(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print("Please enter a valid integer")
#
# n = intInput("Enter a number: ")
# print(n)

# def inputGrade(prompt):
#      while True:
#          try:
#              grade = int(input(prompt))
#              if grade < 1 or grade > 12:
#                  raise ValueError("Grade must be between 1 and 12")
#              return grade
#          except ValueError as e:
#              print(e)
#
# n = inputGrade("Enter a number: ")
# print(n)

price = {
    "apple": 0.49,
    "banana": 0.5
}

# product = input("Enter a product: ")
# try: print(price[product])
# except KeyError: print("Product not found")

# product = input("Enter a product: ")
# actualPrice = price.get(product, "Product not found")

# try:
#     with open("data.txt", "r", encoding="utf-8") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found")

# line = "Ivan;95"
# parts = line.strip().split(";")
# if len(parts) != 2:
#     print("Invalid format")
# else:
#     name, grade = parts
#     try:
#         grade = float(grade)
#         if grade < 0 or grade > 100:
#             raise ValueError("Grade must be between 0 and 100")
#
#     except ValueError as e:
#         print("Invalid grade: ", e)
#     else:
#         print(f"Name: {name}, Grade: {grade}")

lines = [
    "Ivan;95",
    "Liza;hello",
    "Vadymka;100"
]
for index, line in enumerate(lines, 1):
    parts = line.strip().split(";")
    if len(parts) != 2:
        print(f"Invalid format on line {index}")
        continue

    name, grade = parts
    try:
        grade = int(grade)
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100")
    except ValueError:
        print(f"Invalid grade on line {index}: {grade}")
        continue

    print(f"Name: {name}, Grade: {grade}")
