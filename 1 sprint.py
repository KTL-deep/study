# from decimal import Decimal
#
# # Стандартные числа с плавающей запятой
# i = 3.3 + 4.1
# print(i)
# # Вывод в терминал: 7.3999999999999995
#
# # Использование модуля Decimal для точных вычислений
# i = Decimal('3.3') + Decimal('4.1')
# print(i)
# # Вывод в терминал: 7.4
# #-------------------------------------------------
# rating = 4.9
#
# # Используем стандартный оператор if...else
# if rating > 4.7:
#     print('Фильм крут')
# else:
#     print('Так себе киношечка')1
#
# # Используем тернарный оператор
# result = 'Фильм крут' if rating > 4.7 else 'Так себе киношечка'
# print(result)
#
# print('Проверка окончена')
# #-------------------------------------------------
# x = -1
# y = -4
# cuoter = 0
#
# if x and y > 0:
#     cuoter = 1
# elif x < 0 and y > 0:
#     cuoter = 2
# elif x < 0 and y < 0:
#     cuoter = 3
# elif x > 0 and y < 0:
#     cuoter = 4
# print('точка в четверти', cuoter)
# #-------------------------------------------------
# status_string = 'ВСЁ ИДЁТ ПО ПЛАНУ'
# print(status_string.lower())
# print(status_string.upper())
# print(status_string.capitalize())
# print(status_string.title())
# print(status_string.swapcase())
# #-------------------------------------------------
# weight = 75 # Вес
# height = 175 # Рост
# steps = 8462 # Количество пройденных за день шагов
# hours = 2 # Время движения в часах
# len_step_m = 0.65 # Длина одного шага в метрах
# transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры
#
# dist = steps * len_step_m / transfer_coeff # Напишите формулу расчёта
#
# mean_speed = dist / hours
# minutes = hours * 60
#
# spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes
#
# output = (f'Вы прошли {dist} км и потратили {spent_calories:.1f} калорий, '
#           f'Молодец!')  # Здесь подготовьте строку для вывода
# print(output)
# #-------------------------------------------------
# weight = 75 # Вес
# height = 175 # Рост
# steps = 8462 # Количество пройденных за день шагов
# hours = 2 # Время движения в часах
# len_step_m = 0.65 # Длина одного шага в метрах
# transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры
#
# dist =  (steps * len_step_m) / transfer_coeff # Напишите формулу расчёта
#
# mean_speed = dist / hours
# minutes = hours * 60
#
# spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes
#
#
# if dist >= 6.5:
#     motivations = 'Отличный результат! Цель достигнута!'
# elif dist >= 3.9:
#     motivations = 'Неплохо! День был продуктивным.'
# elif dist >=2:
#     motivations = 'Маловато, но завтра наверстаем!'
# else:
#     motivations = 'Лежать тоже полезно. Главное — участие, а не победа!'
#
# output = (f'''Сегодня вы прошли {steps} шагов.
# Пройденная дистанция {dist:.1f} км.
# Вы сожгли {spent_calories:.2f} ккал.
# {motivations}''')  # Здесь подготовьте строку для вывода
# print(output)
# #-------------------------------------------------
# numbers = [i ** 2 for i in range(1, 11)]
# print(numbers)
# # #-------------------------------------------------
# movie_ratings = [4.7, 5.0, 4.3, 3.8]
# new_movie_ratings = [
#    rating + 0.2 if rating < 4.9 else rating for rating in movie_ratings
# ]
# print(new_movie_ratings)
# # Вывод в терминал: [4.9, 5.0, 4.5, 4.0]
# #-------------------------------------------------
# week = [
#     'Понедельник', 'Вторник', 'Среда',
#     'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
# ]
#
# mon, tue, wed, thu, fri, sat, sun = week
# print(wed)
# print(id(wed))
# # Вывод в терминал: Среда
# #-------------------------------------------------
# force_words = ['сила', 'пребудет', 'с', 'тобой', 'Да']
# print(id(force_words))
#
# # Место для вашего кода
# first = force_words.pop(-1)
# last = force_words.pop(0)
# force_words.insert(0, first)
# force_words.append(last)
#
# print(force_words)
#
# # Убедимся, что это тот же объект, что и в начале программы
# print(id(force_words))
# #-------------------------------------------------
# Литерально set объявляется с помощью фигурных скобок.
# toys = {'куклы', 'кубики', 'странная штука', 'самолетики', 'мелки'}
#
# for toy in toys:
#     print(toy)
# #-------------------------------------------------
# movies = ['Матрица', 'Сеть', 'Хакеры', 'Трон', 'Тихушники', 'Сеть', 'Трон']
# uniq_movies = set(movies)
# print(uniq_movies)
# #-------------------------------------------------
# not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
# replaced = not_uniq_str.replace(' ', '')
# count = len(set(replaced))
# print(count)
# #-------------------------------------------------
# package = ['2:00:01', 15000]
# package = tuple(package)
# print(package)
# print(type(package))
#-------------------------------------------------
# movie_info = {'Матрица': 4.5, 'Трон': 4.8}
# movie_names = set(movie_info)
# print(movie_names)
#-------------------------------------------------
# import time
#
# # Создается множество
# num_set = set()
# # С помощью цикла множество заполняется элементами от 0 до 999999
# for num in range(10**6):
#     num_set.add(num)
#
# # В start_time сохраняем время в секундах перед началом поиска
# start_time = time.time()
# if 954365 in num_set:
#     print(True)
#
# # Выводим в терминал время, затраченное на поиск нужного элемента:
# print((time.time() - start_time))
#
# # Создаём и наполняем список:
# num_list = []
# for num in range(10**6):
#     num_list.append(num)
#
# start_time = time.time()
# if 954365 in num_list:
#     print(True)
# print((time.time() - start_time))
#-------------------------------------------------
# maxim_toys = {'машинка', 'скакалка', 'кубики', 'пистолетик'}
# lera_toys = {'скакалка', 'кукла', 'кубики', 'юла'}
#
# # Создаём множество, элементы которого есть в первом И (&) во втором множестве:
# overlap = maxim_toys & lera_toys
# print(overlap)
# # Вывод в терминал: {'кубики', 'скакалка'}
# unite = maxim_toys | lera_toys
# print(unite)
# diff = maxim_toys - lera_toys
# print(diff)
# sym_diff = maxim_toys ^ lera_toys
# print(sym_diff)
#-------------------------------------------------
# num_string_1 = '100 13 2 143 12 3 55 4 64 18 56'
# num_string_2 = '234 2 56 432 3 100 12 99 43 18 31 64'
#
# union = set(num_string_1.split()) & set(num_string_2.split())
# print(union)
# print(len(union))
#-------------------------------------------------
# Исходная строка с ID
# id_string = '32 48 2 6 14 58 2 88 9 14 123 48 3 17 42 42 7'
#
# id_list = id_string.split()
# unique_ids = {int(i) for i in id_list}
# unique_ids_list = list(unique_ids)
# sort_ids = unique_ids_list.sort()
#
# print(unique_ids_list)
# print(sort_ids)
#-------------------------------------------------
# import datetime as dt
#
# lera_birthday = dt.date(2015, 5, 16)
# maxim_birthday = dt.date(2011, 12, 16)
#
# def get_days_to_birthday(date_birthday):
#     today = dt.date.today()
#     today_year = today.year
#     new_date_birthday = date_birthday.replace(year=today_year)
#     if new_date_birthday < today:
#         date = new_date_birthday.replace(year=today_year + 1) - today
#     else:
#         date = date_birthday.replace(year=today_year) - today
#     return date.days
#
# lera_days_left = get_days_to_birthday(lera_birthday)
# maxim_days_left = get_days_to_birthday(maxim_birthday)
#
# print(lera_days_left)
# print(maxim_days_left)
#-------------------------------------------------
import datetime as dt

birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Толя', '12.06.2016')
]

# В эту переменную запишите формат для
# преобразования даты
FORMAT = '%d.%m.%Y'


# Добавьте в объявление функции ещё один параметр - имя
def get_days_to_birthday(name, date_birthday):
    # Преобразуйте полученную строку с датой в объект нужного типа
    date_birthday = None
    name = None

    today = dt.date.today()
    date_birthday = date_birthday.replace(year=today.year)

    if date_birthday < today:
        date_birthday = date_birthday.replace(year=today.year + 1)

    days_to_birthday = date_birthday - dt.date.today()
    return days_to_birthday






# Напечатайте результат вызова функции get_days_to_birthday()
# для каждой пары из списка birthdays
print(get_days_to_birthday(..., ...))