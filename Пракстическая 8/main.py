import random

def create_matrix(row: int, column: int, start: int, end: int):
    matrix = []
    for _ in range(row):
        new_row = []
        for _ in range(column):
            new_row.append(random.randint(start, end))
        matrix.append(new_row)
    return matrix

def ex1():
    print("Задание 1")
  
    matrix = create_matrix(3, 3, 1, 10)
    s = { "column": None, "max": -1 }

    for row in matrix:
        for index, value in enumerate(row):
            if value > s["max"]:
                s["max"] = value
                s["column"] = index

    for index_row in range(len(matrix)):
        matrix[index_row].pop(s["column"])

    for row in matrix:
        print(row)
    print(s)
    


def ex2():
    print("Задание 2")

    matrix = create_matrix(3, 3, 1, 10)
    s = { "row": None, "max_sum": 0 }

    for index_row, row in enumerate(matrix):
        row_sum = sum(row)
        if row_sum > s["max_sum"]:
            s["max_sum"] = row_sum
            s["row"] = index_row

    for row in matrix:
        print(row)
    print(s)


def ex3():
    print("Задание 3")

    matrix = create_matrix(3, 3, -5, 5)
    max_index = 0
    min_index = 0
    s = [{ "value": [], "count": 0 } for _ in range(len(matrix[0]))]

    for row in matrix:
        for index, value in enumerate(row):
            s[index]["value"].append(value)
            if value < 0:
                s[index]["count"] += 1

    for index, value in enumerate(s):
        if value["count"] > s[max_index]["count"]:
            max_index = index
        elif value["count"] < s[min_index]["count"]:
            min_index = index

    for row in matrix:
        print(row)

    print('-------------------')

    for index_row, row in enumerate(matrix):
        for index_column,value in enumerate(row):
            if index_column == max_index:
                matrix[index_row][index_column] = s[min_index]["value"][index_row]
            elif index_column == min_index:
                matrix[index_row][index_column] = s[max_index]["value"][index_row]


    for row in matrix:
        print(row)
    print(s)
    print(s[max_index]["count"])
    print(s[min_index]["count"])


def ex4():
    print("Задание 4")
    
    matrix = create_matrix(3, 3, 1, 10)
    min_value = 99
    min_value_index = -1

    for row in matrix:
        for index, value in enumerate(row):
            if value < min_value:
                min_value = value
                min_value_index = index

    for row in matrix:
        row.append(row[min_value_index])

    for row in matrix:
        print(row)
    print(min_value)
    print(min_value_index)

def ex5():
    print("Задание 5")

    matrix = create_matrix(3, 3, 1, 10)
    value_index = []

    for index, row in enumerate(matrix):
        for value in row:
            if value % 2 != 0:
                value_index.append(index)
                break

    for index in value_index:
        result = 0
        for value in matrix[index]:
            result += value
        print(result / len(matrix[index]))

    for row in matrix:
        print(row)
    print(value_index)


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
