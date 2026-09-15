from math import sin, cos, sqrt, pi

#Задание 1

print("Задание 1")
x = float(input("Введите значение x: "))
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))

def f1(x):
    y = 3 * x + sin(x + 2)
    return y

def f2(x, a):
    y = a * x + cos(2 * x + 1)
    return y

def f3(x, a, b):
    y = a * x + b * sin(2 * x + 2)
    return y

def f4(x, a):
    y = a * x**3 + cos(3 * x + 1) 
    return y

def f5(x, a):
    y = x**2 / a + cos(2 * x - 1)
    return y

def f6(x, a):
    y = x / a + 2 * x
    return y

def f7(x):
    y = 3 * x - 2 * x + 1
    return y

def f8(x):
    y = 1 / 2 * x - 3 * x + 1
    return y

def f9(x, a):
    y = 1 / (x**2 + 1) - a
    return y

def f10(x, a):
    y = a / (x**2 + 1) - cos(2 * x - 1)
    return y

def f11(x):
    y = x**3 - 2 * x + 4
    return y

def f12(x, a, b):
    y = a * x + b * x**3 - 8
    return y

def f13(x, a, b):
    y = a * sqrt(x + 4) - b
    return y

def f14(x):
    y = cos(2 * x - 1) + sin(x)
    return y

def f15(x, a, b):
    y = a * sqrt(x) + b * x
    return y

print(
    f"\nФункция 1: {f1(x)}\n"
    f"Функция 2: {f2(x, a)}\n"
    f"Функция 3: {f3(x, a, b)}\n"
    f"Функция 4: {f4(x, a)}\n"
    f"Функция 5: {f5(x, a)}\n"
    f"Функция 6: {f6(x, a)}\n"
    f"Функция 7: {f7(x)}\n"
    f"Функция 8: {f8(x)}\n"
    f"Функция 9: {f9(x, a)}\n"
    f"Функция 10: {f10(x, a)}\n"
    f"Функция 11: {f11(x)}\n"
    f"Функция 12: {f12(x, a, b)}\n"
    f"Функция 13: {f13(x, a, b)}\n"
    f"Функция 14: {f14(x)}\n"
    f"Функция 15: {f15(x, a, b)}\n"
)

#Задание 2

print("Задание 2")
R = float(input("Введите радиус: "))

L = 2 * pi * R
S = pi * R**2

print(f"Длинна: {L}\nПлощадь: {S}\n")

#Задание 3

print("Задание 3")
number1 = int(input("Введите число 1: "))
number2 = int(input("Введите число 2: "))
number3 = int(input("Введите число 3: "))

print(f"{number1}{number2}{number3}\n")

#Задание 4

print("Задание 4")
km = float(input("Введите расстояние в км: "))
benz = float(input("Введите кол-во потребления бензина на 100км: "))
price = float(input("Введите цену бензина за литр: "))

result_price = ((km * 2) * (benz / 100)) * price

print(result_price, "\n")

#Задание 5

print("Задание 5")
curs_usd = float(input("Введите курс доллара: "))
sum_usd = float(input("Введите сумму в долларах: "))

result = curs_usd * sum_usd
rubles = int(result)
kop = int((result - rubles) * 100)


print(f"{rubles} руб. {kop} коп.")
