"""Переиспользуемый интерфейс добавления и удаления полей у записей."""


def add_field(records, name, func=None, default=None):
    """Добавляет поле каждой записи и возвращает их."""
    for record in records:
        record[name] = func(record) if func is not None else default
    return records


def add_fields(records, **fields):
    """Добавляет несколько константных полей разом."""
    for record in records:
        record.update(fields)
    return records


def remove_field(records, *names):
    """Удаляет перечисленные поля, если они есть."""
    for record in records:
        for name in names:
            record.pop(name, None)
    return records


def map_field(records, name, func):
    """Пересчитывает существующее поле"""
    for record in records:
        record[name] = func(record)
    return records