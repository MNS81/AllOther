from math import atan, pi
def arcctg(x):
    return pi / 2 - atan(x)

def compute_population(year):
    people_year, start_year, age = 172, 2000, 45
    return round(people_year / age * arcctg((start_year - year) / age), 3)

year = int(input('year: '))
print(f'{year} - {compute_population(year)} млрд. человек.')
