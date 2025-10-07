# Аннотация переменной name: "это строка".
name: str = 'Наташа'

# Аннотация переменной var_for_bool: "это булева переменная".
var_for_bool: bool = True

# Можно напечатать аннотации переменных из глобальной области видимости.
print(__annotations__)
>>> {'name': <class 'str'>, 'var_for_bool': <class 'bool'>}