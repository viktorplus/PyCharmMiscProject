# Python Fundamentals 2025: Домашнее задание 19
#
# 1 Реверс словаря
# Напишите программу, которая меняет местами ключи и значения в словаре. Если значения повторяются, добавьте их в список.
# Данные:
# data = {"a": 1, "b": 2, "c": 1, "d": 3}
# Пример вывода:
# Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}
# revers = {}
# for key, value in data.items():
#     if value not in revers:
#         revers[value] = [key]
#     else:
#         revers[value].append(key)
# print(f"Перевернутый словарь: {revers}")
#
#
# # вариант 2
# reversed_dict = {}
# for key, value in data.items():
#     reversed_dict.setdefault(value, []).append(key)
# print("Перевернутый словарь:", reversed_dict)


# вариант 3
# reversed_dict = {v: [k for k, x in data.items() if x == v] for v in set(data.values())}
# print("Перевернутый словарь:", reversed_dict)


# 2 Счётчик букв в словах
# Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь,
# где ключи — это слова, а значения — это ещё один словарь с подсчётом каждой буквы.
# Данные:
# words = ["anna", "bennet", "john"]
# # Пример вывода:
# # {'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1, 'o': 1, 'h': 1, 'n': 1}}
#
# result = {name : {ch:name.count(ch) for ch in name} for name in set(words)}
# print(result)
#
# # вариант из summary
# letter_count = {}
# for word in words:
#     letter_count[word] = {}
#     for letter in word:
#         letter_count[word][letter] = letter_count[word].get(letter, 0) + 1
# print(letter_count)

# 3 Распределение студентов по группам
# У вас есть словарь, где ключи — имена студентов, а значения — их баллы за экзамен.
# Необходимо распределить студентов по группам:
# "Отличники": баллы >= 85
# "Хорошисты": баллы от 70 до 84
# "Троечники": баллы от 50 до 69
# "Не сдали": баллы < 50
#
# Создайте словарь с ключами-группами и словарями со студентами в качестве значений.
# Данные:
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
# Пример вывода:
# Распределение по группам:
# {'Отличники': {'Аня': 92, 'Дима': 88}, 'Хорошисты': {'Боря': 76}, 'Троечники': {'Ваня': 65, 'Ева': 54}, 'Не сдали': {'Галя': 48}}

result = {group: {} for group in groups}
for key, value in students.items():
    if value >= 85:
        result["Отличники"][key]= value
    elif value >= 70:
        result["Хорошисты"][key]= value
    elif value >= 50:
        result["Троечники"][key]= value
    else:
        result["Не сдали"][key]= value
print("Распределение по группам:")
print(result)

# вариант 2
rules = [
    ("Отличники", 85, 100),
    ("Хорошисты", 70, 84),
    ("Троечники", 50, 69),
    ("Не сдали",  0, 49),
]

result = {group: {} for group, min, max in rules}

for name, score in students.items():
    for group, min, max in rules:
        if min <= score <= max:
            result[group][name] = score
            break
print("Распределение по группам:")
print(result)

# вариант из summary
students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]

student_groups = {group: {} for group in groups}

for name, score in students.items():
    if score >= 85:
        group_name = "Отличники"
    elif 70 <= score < 85:
        group_name = "Хорошисты"
    elif 50 <= score < 70:
        group_name = "Троечники"
    else:
        group_name = "Не сдали"
    student_groups[group_name][name] = score

print("Распределение по группам:")
print(student_groups)