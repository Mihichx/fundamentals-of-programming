def function1():
    print("\nЗадание 1")

    value = 12
    end_value = 100
    result = 0

    a = range(1, 5)
    print(a)

    for i in range(value, end_value, 3):
        result += 1

    print(f"Ответ {result}")


def function2():
    print("\nЗадание 2")

    value = 1
    end_value = 100

    for i in range(value, end_value):
        if i % 15 == 0:
            print("Fizz-Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def function3():
    print("\nЗадание 3")

    n = int(input("Введите значение >= 2: "))
    result = 0

    if n >= 2:
        for i in range(n, 20):
            result += (i - 1) * i

    print(result)

def function4():
    print("\nЗадание 4")

    value = 1000
    end_value = 10000

    for i in range(value, end_value):
        flag = 1
        value_str = str(i)

        for j in range(4):
            for n in range(j + 1, 4):
                if value_str[j] == value_str[n]:
                    flag = 0
                    break

        if flag == 1:
            a = int(value_str[0])
            b = int(value_str[1])
            c = int(value_str[2])
            d = int(value_str[3])
        
            if (int(value_str[0] + value_str[1])) - (int(value_str[2] + value_str[3])) == a + b + c + d:
                print(i)

def function5():
    print("\nЗадание 5")

    n = int(input("Введите число: "))
    result = 0

    for i in range(1, (n / 2) + 1):
        if n % i == 0:
            result += i

    if result == n:
        print("Совершенное")
    else:
        print("Не совершенное")

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
