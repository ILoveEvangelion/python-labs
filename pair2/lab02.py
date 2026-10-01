#1

#n = int(input())
#count = 0
#suma = 0
#for i in range(1, n+1):
#    if i % 3 == 0 or i % 5 == 0:
#        count += 1
#        suma += i

#if count != 0:
#    avr = suma / count
#    print(count, suma, avr)

#2

#n = int(input())
#count = 0
#suma = 0
#minN = 0
#maxN = 0

#while n > 0:
#    num = n % 10
#    if num > maxN:
#        maxN = num
#    elif num < minN:
#        minN = num
#    n //= 10
#    count += 1
#    suma += num

#print(count, suma, minN, maxN)

#3

#n = int(input())
#last = 0

#for i in range(1, n+1):
#    last = i
#    sc = True
#    while last > 0:
#        digit = last % 10
#        if digit == 0 or i % digit != 0:
#            sc = False
#            break
#        last //= 10
#    if sc:
#        print(i)

#4

#width = int(input("width "))
#height = int(input("height "))
#border = input("ramka ")
#inside = input("vseredyni ")

#for i in range(1, height+1):
#    for j in range(1, width+1):
#        if i == 1 or i == height or j == 1 or j == width:
#            print(border, end="")
#        else:
#            print(inside, end="")
#    print()