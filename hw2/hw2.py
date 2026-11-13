import csv


def read_file(name):
    info = []
    data = []
    try:
        with open(name, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                info.append(row)
            info.pop(0)  # 'ФИО полностью; Департамент; Отдел; Должность; Оценка; Оклад'
            for i in info:
                i = i[0].split(';')
                data.append(i)
    except FileNotFoundError:
        print(f'Ошибка: файл "{name}" не найден.')
        return []
    return data


def hierarchy(file):
    # Я тут не очень поняла, что считать за команды, взяла отделы. Отделы взяла без повторений.
    # Если повторения важны - можно set на [] заменить. Ну и add на append))
    if file == []:
        return 'Файл пустой, не могу сформировать отчёт:('
    departm = {}
    for i in file:
        departm.setdefault(i[1], set()).add(i[2])
    return departm


def summary(file):
    if file == []:
        return 'Файл пустой, не могу сформировать отчёт:('
    salary = {}
    summ = []
    for i in file:
        salary.setdefault(i[1], []).append(int(i[5]))
    for key in salary.keys():
        summ.append({'name': key,
                     'people': len(salary[key]),
                     'min_salary': min(salary[key]),
                     'max_salary': max(salary[key]),
                     'min_salary': min(salary[key]),
                     'avg_salary': sum(salary[key]) / len(salary[key])})
    return summ


def summary_csv(file, new_name):
    if file == []:
        return 'Файл пустой, не могу сформировать отчёт:('
    data = summary(file)
    fieldnames = ['name', 'people', 'min_salary', 'max_salary', 'avg_salary']
    with open(new_name, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def perort(file, option, name_file=None):
    file = read_file(file)
    if option == 1:
        print(hierarchy(file))
    elif option == 2:
        print(summary(file))
    elif option == 3:
        summary_csv(file, name_file)
    else:
        print('Мы такое пока не реализовали))')


if __name__ == '__main__':
    perort('Corp_Summary.csv', 1)
    print('-' * 30)
    perort('Corp_Summary.csv', 2)
    print('-' * 30)
    perort('Corp_Summary.csv', 3, 'Mur')
    perort('Corp_Summary.csv', 'Хи-хи-хи, всё сломаю')
    print('-' * 30)
    perort('Хе-хе-хе, и тут сломаю', 1)
    print('-' * 30)
    perort('Ну хоть тут сломаю', 2)



