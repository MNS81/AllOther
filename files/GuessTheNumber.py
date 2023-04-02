from random import randint
import winsound
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
            if count < 10:
                print(f'Ваше число меньше загаданного, попробуйте еще разок\nосталось попыток {10 - count}')
                print('\n' + '*' * 20 + '  МАША, ВВЕДИ ЧИСЛО БОЛЬШЕ ПРЕДЫДУЩЕГО!!!  ' + '*' * 20)
            else: print('Ваше число меньше загаданного')
        elif num > number:
            if count < 10:
                print(f'Ваше число больше загаданного, попробуйте еще разок\nосталось попыток {10 - count}')
                print('\n' + '*' * 20 + '  МАША, ВВЕДИ ЧИСЛО МЕНЬШЕ ПРЕДЫДУЩЕГО!!!  ' + '*' * 20)
            else: print('Ваше число больше загаданного')
        else:
            print(f'Вы угадали, поздравляем!\nколичество попыток {count}')
            winsound.PlaySound('beep.wav', winsound.SND_FILENAME)
            break
        print()
        count += 1
        if count == 11:
            print('Вы проиграли, попробуйте еще разок')
            winsound.PlaySound('beep.wav', winsound.SND_FILENAME)
            break
    more = input('Хотите поиграть еще раз? Введите "y" или "д" ')
    if more in 'yд':
        print()
        game()
    else:
        print(f'\nДо свидания!\n')
        input('Нажмите Enter для выхода')

game()