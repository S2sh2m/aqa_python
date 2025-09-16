alice_in_wonderland = """'"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'"""

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
def alice():
    for char in alice_in_wonderland:
        if char == "'":
            print(char)

    print(alice_in_wonderland)

    """
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
def balck_sea(black_sea_square = 436402, azov_sea_square = 37800 ):
    azov_and_black = black_sea_square + azov_sea_square
    return azov_and_black

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
def warehouse(all_warehouse=375291, first_and_second=250449, second_and_third=222950):
    first = all_warehouse - second_and_third
    third = all_warehouse - first_and_second
    second = all_warehouse - (first + third)
    return first, second, third


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def payment(month_pay = 1179 , pay_term = 18 ):
    pc_price = month_pay * pay_term
    return pc_price


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
def remainder():
    a = 8019 / 8
    b = 9907 / 9
    c = 2789 / 5
    d = 7248 / 6
    e = 7128 / 5
    f = 19224 / 9

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    return None
# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
def pizza_order():
    pizza_big_price = 274
    pizza_middle_price = 218
    juice_price = 35
    cake_price = 350
    water_price = 21

    big_pizza_order_amount = 4
    middle_pizza_order_amount = 2
    juice_order_amount = 4
    cake_order_amount = 1
    water_order_amount = 3

    total_amount = (pizza_big_price * big_pizza_order_amount) + (pizza_middle_price * middle_pizza_order_amount) + (juice_price * juice_order_amount) + (cake_price * cake_order_amount) + (water_price + water_order_amount)
    return total_amount

"""Or even shorter kind of juice_total_price = 3 * 35 and total_amount = juice_total_price + ...  """

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def photo_album():
    all_photos = 232
    photo_on_page = 8
    all_page_needed = all_photos / photo_on_page
    return all_page_needed

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
def gasoline():
    total_range = 1600
    fuel_consumption = 9
    fuel_tank = 48
    total_consumption = total_range / fuel_consumption
    total_gas_station_stop = total_consumption / fuel_tank

    print(round(total_consumption, 2))
    return round(total_gas_station_stop)
