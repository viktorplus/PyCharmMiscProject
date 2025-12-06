"""Python Fundamentals 2025: Домашнее задание 11
Звёздочки вместо чисел
Напишите программу, которая заменяет все цифры в строке на звёздочки *.
text = "My number is 123-456-789"
Пример вывода:
Строка: My number is 123-456-789
Результат: My number is ***-***-***
"""

# text = "My number is 123-456-789"
# result = ''
# for ch in text:
#     if ch.isdigit():
#         result +="*"
#     else:
#         result += ch
# print(f"Строка: {text}")
# print(f"Результат: {result}")



"""
Количество символов
Напишите программу, которая подсчитывает количество вхождений всех символов в строке.
Нужно вывести только символы, которые встречаются более 1 раза (игнорируя регистр),
с указанием их количества. Выводите повторяющиеся символы только один раз.
text = "Programming in python"
Пример вывода:
Строка: Programming in python
Символ 'p' встречается 2 раз(а)
Символ 'r' встречается 2 раз(а)
Символ 'o' встречается 2 раз(а)
Символ 'g' встречается 2 раз(а)
Символ 'm' встречается 2 раз(а)
Символ 'i' встречается 2 раз(а)
Символ 'n' встречается 3 раз(а)
Символ ' ' встречается 2 раз(а)
"""

# text = "Programming in python"
#
# txt = text.lower()
# uniq_ch = ""
# for item in txt:
#     count = txt.count(item)
#     if  count >= 2 and item not in uniq_ch:
#         print(f"Символ '{item}' встречается {count}")
#         uniq_ch+= item


"""
Увеличение чисел
Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
Пример вывода:
I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
"""


# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# word_list = text.split( )                              # разбиваем строку на список слов
# for i in range (len(word_list)):                       # будем менять слова обращаясь по индексу, поэтому диапазонный цикл
#     if word_list[i][0].isdigit():                      # если в слове первый символ цифра
#         word_list[i] = str(float(word_list[i])*10)     # тут бы еще проверку на ошибку сделать, жаль пока не знаем как
# print(" ".join(word_list))

