"""Конфиг и процессор для обработки данных о призах."""

from json_dict_processing import create_processor


def _to_int_or_none(value):
    """Безопасно приводит значение к int, иначе возвращает None."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], _to_int_or_none),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
}


def prize_processor():
    """Создаёт процессор для списка призов лауреата."""
    return create_processor(CONFIG_PRIZE, list_processor=True)
