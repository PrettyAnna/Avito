"""Конфиги и процессоры для лауреатов-людей и лауреатов-организаций."""

from json_dict_processing import create_processor
from prizes_configs import prize_processor


def process_year(year_string):
    """Извлекает год из строки даты формата 'YYYY-MM-DD' (или просто 'YYYY')."""
    if not year_string:
        return None
    return int(str(year_string).split('-')[0])


CONFIG_PERSON = {
    'id': ['id'],  
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}

CONFIG_ORG = {
    'id': ['id'],
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor()),
}



def process_persons(laureate):
    """Обрабатывает словарь лауреата-человека по CONFIG_PERSON."""
    processed = create_processor(CONFIG_PERSON)(laureate)
    processed['type_'] = 'person'
    return processed


def process_orgs(laureate):
    """Обрабатывает словарь лауреата-организации по CONFIG_ORG."""
    processed = create_processor(CONFIG_PERSON)(laureate)
    processed['type_'] = 'org'
    return processed

