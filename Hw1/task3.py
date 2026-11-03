if __name__ == '__main__':
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]
    sum_returned = 0
    people_returned = set()
    sum_delivered = []
    for i in orders:
        if i['status'] == 'returned':
            sum_returned += i['amount']
            people_returned.add(i['buyer'])
        else:
            sum_delivered.append(i['amount'])
    print(f'''На какую сумму оформили возвраты - {sum_returned}
Кто хотя бы раз вернул заказ - {people_returned}
Сколько заказов доставлено покупателю - {len(sum_delivered)}
Средний чек доставленных заказов - {sum(sum_delivered) / len(sum_delivered)}''')