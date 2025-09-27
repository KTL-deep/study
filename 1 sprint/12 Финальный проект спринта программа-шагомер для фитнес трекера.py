# Импортируйте необходимые модули

import datetime as dt

FORMAT = '%H:%M:%S' # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.



def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) !=2 or not data[0] or not data[1]:
        return False
    return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if storage_data and time <= max(storage_data.keys()):
        return False
    return True


def get_step_day(steps):
    """Получить количество пройденных шагов за этот день."""
    return sum(storage_data.values()) + steps


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return steps * STEP_M / 1000


def get_spent_calories(dist, current_time):
    """Получить значения потраченных калорий."""
    if not storage_data:
        return 0

    # Рассчитываем длительность тренировки в минутах и часах
    duration_minutes = (current_time - min(storage_data.keys())).total_seconds() / 60
    duration_hours = duration_minutes / 60

    if duration_hours == 0:
        return 0

    mean_speed = dist / duration_hours

    # Формула расчета калорий
    spent_calories = (K_1 * WEIGHT + (mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * duration_minutes
    return spent_calories

data_packages = [
    ('09:30:00', 1500),
    ('11:00:00', 2500),
    ('11:00:00', 3000),  # Некорректное время
    ('13:30:00', 4000),
    ('15:00:00', 3000),
    (None, 100) # Некорректные данные
]


storage_data = {}
