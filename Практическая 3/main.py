import random

#Задание 1-2
print("Задание 1-2")

value = int(input())
value_str = str(value)
flag = 0
flag1 = 0
revers_value = 0

for i in range(len(value_str)):
    past_char = value_str[i]
    if value_str[i] == "5":
        flag = 1
    try:
        if past_char == value_str[i + 1]:
            flag1 = 1
    except:
        pass

if flag == 1:
    while value > 0:
        digit = value % 10
        revers_value = (revers_value * 10) + digit
        value = value // 10
    print(f"Перевёрнутый результат: {revers_value}")
else:
    print(f"Результат: {value}")

if flag1 == 1:
    print("Есть повторяющиеся цифры")

#Задание 3
print("\nЗадание 3")

birthday = list(map(int, input("Введите свой день рождения через пробел 'день месяц': ").split()))
zodiac = ""

def zodiac_sign(birthday, mount, mount1, day, day1, day2, day3):
    return (birthday[1] == mount and day <= birthday[0] <= day1) or (birthday[1] == mount1 and day2 <= birthday[0] <= day3)

if zodiac_sign(birthday, 12, 1, 22, 31, 1, 19):
    zodiac = "Козерог"
elif zodiac_sign(birthday, 1, 2, 20, 31, 1, 18):
    zodiac = "Водолей"
elif zodiac_sign(birthday, 2, 3, 19, 28, 1, 20):
    zodiac = "Рыбы"
elif zodiac_sign(birthday, 3, 4, 21, 31, 1, 19):
    zodiac = "Овен"
elif zodiac_sign(birthday, 4, 5, 20, 30, 1, 20):
    zodiac = "Телец"
elif zodiac_sign(birthday, 5, 6, 21, 31, 1, 20):
    zodiac = "Близнецы"
elif zodiac_sign(birthday, 6, 7, 21, 30, 1, 22):
    zodiac = "Рак"
elif zodiac_sign(birthday, 7, 8, 23, 31, 1, 22):
    zodiac = "Лев"
elif zodiac_sign(birthday, 8, 9, 23, 31, 1, 22):
    zodiac = "Дева"
elif zodiac_sign(birthday, 9, 10, 23, 30, 1, 22):
    zodiac = "Весы"
elif zodiac_sign(birthday, 10, 11, 23, 31, 1, 21):
    zodiac = "Скорпион"
elif zodiac_sign(birthday, 11, 11, 22, 30, 1, 21):
    zodiac = "Стрелец"
else:
    zodiac = "Не правильные ввод"

print(f"Твой знак зодиака: {zodiac}")

#Задание 4
print("\nЗадание 4")

experience = float(input("Введите стаж работы: "))
salary = int(input("Введите ваш оклад: "))

if 5 < experience <= 10:
    salary += (salary * 10) / 100
elif 10 < experience <= 15:
    salary += (salary * 15) / 100
elif 15 < experience:
    salary += (salary * 20) / 100   

print(f"Ваш оклад составит {salary}")

#Задание 5
print("\nЗадание 5")

x = random.randint(1, 9)
y = random.randint(1, 9)

result = x * y
answer = int(input(f"Решите {x} * {y} и введите ответ: "))

if result == answer:
    print("Правильно")
else:
    print("Не правильно")
