# Импортируйте необходимые модули

import datetime as dt

FORMAT = '%H:%M:%S'  # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.

storage_data = {}


def check_correct_data(data):
    """Проверка корректности полученного пакета."""
    if len(data) != 2 or data[0] is None or data[1] is None:
        return False
    return True


def check_correct_time(time):
    """Проверка корректности параметра времени."""
    if not storage_data or time > max(storage_data.keys()):
        return True
    return False


def get_time(data):
    """Получить общее время тренировки."""
    if not data:
        return dt.timedelta(0)
    times = list(data.keys())
    start_time = dt.datetime.strptime(min(times), FORMAT)
    end_time = dt.datetime.strptime(max(times), FORMAT)
    return end_time - start_time


def get_step_day():
    """Получить количество пройденных шагов за этот день."""
    return sum(storage_data.values())


def get_distance(steps):
    """Получить дистанцию пройденного пути в км."""
    return steps * STEP_M / 1000


def get_spent_calories(dist, duration):
    """Получить значения потраченных калорий."""
    duration_minutes = duration.total_seconds() / 60
    if duration_minutes == 0:
        return 0
    mean_speed = dist / (duration_minutes / 60)
    spent_calories = ((K_1 * WEIGHT + (mean_speed**2 / HEIGHT) * K_2 * WEIGHT)
                      * duration_minutes)
    return spent_calories


def accept_package(data):
    """Обработать пакет данных."""
    if check_correct_data(data) and check_correct_time(data[0]):
        storage_data[data[0]] = data[1]
        return True
    return False


data_packages = [
    ('09:30:00', 1500),
    ('11:00:00', 2500),
    ('11:00:00', 3000),  # Некорректное время
    ('13:30:00', 4000),
    ('15:00:00', 3000)
]

for package in data_packages:
    accept_package(package)

total_time = get_time(storage_data)
total_steps = get_step_day()
total_distance = get_distance(total_steps)
total_calories = get_spent_calories(total_distance, total_time)

print(f'''
Время: {total_time}.
Количество шагов за сегодня: {total_steps}.
Дистанция составила {total_distance:.2f} км.
Вы сожгли {total_calories:.2f} ккал.
Отличный результат! Цель достигнута.
''')
