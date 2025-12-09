"""Номер покупки
Дан список покупок. Найдите какой по счету (начиная с единицы) товар с названием "Milk". Если товара нет, выведите сообщение об отсутствии.

Данные:
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]"""

# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
# if "Milk" in products:
#     print (f"Товар 'Milk' в списке покупок: {products.index('Milk')+1}")
# else:
#     print ("Товара нет в списке")

"""Список уникальных слов
Дан текст. Программа должна:
Разбить текст на слова.
Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
Вывести количество уникальных слов.
Данные:
text = "Python is a great programming language. Python is popular and powerful."
Количество уникальных слов: 9
Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']"""

# text = "Python is a great programming language. Python is popular and powerful."
# correct_text = text.lower().replace('.', '') # strip
# splitted_text = correct_text.split()
# uniq_text = list()
# for char in splitted_text:
#     if char not in uniq_text:
#         uniq_text.append(char)
# uniq_text.sort()
# print(f"{uniq_text, len(uniq_text)}")

"""Перемещение в конец
Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка,
сохраняя порядок остальных элементов.
Данные:
numbers = [4, 7, 1, 6, 3, 8, 2]

Перемещённые элементы: [6, 7, 8, 4, 1, 3, 2]"""

# numbers = [4, 7, 1, 6, 3, 8, 2]
# new_list =[]
# for num in numbers:
#     if num >= 5:
#         new_list.append(num)
# for num in numbers:
#     if num < 5:
#         new_list.append(num)
#
# print(f"Перемещенные элементы {new_list}")

"""способ 2"""

# numbers = [4, 7, 1, 6, 3, 8, 2]
# i = 0
# length = len(numbers)
# while i < length:
#     if numbers[i] < 5:
#         numbers.append(numbers.pop(i))
#         length -= 1
#     else:
#         i += 1
# print(numbers)

"""способ 3"""
# numbers = [4, 7, 1, 6, 3, 8, 2]
#
# greater = []
# less = []
#
# for n in numbers:
#     if n < 5:
#         less.append(n)
#     else:
#         greater.append(n)
#
# numbers.clear()          # очищаем исходный список
# numbers.extend(greater)  # сначала большие
# numbers.extend(less)     # потом маленькие
#
# print(numbers)


"""Суммы пар
Напишите программу, которая обрабатывает список чисел и возвращает новый список,
 содержащий все возможные суммы пар разных элементов без дубликатов значений. 
 Результат должен быть отсортирован по убыванию.
Данные:
numbers = [3, 5, 9]
Суммы пар чисел по убыванию: [14, 12, 8]
"""

# numbers = [3, 5, 9]
# l = []
#
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         sum = numbers[i] + numbers[j]
#         if sum not in l:
#             l.append(sum)
#
# l.sort(reverse=True)
# print(l)

"""Покупки с лимитом бюджета
Дан список покупок, где каждый элемент — это кортеж с названием товара и его ценой. 
Покупки распределены по приоритетности. Пользователь вводит бюджет. Программа должна вывести:
список покупок, которые он может себе позволить;
итоговую стоимость этих товаров.
Данные:"""
# shopping_list = [
# ("Bread", 1.20),
# ("Milk", 0.99),
# ("Eggs", 2.50),
# ("Butter", 3.75),
# ("Cheese", 4.10),
# ("Apple", 0.50)
# ]
""" Введите ваш бюджет: 7

Покупки в рамках бюджета:
Bread: $1.20
Milk: $0.99
Eggs: $2.50
Apple: $0.50

Итоговая стоимость: $5.19"""

# budget = 7
# total = 0
#
# print("Покупки в рамках бюджета:")
# for item, price in shopping_list:
#     if budget >= price:
#         budget -= price
#         total += price
#         print(f"{item}: ${price:.2f}")
#
# print(f"\nИтоговая стоимость: ${total:.2f}")


"""Оценки студентов
Дан список студентов, где каждый элемент — это кортеж с именем студента и его оценками. Программа должна вывести их имена
и средний балл в виде таблицы. Используйте форматирование для выравнивания колонок.
Данные:
""" """
Вывод:
Имя       Средний балл
Alice            84.33
Bob              85.33
Charlie          87.33
Diana            72.33
"""
students = [
    ("Alice", [85, 90, 78]),
    ("Bob", [88, 76, 92]),
    ("Charlie", [90, 87, 85]),
    ("Diana", [72, 80, 65])
]

print(f"{'Имя':<10} {'Средний балл':>12}")
for student in students:
    total = 0
    grades = student[1]

    for grade in grades:
        total += grade

    avg = total / len(grades)

    print(f"{student[0]:<10} {avg:>12.2f}")



