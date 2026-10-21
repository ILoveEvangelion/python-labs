# # bookDict = {
# #     "title": "Kobzar",
# #     "author": "Taras Schevchenko",
# #     "copies": 15
# # }
# # print(bookDict["title"])
#
# class Book:
#     def __init__(self, title, price, copies):
#         self.title = title
#         self.price = price
#         self.copies = copies
#
#     def available(self):
#         return self.copies > 0
#
# book1 = Book("Kobzar", 450, 15)
# book2 = Book("Lisova pisnya", 500, 0)
# # print(book1.title, book1.price)
# # print(book2.title, book2.price)
#
# print(book1.available())
# print(book2.available())

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def info(self):
        print(f"Rectangle with width {self.width} and height {self.height}")
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")