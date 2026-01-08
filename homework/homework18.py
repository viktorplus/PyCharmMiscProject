# Python Fundamentals 2025: Домашнее задание 18
# Не уникальные числа
# Напишите программу, которая находит все числа, встречающиеся более одного раза в списке,
# и выводит их в порядке убывания.
# Данные:
numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
# Пример вывода:
# Числа, встречающиеся более одного раза: [7, 4, 3, 8]
count_num = dict()
for number in numbers:
    if number in count_num:
        count_num[number] += 1
    else:
        count_num[number] = 1
result = sorted({key for key, value in count_num.items() if value > 1}, reverse=True)
print(f"Числа, встречающиеся более одного раза: {result}")

# Вариант set comprehensive
print(sorted({x for x in numbers if numbers.count(x) > 1}, reverse=True))


# Проверка подмножества Задача:
# Напишите программу, которая проверяет, является ли один словарь подмножеством другого
# (т.е. все его пары "ключ-значение" содержатся в другом словаре).
# Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}
# Пример вывода:
# Первый словарь является подмножеством второго.
d1_in_d2 = True
for key, value in dict1.items():
    if key not in dict2 or dict2[key] != value:
        d1_in_d2 = False
        break

d2_in_d1 = True
for key, value in dict2.items():
    if key not in dict1 or dict1[key] != value:
        d2_in_d1 = False
        break

if d1_in_d2 and d2_in_d1:
    print("Словари идентичны")
elif d1_in_d2:
    print("Словарь dict1 является подмножеством dict2")
elif d2_in_d1:
    print("Словарь dict2 является подмножеством dict1")
else:
    print("Словари не являются подмножествами")

