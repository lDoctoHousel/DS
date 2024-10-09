import json

with open('orders_july_2023.json', 'r') as my_file:
    orders_july = my_file.read()
orders = json.loads(orders_july)

print(orders)
print(type(orders))

max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')


max_price = 0
max_order_num = None
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_price = price
        max_order_num = order_num
print(f'Номер самого дорогого заказа в июле: {max_order_num}')


max_quantity = 0
max_order_num = None
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_quantity = quantity
        max_order_num = order_num
print(f'Номер заказа с самым большим количеством товаров: {max_order_num}')


max_date = ''
for order_num, orders_data in orders.items():
    order = orders_data['date']
    if max_date == '' or max_order_num < order:
        max_date = order
        max_order_num = order_num
print(f'День, когда было сделано больше всего заказов: {max_date}')


quantity = 0
user_max_quantity = None
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    order_id = orders_data['user_id']
    if user_max_quantity is None or quantity > quantity:
        user_max_quantity = order_id
print(f'Пользователь, который сделал самое большое количество заказов за июль: {user_max_quantity}')


max_sum = 0
max_price_user = None
for orders_id, orders_data in orders.items():
    user_id = orders_data['user_id']
    price = orders_data['price']
    sum_of_prices = sum(price for _ in range(price))
    if max_sum < sum_of_prices:
        max_sum = sum_of_prices
        max_price_user = price
print(f'Пользователь с самой большой суммарной стоимостью заказов за июль: {max_price_user}')


from statistics import mean
prices = []
for order_num, orders_data in orders.items():
    prices.append(orders_data['price'])
avg_price = mean(prices)
print(f'Средняя стоимость заказа была в июле: {round(avg_price, 2)}')


sum_of_prices = 0
sum_of_quantity = 0
for order_num, orders_data in orders.items():
    sum_of_prices += orders_data['price']
    sum_of_quantity += orders_data['quantity']
avg_price_quantity = sum_of_prices / len(orders) + sum_of_quantity / len(orders)
print(f'Средняя стоимость товаров в июле: {avg_price_quantity}')