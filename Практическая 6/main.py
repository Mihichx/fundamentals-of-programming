def function1():
    print("\nЗадание 1")

    value = str(input("Введите предложение: "))
    value += " 0"
    words = ""
    flag = 0
    result = 0

    for i in range(len(value)):
        if value[i] == " ":
            continue
        if value[i - 1] == " ":
            for j in range(len(words)):
                if words[j] == "А" and flag != 1:
                    result += 1
                    flag = 1
            flag = 0
            words = ""
        words += value[i]

    print(result)


def function2():
    print("\nЗадание 2")

    value = str(input("Введите слово: "))
    result1 = ""
    result2 = ""

    for i in range(len(value)):
        if i % 2 != 0:
            result1 += value[i]
        elif i % 2 == 0:
            result2 += value[len(value) - i - 1]
    result = result1 + result2

    print(result)


def function3():
    print("\nЗадание 3")

    value = str(input("Введите путь: "))
    word = ""
    flag = 0

    for i in range(len(value)):
        if value[i] == ".":
            break
        word += value[i]
        if value[i] == "/":
            word = ""

    print(word)


def function4():
    print("\nЗадание 4")

    value = str(input("Введите текст: "))

    if len(value) >= 3:
        if (
            value[len(value) - 3] == "i"
            and value[len(value) - 2] == "n"
            and value[len(value) - 1] == "g"
        ):
            value = list(value)
            value[len(value) - 3] = "l"
            value[len(value) - 2] = "y"
            value[len(value) - 1] = ""

            value = "".join(value)

    print(value)


def function5():
    print("\nЗадание 5")

    value = str(input("Введите текст: "))
    value = list(value)
    alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    for i in range(len(value)):
        for j in range(len(alf)):
            if j == len(alf) - 1:
                z = 26
            elif value[i] == alf[25]:
                z = 0
            else:
                z = j + 1
            if value[i] == alf[j]:
                value[i] = alf[z]
                break

    value = "".join(value)

    print(value)


if __name__ == "__main__":
    ex = int(input("Введите номер задания или 0 если все подряд надо: "))

    if ex == 0:
        function1()
        function2()
        function3()
        function4()
        function5()
    elif ex == 1:
        function1()
    elif ex == 2:
        function2()
    elif ex == 3:
        function3()
    elif ex == 4:
        function4()
    elif ex == 5:
        function5()
