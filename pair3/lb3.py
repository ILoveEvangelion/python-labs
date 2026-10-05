import string

#1
#text = input("Введіть текст: ")

#letters = 0
#digits = 0
#spaces = 0
#vowels = 0

#голосні, англійські та українські
#vowels = "aeiouyаеєиіїоуюя"

#for char in text:
#    if char.isalpha():
#        letters += 1
#        if char.lower() in vowels:
#            vowels += 1
#    elif char.isdigit():
#        digits += 1
#    elif char.isspace():
#        spaces += 1

#words = len(text.split())

#print("Символів:", len(text))
#print("Літер:", letters)
#print("Цифр:", digits)
#print("Пробілів:", spaces)
#print("Голосних:", vowels)
#print("Слів:", words)

#2
#text = input("Введіть прізвище, ім'я та по батькові: ")

#parts = text.split()
#if len(parts) == 3:
#    name1, name2, name3 = parts
#    result = f"{name1.capitalize()} {name2[0].upper()}.{name3[0].upper()}."
#    print(result)

#3
#text1 = input("Введіть перший рядок: ")
#text2 = input("Введіть другий рядок: ")

#normalised1 = text1.replace(" ", "").lower()
#normalised2 = text2.replace(" ", "").lower()

#is_anagram = normalised1 == normalised2[::-1]

#if is_anagram:
#    print("Рядки є анаграмами")
#else:
#    print("Рядки не є анаграмами")

#4
text = input("Введіть речення: ")

parts = text.split()

#я ДУЖЕ ДУЖЕ сильно не хотів робити декілька циклів for, тому я використав linq, щоб красиво та зручно було
words = [w.strip(string.punctuation) for w in parts]

#на випадок якщо пунктуаційні знаки відокремлено пробілом ("Привіт !"), щоб пустих слів не було
words = [w for w in words if w]

if words:
    max_len = max(len(w) for w in words)
    min_len = min(len(w) for w in words)

    longest = []
    shortest = []
    for w in words:
        if len(w) == max_len and w.lower() not in [x.lower() for x in longest]:
            longest.append(w)
        if len(w) == min_len and w.lower() not in [x.lower() for x in shortest]:
            shortest.append(w)

    special = [w.lower() for w in words]

    print("Найдовші:", ", ".join(longest))
    print("Найкоротші:", ", ".join(shortest))
    print("Унікальних слів:", len(special))

    old = input("Яке слово замінити? ")
    new = input("На яке слово замінити? ")

    result = []
    for char in parts:
        core = char.strip(string.punctuation)
        if core and core.lower() == old.lower():
            start = char.index(core)
            char = char[:start] + new + char[start + len(core):]
        result.append(char)

    print("Після заміни:", " ".join(result))