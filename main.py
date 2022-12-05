import math

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
print("Сумма =", a + b)
print("Разность =", a - b)
print("Умножение =", a * b)
print("Деление =", a / b)
print("Возведение в степень =", a ** b)
print("Деление по модулю =", a % b)
print("Целочисленное деление =", a // b)

name = input("Введите имя: ")
print('Привет, {}!'.format(name))

text = input("Введите текст: ")
print(text[-1] + text[-2])

R = float(input("Введите радиус круга: "))
print("Площадь круга = {:.2f}".format(math.pi * (R ** 2)))
