"""Общие функции для списков плоских словарей: WHERE, GROUP BY, агрегации."""


def filter_records(data, **conditions):
    """Аналог SQL WHERE: возвращает записи, удовлетворяющие всем условиям."""
    result = []
    for record in data:
        for field, condition in conditions.items():
            value = record.get(field)
            if callable(condition):
                matched = condition(value)
            else:
                matched = value == condition
            if not matched:
                break
        else:
            result.append(record)
    return result


def group_by(data, keys):
    """Аналог SQL GROUP BY: {ключ: [записи]}."""
    if not isinstance(keys, (list, tuple)):
        keys = [keys]
        single = True
    else:
        single = False
    groups = {}
    for record in data:
        values = tuple(record.get(k) for k in keys)
        key = values[0] if single else values
        groups.setdefault(key, []).append(record)
    return groups


def aggregate(data, field, func, default=None):
    """Применяет агрегацию к значениям поля, пропуская None."""
    values = [record.get(field) for record in data if record.get(field) is not None]
    if not values:
        return default
    return func(values)


def aggregate_by(data, keys, field, func):
    """Группирует записи и считает агрегат func по полю field в каждой группе."""
    result = {}
    for key, records in group_by(data, keys).items():
        values = [r.get(field) for r in records if r.get(field) is not None]
        result[key] = func(values) if values else None
    return result