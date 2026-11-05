def ex1():
    print("Задание 1")

    s = {"яблоки": 3, "бананы": "много", "груши": 5, "апельсины": 2}
    result = 0

    for i in s:
        value = s[i]
        if isinstance(value, int):
            result += value**2

    print(result)


def ex2():
    print("Задание 2")

    s = {"яблоки": 3, "бананы": "много", "груши": 5, "апельсины": 2}
    value = str(input("Введите букву: "))

    for i in list(s):
        if i[0] != value[0]:
            s.pop(i)

    print(s)


def ex3():
    print("Задание 3")

    s = {1: 7, 2: 15, 3: 23}
    result = ""

    for i in s:
        result += str(s[i])

    result = result[::-1]

    print(result)


def ex4():
    print("Задание 4")

    n = int(input("Введите число: "))
    s = {i: i**2 for i in range(1, n + 1)}

    print(s)


def ex5():
    print("Задание 5")

    s = {"физика": 85, "математика": 98, "программирование": 92, "химия": 74}

    print("a")
    print(max(s.values()), min(s.values()))

    print("b")
    for key in s.keys():
        print(key)

    for value in s.values():
        print(value)

    print("c")
    s = {"x": list(range(11, 21)), "y": list(range(21, 31)), "z": list(range(31, 41))}

    print(s)
    for i in s:
        print(s[i][4])


if __name__ == "__main__":
    value = int(input("Введите номер задания или 0: "))

    print("\n")
    if value == 1:
        ex1()
    elif value == 2:
        ex2()
    elif value == 3:
        ex3()
    elif value == 4:
        ex4()
    elif value == 5:
        ex5()
    else:
        print("\n")
        ex1()
        print("\n")
        ex2()
        print("\n")
        ex3()
        print("\n")
        ex4()
        print("\n")
        ex5()
