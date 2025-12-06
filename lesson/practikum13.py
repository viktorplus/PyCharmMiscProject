"""Письма клиентам
Напишите программу, которая генерирует текстовые шаблоны писем для клиентов на основе заранее
подготовленных данных. В письмах отображается информация о покупке, скидке и итоговой стоимости в
соответствии с шаблоном.
Данные:
clients = [
 ("Иван", "Иванов", 10, [("Кофе", 100.00), ("Чай", 200.00)]),
 ("Анна", "Смирнова", 15, [("Шоколад", 150.00), ("Печенье", 50.00)]),
 ("Петр", "Сидоров", 20, [("Чайник", 1000.00), ("Кружка", 300.00)])
]"""


clients = [
 ("Иван", "Иванов", 10, [("Кофе", 100.00), ("Чай", 200.00)]),
 ("Анна", "Смирнова", 15, [("Шоколад", 150.00), ("Печенье", 50.00)]),
 ("Петр", "Сидоров", 20, [("Чайник", 1000.00), ("Кружка", 300.00)])
    ]
for firstname, lastname, discount, purchaselist in clients:
    tprice = 0
    tname = ()
    for name, price in purchaselist:    #sum_price = sum(price for name_product, price in product)
        tname  += (name,)
        tprice += price
    final_price = tprice * (1 - discount / 100)

    print(f"Клиент {firstname} {lastname} вы купили товары {", ".join(tname).lower()} имеет скидку {discount} совершил покупку на сумму {tprice} со скидкой итого{final_price}")

###
    # employees = [
    #     ("Иван", "Иванов", "Менеджер", 6000),
    #     ("Мария", "Петрова", "Аналитик", 2000),
    #     ("Сергей", "Сидоров", "Разработчик", 1400),
    #     ("Анна", "Смирнова", "Дизайнер", 1950)
    # ]
    # name_max = max(len(name) for name, lastname, job_title, salary in employees) + 5
    # lastname_max = max(len(lastname) for name, lastname, job_title, salary in employees) + 5
    # job_title_max = max(len(job_title) for name, lastname, job_title, salary in employees) + 5
    # salary_max = max(len(str(salary)) for name, lastname, job_title, salary in employees) + 5
    # print(f'{"Name":<{name_max}}{"Lastname":<{lastname_max}}{"Job_title":<{job_title_max}}{"Salary":>{salary_max}}')
    # total_width = name_max + lastname_max + job_title_max + salary_max
    # total_end = name_max + lastname_max + job_title_max
    # print("_" * total_width)
    # sum_salary = sum(s for *_, s in employees)
    # avg_salary = sum_salary / len(employees)
    #
    # for name, lastname, job_title, salary in employees:
    #     print(f'{name:<{name_max}}{lastname:<{lastname_max}}{job_title:<{job_title_max}}{salary:>{salary_max},.2f}')
    #
    # print("_" * total_width)
    # print(f"{'Итого:':<{total_end}}{sum_salary:>{salary_max},.2f}")
    # print(f'{"Средняя зарплата:":<{total_end}}{avg_salary:>{salary_max},.2f}')


    # clients = [
    #     ("Иван", "Иванов", 10, [("Кофе", 100.00), ("Чай", 200.00)]),
    #     ("Анна", "Смирнова", 15, [("Шоколад", 150.00), ("Печенье", 50.00)]),
    #     ("Петр", "Сидоров", 20, [("Чайник", 1000.00), ("Кружка", 300.00)])
    # ]
    # for name, surname, discount, product in clients:
    #     sum_price = sum(price for name_product, price in product)
    #     total_price = sum_price * (1 - discount / 100)
    #     product_str = "\n".join(f" - {name}: {price}" for name, price in product)
    #     print(f"Уважаемый(-ая) {name} {surname},\nСпасибо за покупку в нашем магазине!\n"
    #           f"Вы купили следующие товары:\n{product_str}\n"
    #           f"Общая сумма покупок: {sum_price}\n"
    #           f"Ваша скидка: {discount}\nСумма с учётом скидки: {total_price}\n"
    #           f"Благодарим за покупку!\n")

    """products = [("Молоко", 3, 10),
            ("Хлеб", 1, 5),
            ("Сахар-песок", 2, 15),
            ("Подсолнечное масло", 5, 3),
            ("Шоколадный-молочный сахарный батончик", 4, 20),
            ("Мороженое", 3, 20)]

name_max = max(len(name) for name, price, quantity in products)
print(f"| {'Название':<{namemax}} | {'Цена':>10} | {'Количество':>10} |")
print("" * (name_max + 30))
for name, price, quantity in products:
        print(f"| {name:<{name_max}} | {price:>10} | {quantity:>10} |")"""

    """clients = [
    ("Иван", "Иванов", 10, [("Кофе", 100.00), ("Чай", 200.00)]),
    ("Анна", "Смирнова", 15, [("Шоколад", 150.00), ("Печенье", 50.00)]),
    ("Петр", "Сидоров", 20, [("Чайник", 1000.00), ("Кружка", 300.00)])
]

for client in clients:
    name, surname, discount, purchases = client

    print(f"Уважаемый(ая) {name} {surname},")
    print("Спасибо за покупку в нашем магазине!")
    print("Вы купили следующие товары:")

    total = 0
    for item_name, item_price in purchases:
        print(f"- {item_name}: {item_price:.2f}")
        total += item_price

    print(f"Общая сумма покупок: {total:.2f}")
    print(f"Ваша скидка: {discount}%")
    print(f"Сумма с учётом скидки: {total * (1 - discount / 100):.2f}")
    print("Благодарим за покупку!\n")"""



