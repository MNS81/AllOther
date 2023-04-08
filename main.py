def check_input(n):
    try:
        if int(n) > 0 and int(n) <= 100: return int(n)
        else:
            while int(n) < 0 or int(n) > 100:
                print('Неверный формат ввода!')
                n = input('Введите число от 0 до 100: ')
            return int(n)
    except ValueError:
        while True:
            print('Неверный формат ввода!')
            n = input('Введите число от 0 до 100: ')
            if n.isdigit() and int(n) > 0 and int(n) <= 100: return int(n)

ostatok = lambda x: round(12.5 - x * 0.12, 2)

while True:
    percent = check_input(input('\nВведите проценты: '))
    print(f'{percent}% = {ostatok(percent)}м.')
    if input('''\nВыберите действие:\n\t0 - Выход\n\t1 - Продолжить\n>>> ''') == '0': break