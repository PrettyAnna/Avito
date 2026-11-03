from collections import Counter
if __name__ == '__main__':
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]
    count = Counter(queries)
    print(f'''Сколько всего поисковых запросов в ленте - {len(queries)}
Сколько раз ввели каждый запрос - {count}
Какой запрос вводили чаще всего - {count.most_common(1)[0][0]}
Какую долю всех поисков он занимает - {count.most_common(1)[0][1] / len(queries)}''')
    list_name = []
    for k, v in count.items():
        if v == 1:
            list_name.append(k)
    print(f'Kакие запросы встретились один раз - {list_name}')