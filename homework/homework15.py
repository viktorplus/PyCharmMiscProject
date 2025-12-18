"""Python Fundamentals 2025: Домашнее задание 15
Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]


for i in range(len(text_list) - 1, -1, -1):  # идём с конца к началу
    text = text_list[i].lower()

    if " " in text:  # если больше одного слова — удаляем
        del text_list[i]
    else:
        text_list[i] = text  # записываем строку в нижнем регистре

print(f"Обработанный список: {text_list}")

# вариант 2

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
text_list = ["Hello", "World", "Python Programming", "Advanced Topics", "Simple"]

i = 0
while i < len(text_list):
    text = text_list[i].lower()
    if " " in text:
        del text_list[i]
    else:
        text_list[i] = text
        i += 1
print("Обработанный список:", text_list)





# вариант 3
# text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
# result = [word.lower() for word in text_list if " " not in word]
# print("Обработанный список:", result)


"""
Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку к каждому товару и добавить в список элемент с новой ценой. В конце вывести таблицу с новой ценой.
Данные:
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

Пример вывода:
Введите скидку (в процентах): 17
Товар          Старая цена    Новая цена
Laptop            1200.00$       996.00$
Mouse                25.00$         20.75$
Keyboard           75.00$         62.25$
Monitor            200.00$       166.00$
"""
products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
discount = int(input("Введите скидку (в процентах): "))
print(f"{'Товар':<10}{'Старая цена':>16}{'Новая цена':>16}")
for product in products:
    product.append((1-discount/100)*product[1])
    print(f"{product[0]:<10}{product[1]:>15.2f}${product[2]:>15.2f}$")

