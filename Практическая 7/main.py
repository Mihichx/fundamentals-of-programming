def ex1():
    print("Задание 1")

    value = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value1 = []
    result = []
    for number in value:
        if number % 2 == 0:
            result.append(number)
        else:
            value1.append(number)

    value1 = value1[::-1]
    for number in value1:
        result.append(number)

    print(result)


def ex2():
    print("Задание 2")

    value = [20, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    result = []

    for number in value:
        if number % 5 == 0:
            result.append(number)

    len_result = len(result)

    for i in range(len_result):
        for j in range(i + 1, len_result):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    print(result)


def ex3():
    print("Задание 3")

    value = [20, 15, 1, 2, 3, 1, 5, 6, 7, 8, 30, 10, 11, 12, 13, 14]
    len_value = len(value)
    min_value_index = max_value_index = 0
    result = 0

    for i in range(len_value):
        if value[i] < value[min_value_index]:
            min_value_index = i
        elif value[i] > value[max_value_index]:
            max_value_index = i

    for j in range(min_value_index, max_value_index + 1):
        result += value[j]
        value[j] = 0

    print(value)
    print(result)


def ex4():
    print("Задание 4")

    value = [20, 15, 1, 2, 3, 1, 5, 6, 7, 8, 30, 10, 11, 12, 13, 14]
    len_value = len(value)
    value1 = value.copy()
    min_value_index = max_value_index = 0

    for i in range(len_value):
        if value[i] < value[min_value_index]:
            min_value_index = i
        elif value[i] > value[max_value_index]:
            max_value_index = i

    for j in range(min_value_index + 1, max_value_index):
        value[j] = value[j] * 2

    print(value1)
    print(value)


def ex5():
    print("Задание 5")

    value = [20, 15, 1, 2, 3, 1, 5, 6, 7, 8, 30, 10, 11, 62, 13, 14]
    len_value = len(value)
    value1 = []

    for i in range(len_value):
        if 10 <= value[i] <= 99:
            value1.append(value[i])

    len_value1 = len(value1)

    for i in range(len_value1):
        for j in range(i + 1, len_value1):
            number = int(str(value1[i])[0])
            number_next = int(str(value1[j])[0])
            if number < number_next:
                value1[i], value1[j] = value1[j], value1[i]

    print(value1)


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
