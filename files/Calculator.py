print('*** Calculator ***')
print()
print('''Доступные операции:
\t+ - сложение
\t- - вычитание
\t* - умножение
\t/ - деление
\t% - остаток от деления
\t// - целочисленное деление
\t^ - возведение в степень''')
print('Пример ввода: a * b, пробелы обязательны!')
print()
a, oper, b = input('>>> ').split()
print()
a = int(a)
b = int(b)
match oper:
    case '+': print(f'{a} + {b} = {a + b}')
    case '-': print(f'{a} - {b} = {a - b}')
    case '*': print(f'{a} * {b} = {a * b}')
    case '/': print(f'{a} / {b} = {a / b}' if b != 0 else 'На ноль делить нельзя!')
    case '%': print(f'{a} % {b} = {a % b}' if b != 0 else 'На ноль делить нельзя!')
    case '//': print(f'{a} // {b} = {a // b}' if b != 0 else 'На ноль делить нельзя!')
    case '^': print(f'{a} ^ {b} = {a ** b}')
    case default: print('Неизвестная операция')
input()