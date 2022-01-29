# -- coding: utf-8 --

from tkinter import *
from tkinter import messagebox


def N1():
    arg = txt.get()
    i = 1
    N = int(txt.get())
    result = ""
    while i ** 2 <= N:
        result += str(i ** 2) + ' '
        i += 1
    messagebox.showinfo('Результат', result)

def N3():
    arg = txt2.get()
    N = int(txt2.get())
    i = 0
    a = 1
    while a * 2 <= N:
        a *= 2
        i += 1
    messagebox.showinfo('Результат', "Показатель степени: " + str(i) + " " + "число: " + str(a))

l2 = 0
S = 0


def N6():
    global l2
    global S
    arg = int(txt5.get())
    if arg != 0:
        l2 += 1
        S += arg
    else:
        messagebox.showinfo('Результат', S / l2)
        l2 = 0
        S = 0
    txt5.delete(0, END)

window = Tk()
window.title("Добро пожаловать в практическую работу №6")
window.geometry('600x300')
lbl = Label(window, text="Введите целое число -> ")
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
btn = Button(window, text="N5.1", command=N1)
btn.grid(column=2, row=0)

lbl2 = Label(window, text="Введите натуральное число -> ")
lbl2.grid(column=0, row=2)
txt2 = Entry(window, width=10)
txt2.grid(column=1, row=2)
btn2 = Button(window, text="N5.3", command=N3)
btn2.grid(column=2, row=2)

lbl5 = Label(window, text="Введите числа по одному. Чтобы завершить, введите 0")
lbl5.grid(column=0, row=5)
txt5 = Entry(window, width=10)
txt5.grid(column=1, row=5)
btn5 = Button(window, text="N5.6", command=N6)
btn5.grid(column=2, row=5)

window.mainloop()