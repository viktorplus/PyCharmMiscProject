"""Python Fundamentals 2025: Домашнее задание 15
Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки, содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру.
Данные:
text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
Пример вывода:
Обработанный список: ['hello', 'world', 'simple']
"""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]
for text in text_list:
    text.lower()
    if text.count(" "):
        text_list.remove(text)
print(f"Обработанный список: {text_list}")


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

