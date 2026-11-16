def count_records(records):
    """Сколько всего записей."""
    return len(records)


def missing_values_summary(records, fields):
    """Считает пропуски по каждому полю."""
    return {
        field: sum(1 for r in records if r.get(field) is None)
        for field in fields
    }


def missing_share(records, fields):
    """Доля пропусков по каждому полю."""
    n = len(records)
    if n == 0:
        return {field: 0.0 for field in fields}
    return {
        field: missing_values_summary(records, [field])[field] / n
        for field in fields
    }


def get_ids(records):
    """Список id как целых чисел."""
    return [int(r['id']) for r in records if r.get('id') is not None]


def find_id_extremes(records):
    """Мин и макс id и годы награждения, которым они соответствуют."""
    ids = get_ids(records)
    min_id = min(ids)
    max_id = max(ids)

    result = {}

    for r in records:
        if r.get('id') is not None and int(r['id']) == min_id:
            years = [p['award_year'] for p in r.get('prizes_relevant') or []
                     if p.get('award_year') is not None]
            result['min'] = {'id': min_id,
                             'first_award_year': min(years) if years else None}
            break

    for r in records:
        if r.get('id') is not None and int(r['id']) == max_id:
            years = [p['award_year'] for p in r.get('prizes_relevant') or []
                     if p.get('award_year') is not None]
            result['max'] = {'id': max_id,
                             'first_award_year': min(years) if years else None}
            break

    return result


def find_duplicate_ids(records):
    """Возвращает список id, которые встречаются более одного раза."""
    ids = get_ids(records)
    seen, duplicates = set(), set()
    for i in ids:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    return sorted(duplicates)


def find_id_gaps(records, max_step=1):
    """Пары соседних id в отсортированном массиве, различающиеся более чем на max_step."""
    ids = sorted(get_ids(records))
    return [(a, b) for a, b in zip(ids, ids[1:]) if b - a > max_step]


EDA_FIELDS = ['id', 'name', 'gender', 'birth_year',
              'country_birth', 'country_now', 'prizes_relevant', 'type_']