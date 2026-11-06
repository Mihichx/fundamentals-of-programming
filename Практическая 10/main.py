def ex1():
    print("Задание 1")

    set1 = "привет"
    set2 = "тевирп"

    if set(set1) == set(set2):
        print("True")
    else:
        print("False")


def ex2():
    print("Задание 2")

    set1 = set("Привет")
    set2 = set("ивет")

    set1.difference_update(set2)

    print(set1)


def ex3():
    print("Задание 3")

    num1 = 123456
    num2 = 246

    set1 = set(str(num1))
    set2 = set(str(num2))

    if set2.issubset(set1):
        print("True")
    else:
        print("False")


def ex4():
    print("Задание 4")

    num1 = 987321
    num2 = 12345

    common_digits = set(str(num1)) & set(str(num2))

    if common_digits:
        result_num = int("".join(sorted(common_digits)))
        print("Число из общих цифр:", result_num)
    else:
        print("Общих цифр нет")


def ex5():
    print("Задание 5")

    set1 = {1, 2, 3}
    set2 = {2, 3, 4}
    set3 = {5, 6, 7}

    set3 = set1 & set2 | set3

    print(set3)


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
