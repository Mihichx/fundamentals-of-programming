def function1():
    print("Задание 1")
    
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    quality = 0

    if a < b:
        while b >= a:
            print(b)
            b -= 1
            quality += 1
        print(f"Кол-во чисел: {quality}")
    else:
        print("Не соблюдены условия задания A < B")

def function2():
    print("Задание 2")

    day = 1
    lim_day = 7 
    distance = 10 # км
    progress = 10 # процент
    flag = 0

    while day <= lim_day:
        distance += (distance * progress) / 100
        if distance > 15 and flag == 0:
            flag = day
        day += 1

    print(f"За {lim_day} дней лыжник пробежал {round(distance)}км. На {flag} день пробежал > 15км.")

def function3():
    print("Задание 3")

    value = 10
    result = 0

    while value < 100:
        if 10 >= int(str(value)[0]) + int(str(value)[1]):
            result += value
        value += 1

    print(result)

def function4():
    print("Задание 4")

    P = int(input("Введите значение P: ")) # товаров в первый день
    Q = int(input("Введите значение Q: ")) # на Q больше каждый день
    T = int(input("Введите значение T: ")) # запланированный объём 
    day = 0

    while P < T:
        P += Q
        day += 1

    print(f"Потребовалось {day} дней(я) для выполнения плана")

def function5():
    print("Задание 5")

    A = int(input("Введите первое число: "))
    B = int(input("Введите второе число: "))

    while A > B:
        if A % 2 == 0 and A != B:
            A = A / 2
            print(":2", A)
        elif A % 2 != 0:
            print(":2 ошибка")
            A -= 1
            print("-1", A)

    print(f"Ответ {A:.0f}")

     

if __name__ == "__main__":
    # function1()
    # print("\n")
    # function2()
    # print("\n")
    function3()
    print("\n")
    # function4()
    # print("\n")
    # function5()
    # print("\n")
