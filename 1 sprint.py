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
not_uniq_str = 'съешь же ещё этих мягких французских булок да выпей чаю'
replaced = not_uniq_str.replace(' ', '')
count = len(set(replaced))
print(count)
#-------------------------------------------------


