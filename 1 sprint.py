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
weight = 75 # Вес
height = 175 # Рост
steps = 8462 # Количество пройденных за день шагов
hours = 2 # Время движения в часах
len_step_m = 0.65 # Длина одного шага в метрах
transfer_coeff = 1000 # Коэффициент перевода значения расстояния из метров в километры

dist =  (steps * len_step_m) / transfer_coeff # Напишите формулу расчёта

mean_speed = dist / hours
minutes = hours * 60

spent_calories = (0.035*weight + (mean_speed**2 / height) * 0.029*weight) * minutes


if dist >= 6.5:
    motivations = 'Отличный результат! Цель достигнута!'
elif dist >= 3.9:
    motivations = 'Неплохо! День был продуктивным.'
elif dist >=2:
    motivations = 'Маловато, но завтра наверстаем!'
else:
    motivations = 'Лежать тоже полезно. Главное — участие, а не победа!'

output = (f'''Сегодня вы прошли {steps} шагов.
Пройденная дистанция {dist:.1f} км.
Вы сожгли {spent_calories:.2f} ккал.
{motivations}''')  # Здесь подготовьте строку для вывода
print(output)