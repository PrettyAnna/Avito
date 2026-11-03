if __name__ == '__main__':
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]
    all_revenue = 0
    max_revenue = 0
    avg_revenue_day = {}
    day_returns20 = []
    for i in days:
        all_revenue += i['revenue']
        if i['revenue'] > max_revenue:
            max_revenue = i['revenue']
            day_max_revenue = i['day']
        avg_revenue_day[i['day']] = round(i['revenue'] / (i['orders']), 2)
        if i['returns'] / i['orders'] > 0.2:
            day_returns20.append(i['day'])
    print(f'''Выручка за всю неделю - {all_revenue}
День с самой большой выручкой - {day_max_revenue}
Средняя выручка на один заказ в каждый день - {avg_revenue_day}
Дни, где возвратов больше 20% заказов - {day_returns20}''')