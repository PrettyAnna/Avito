def extract_nested_value(obj, keys):
    """Извлекает значение из вложенных структур данных по цепочке ключей.
    Если на каком-то шаге ключ отсутствует (или вместо словаря лежит None), возвращает None.
    """
    current = obj
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def process_dictionary_with_config(dictionary, config):
    """Обрабатывает один словарь согласно словарю-конфигу."""
    if not isinstance(dictionary, dict):
        raise TypeError(f"Не словарь")

    result = {}
    for attribute, spec in config.items():
        if isinstance(spec, tuple):
            if len(spec) != 2:
                raise ValueError(
                    f"Что-то не то с данными"
                )
            path, func = spec
        elif isinstance(spec, list):
            path, func = spec, None
        else:
            raise ValueError(
                f"Что-то не то с данными"
            )

        value = extract_nested_value(dictionary, path)
        if func is not None and value is not None:
            value = func(value)
        result[attribute] = value
    return result


def process_list_of_dicts_with_config(list_of_dicts, config):
    """Обрабатывает список словарей по одному конфигу."""
    if list_of_dicts is None:
        return []
    if not isinstance(list_of_dicts, list):
        raise TypeError(
            f"Не список словарей"
        )
    return [process_dictionary_with_config(d, config) for d in list_of_dicts]


def create_processor(config, list_processor=False):
    """Создаёт процессор с предзагруженной конфигурацией."""
    inner = process_list_of_dicts_with_config if list_processor \
        else process_dictionary_with_config

    def processor(data):
        return inner(data, config)

    return processor
