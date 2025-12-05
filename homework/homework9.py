"""Python Fundamentals 2025: Домашнее задание 9
Таблица умножения
Напишите программу, которая выводит таблицу умножения для чисел от 1 до n. Где n это число, которое введет пользователь. Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)
Пример вывода:
Введите число: 5"""

# number = int(input())+1
# for i in range(1,number):
#     for j in range(1, number):
#         print(i*j, end="\t")
#     print()


"""Лестница чисел
Напишите программу, которая принимает число n и выводит "лестницу" из чисел. Каждая строка лестницы содержит числа от 1 до номера строки.
Пример вывода:
Введите число: 5  """

# number = int(input())+2 # +2 потому что по единице теряется на каждом цикле (не включен конец диапазона)
# for i in range(1,number):
#     for j in range(1,i):
#         print(j, end="\t")
#     print()

"""Удаление всех повторяющихся символов
Напишите программу, которая принимает строку и удаляет из неё все повторяющиеся символы, сохраняя только первые их вхождения.
Пример вывода:
Введите строку: Python programming  
Результат: Python prgami"""

# str1 = input("Введите строку: ")
# mod_str1 = str1[0]
# for i in range(len(str1)):
#     for j in range(len(mod_str1)):
#         if str1[i] == mod_str1[j]:
#             break
#     else: mod_str1 += str1[i]
# print(mod_str1)

str1 = input("Введите строку: ")
mod_str1 = ""
for i in range(len(str1)):
    if str1[i] not in mod_str1:
        mod_str1 += str1[i]
print(mod_str1)

# text = "Python programming"
# print("Python" in text)
# print("Hello" in text)