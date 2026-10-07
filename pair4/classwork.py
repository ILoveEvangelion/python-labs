#list
#grades = [12, 4, 6, 9]
#numbers = []
#numbers2 = list()
#print(grades[2])
#print(grades[5])
#print(len(grades))
#print(grades[len(grades)-1])

#numbers.append(5)
#numbers.append(6)
#numbers.append("6")
#numbers.insert(1, 2)
#numbers.insert(10, 2)
#numbers.extend([5, 6, 5, "4"])
#if "6" in numbers:
#    numbers.remove("6")

#numbers.pop(-1)

#del numbers[1]
#del numbers

#numbers.clear()
#print(numbers.count(5))
#print(numbers.index(6))

#print(2 in numbers)
# len()
# min()
# max()
# sum()
#if len(numbers) > 0:
#    average = sum(numbers) / len(numbers)

#numbers.sort()
#print(numbers)
#numbers.sort(reverse=True)
#print(numbers)

#print(numbers)
#numbers.reverse()

#print(numbers[1:3])
#print(numbers[::-1])
#print(numbers[::2])

#for number in numbers:
#    print(number)

#print(numbers)

#digits = [-1, 0, 4, -5, 3, -6]
#positive = []
#even = []
#for digit in digits:
#    if digit > 0:
#        positive.append(digit)
#    if digit % 2 == 0:
#        even.append(digit)
#print(positive)

#tuple
#rgb = (255, 0, 0)
#r, g, b = rgb

#data = ()
#a = (1,)
#rgb[1] = 255

#point = (4, -6)
#point = point + (4,)
#print(point)

#a = (30, 40)
#b = (50, 60)
#c = a + b
#c = a[:1] + b[::]
#print(c)
#c.count()
#c.index()

#set
#subjects = {"Python", "HTML", "CSS", "JavaScript"}
#print(subjects)

#data = {}
#print(type(data))
#data2 = set()
#data2.add("C++")
#data2.update(["C", "C#"])

#data2.remove("HTML")
#data2.discard("C++")

#data2.pop()
#data2.clear()

#if "Python" in data2:
#    print("111")

#dictionary
#student = {
#    "name": "John",
#    "age": 67
#}

#names = ["Ivan", "Olha", "Vadym", "Ivan", "Irina"]
#new_names = set(names)
#print(new_names)

#names1 = {"Ivan", "Olha", "Vadym"}
#names2 = {"Ivan", "Irina"}

#names3 = names1 | names2
#names4 = names1 & names2
#names5 = names1 - names2
#names6 = names2 - names1

#print(names3)
#print(names4)
#print(names5)
#print(names6)

#products = ["bread", "milk", "apple", "banana"]
#prices = [30, 50, 50, 80]

#prices = {"bread": 30, "milk": 50, "apple": 50, "banana": 80}
#student = {}
#student2 = dict()

#prices["tea"] = 76
#prices["bread"] = 45
#prices.update({
#    "juice": 60,
#    "water": 100,
#    "larp": 77
#})

#deleted = prices.pop("milk")

#.items()
#.get()
#.value()
#.key()

#for key, value in prices.items():
#    print(key, value)

#print(prices["bread"])
#print(prices)