import json

with open("data/routes_data.json", "r", encoding="utf-8") as f:
    FLIGHT_INFO = json.load(f)

CITY_MAPPING = {
    'MOW': 'Москва',
    'LED': 'Санкт-Петербург',
    'BCN': 'Барселона',
    'HKT': 'Пхукет',
    'IST': 'Стамбул',
    'DXB': 'Дубай',
    'DOH': 'Доха',
    'AYT': 'Анталья',
    'BKK': 'Бангкок',
    'LON': 'Лондон',
    'PAR': 'Париж',
    'TBS': 'Тбилиси',
    'BEG': 'Белград',
    'BJS': 'Пекин',
    'TYO': 'Токио',
    'FRA': 'Франкфурт',
    'AMS': 'Амстердам',
    'AER': 'Сочи'
}

CITY_TO_IATA = {value: key for key, value in CITY_MAPPING.items()}