"""Python Fundamentals 2025: Домашнее задание 14
Число в конце
Напишите программу, которая создает новый список. В него необходимо добавить только те строки из исходного списка, в которых цифры находятся только в конце.
Данные:
strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
Пример вывода:
Строки с цифрами только в конце: ['apple23', 'grape3']
"""

# strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
# result =[]
# for string in strings:
#     if string.rstrip("0123456789").isalpha():
#          result.append(string)
# print(f"Строки с цифрами только в конце: {result}")


"""
Удаление кратных
Напишите программу, которая удаляет из списка все значения, кратные числу, которое вводится пользователем.
Данные:
numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
Пример вывода:
Введите число для удаления кратных ему элементов: 3
Список без кратных значений: [1, 10, 19, 20]
"""

# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# result = []
# userinput = int(input("Введите число для удаления кратных ему элементов: "))
# for number in numbers:
#     if number % userinput:
#         result.append(number)
# print(f"Список без кратных значений: {result}")

# вариант 2
# numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
# k = int(input("Введите число для удаления кратных ему элементов: "))
#
# numbers[:] = [x for x in numbers if x % k != 0]
# print("Список без кратных значений:", numbers)

"""
Порядок четных
Напишите программу, которая формирует новый список чисел. Добавьте в него все элементы исходного списка, где:
нечетные числа занимают те же позиции,
чётные числа отсортированы между собой обратном порядке.
Данные:
numbers = [5, 2, 3, 8, 4, 1, 2, 7]
Пример вывода:
Список после сортировки: [5, 8, 3, 4, 2, 1, 2, 7]"""

# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
# result = numbers[:]
# ind = []
# dig = []
# for index, number in enumerate(numbers):
#     if number % 2 == 0:
#         ind.append(index)
#         dig.append(number)
# dig.sort(reverse=True)
# for i in range (len(ind)):
#     result[ind[i]] = dig[i]
# print(f"Список после сортировки: {result}")

# второй способ

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
result = numbers[:]
ind = []
dig = []
for index, number in enumerate(numbers):
    if number % 2 == 0:
        ind.append(index)
        dig.append(number)
        result.remove(number)

dig.sort(reverse=True)
for i in range (len(ind)):
    result.insert(ind[i], dig[i])
print(f"Список после сортировки: {result}")

# третий способ
# numbers = [5, 2, 3, 8, 4, 1, 2, 7]
#
# evens = sorted([x for x in numbers if x % 2 == 0], reverse=True)
#
# result = []
# ei = 0
# for x in numbers:
#     if x % 2 != 0:
#         result.append(x)          # нечётные на месте
#     else:
#         result.append(evens[ei])  # вставляем следующий чётный
#         ei += 1
#
# print("Список после сортировки:", result)
# [5, 8, 3, 4, 2, 1, 2, 7]



