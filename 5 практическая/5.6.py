# -- coding: utf-8 --
sum = 0
length = 0
element = int(input('Введите числа: '))
while element != 0:
    sum += element
    length += 1
    element = int(input())
print(sum / length)