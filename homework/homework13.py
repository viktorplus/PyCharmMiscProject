"""Python Fundamentals 2025: Домашнее задание 13
Прогрессия увеличения
Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке.
Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
Данные:
numbers = (3, 7, 2, 8, 5, 10, 1)
Пример вывода:
Кортеж по возрастанию: (3, 7, 8, 10)
"""
# numbers = (3, 7, 2, 8, 5, 10, 1)
# max = numbers[0]
# typle_result = (numbers[0],)
# for number in numbers:
#     if number > max:
#         max = number
#         typle_result += (number,)
# print(f"Кортеж по возрастанию: {typle_result}")

"""
Повторяющиеся элементы
Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза. Вывести сами элементы и их индексы.
Данные:
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
Пример вывода:
Индексы элемента 2: 1 4 9 
Индексы элемента 3: 2 6 
Индексы элемента 4: 3 8
"""
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
uniq = ()
for index, number in enumerate(numbers):
    if numbers.count(number) > 1 and number not in uniq:
        typle2 = ()
        uniq += (number,)
        for index2, number2 in enumerate(numbers[index:]):
            if number2 == number:
                typle2 += (str(index2 + index),)
        print(f"Индексы элемента {number}: {" ".join(typle2)} ")
