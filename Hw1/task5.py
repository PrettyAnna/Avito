if __name__ == '__main__':
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]
    bad_stars = 0
    name_stars = {}
    for i in reviews:
        i['product'] = i['product'].capitalize()
        name_stars.setdefault(i['product'], []).append(i['stars'])
        if i['stars'] == 1 or i['stars'] == 2:
            bad_stars += 1
    avg_stars_min_two_reviews = {k:sum(v) / len(v) for k, v in name_stars.items() if len(v) > 1}
    min_avg = 5
    for k, v in avg_stars_min_two_reviews.items():
        if v < min_avg:
            min_avg = v
            day_min_avg = k

    print(f'''Среднюю оценку каждого товара - { {k:sum(v) / len(v) for k, v in name_stars.items()} }
Худший товар по средней оценке среди тех, у кого хотя бы два отзыва - {day_min_avg}
Сколько отзывов на 1 или 2 звезды - {bad_stars}
Какую долю всех отзывов они составляют - {bad_stars / len(reviews)}''')