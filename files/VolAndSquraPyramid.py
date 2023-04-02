from math import sqrt
# Объём пирамиды
def volume(a, h): return round(a ** 2 * h / (4 * sqrt(3)), 3)
# Площадь пирамиды
def square(a, h): return round(a ** 2 * sqrt(3) / 4 + 3 * a / 2 * sqrt(h ** 2 + a ** 2 / 12), 3)

a, h = float(input('Длина основания: ')), float(input('Высота: '))
if a <= 0 or h <= 0: print('error')
else: print(volume(a, h), square(a, h))