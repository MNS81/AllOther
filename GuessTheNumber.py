from random import randint
print('*** Guess the number! ***')
print()
print('''Добро пожаловать в игру "Числовая угадайка"!
У Вас есть 10 попыток чтобы угадать число!''')
print()

def is_valid(s):
    if s.isdigit() and int(s) > 0 and int(s) <= 100: return int(s)
    else:
        while not s.isdigit():
            print('А может быть все-таки введем целое число от 1 до 100?')
            s = input()
        return int(s)

def game():
    number = randint(1, 100)
    count = 1
    while True:
        num = is_valid(input('Введите число от 1 до 100: '))
        if num < number:
            if count < 10: print(f'Ваше число меньше загаданного, попробуйте еще разок\nосталось попыток {10 - count}')
            else: print('Ваше число меньше загаданного')
        elif num > number:
            if count < 10: print(f'Ваше число больше загаданного, попробуйте еще разок\nосталось попыток {10 - count}')
            else: print('Ваше число больше загаданного')
        else:
            print(f'Вы угадали, поздравляем!\nколичество попыток {count}')
            break
        print()
        count += 1
        if count == 11:
            print('Вы проиграли, попробуйте еще разок')
            break
    more = input('Хотите поиграть еще раз? Введите "y" ')
    if more == 'y': game()
    else: print('До свидания!')

game()