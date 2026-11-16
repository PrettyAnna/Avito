import statistics

from dataset_helpers import group_by


def mean(data, field):
    values = [r.get(field) for r in data if r.get(field) is not None]
    return statistics.mean(values) if values else None


def median(data, field):
    values = [r.get(field) for r in data if r.get(field) is not None]
    return statistics.median(values) if values else None


def max_value(data, field):
    values = [r.get(field) for r in data if r.get(field) is not None]
    return max(values) if values else None


def min_value(data, field):
    values = [r.get(field) for r in data if r.get(field) is not None]
    return min(values) if values else None


def count_not_none(data, field):
    return sum(1 for r in data if r.get(field) is not None)


def describe(data, field):
    """Сводка по полю: количество, среднее, медиана, минимум, максимум."""
    values = [r.get(field) for r in data if r.get(field) is not None]
    if not values:
        return None
    return {
        'count': len(values),
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'min': min(values),
        'max': max(values),
    }


def _apply_metric(records, metric, value_field):
    if metric == 'count':
        return len(records)
    if metric == 'mean':
        return mean(records, value_field)
    if metric == 'median':
        return median(records, value_field)
    if metric == 'max':
        return max_value(records, value_field)
    raise ValueError(f'Неизвестная метрика')


def top_n(data, group_field, n=5, metric='count', value_field=None):
    """Топ-N групп по метрике."""
    scored = []
    for key, records in group_by(data, group_field).items():
        score = _apply_metric(records, metric, value_field)
        if score is not None:
            scored.append((key, score))
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return scored[:n]