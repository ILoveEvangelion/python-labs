import math
from math import *
import statistics as stat
import random
from datetime import date
import demo
from tkinter import *

# print(math.sqrt(81))
#
# a = [10, 15, 3, 5, 8, 9]
# print(stat.mean(a))
#
# r = int(input())
# S = round(pi * pow(r, 2), 2)
# print(S)

# balls = 37
# n = 6
#
# print(f'full: {floor(balls / n)}, total: {ceil(balls / n)}')

# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 100))
# print(numbers)
#
# selected = random.choice(numbers)
# print(selected)
#
# print(date.today())
#
# print(demo.square(5))
# print(demo.even(7))
# grades = [12, 5, 7, 9]
# print(demo.average(grades))

latestLabel = None
def text():
    global latestLabel
    if latestLabel is None:
        text = "Thanks, I'm full."
        latestLabel = Label(frame, text=text, font=("Arial", 18), bg="black", fg="white")
        latestLabel.grid(row=2, column=0)

def hideText(event):
    global latestLabel
    if latestLabel is not None:
        latestLabel.destroy()
        latestLabel = None

window = Tk()
window.title('1')
window.geometry('500x400')
window.resizable(False, False)
window["bg"] = "black"

label = Label(window, text="Let's larp!", font=("Arial", 18), bg="black", fg="white")
# label.place(x=200, y=175)
label.pack()
frame = Frame(window, bg="black")
frame.pack()

bt1 = Button(frame, text="Just this once.", width=25, activebackground="gray", command=text)
bt1.grid(row=0, column=0, padx=10)
bt2 = Button(frame, text="This is what dessert tastes like!", width=25, activebackground="gray")
bt2.grid(row=1, column=0, padx=10)
bt2.bind("<Button-1>", hideText)

window.mainloop()