from random import randint

def roll_the_dice():
    return randint(1, 11)

def ends_word(n):
    s = 'очк'
    if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: return s + 'а'
    elif n == 1 or n == 21: return s + 'о'
    else: return s + 'ов'

def game_rules():
    print('''Правила игры:
    Игрок набирает очки, бросая 11-гранный кубик несколько раз с целью получить 21 очко.
    \t1. Если игрок набирает ровно 21 очко, он автоматически выигрывает игру.
    \t2. Если у игрока больше 21 очка, он "перебрал" и игру выигрывает дилер.
    \t3. Если у дилера больше 21 очка, он "перебрал" и игру выигрывает игрок.
    \t4. Если ни игрок, ни дилер не "перебрали", выигрывает тот, у кого больше очков. 
    \t5. При ничьей игра считается ничейной.\n''')

def player():
    result = 0
    while result < 21:
        ans = input('0 - Бросить\nEnter - Остановиться\n--> ')
        if ans == '0':
            print('Игрок бросает кости')
            deal = roll_the_dice()
            result += deal
            print(f'У вас {result} {ends_word(result)}\n')
        else: break
    if result > 21: print("Игрок перебрал! Дилер выиграл!\n")
    elif result == 21: print("Игрок выиграл!\n")
    else: return result

def dealer():
    result = 0
    while result < 17:
        deal = roll_the_dice()
        result += deal
    if result > 21: print("Дилер перебрал! Игрок выиграл!\n")
    elif result == 21: print("Дилер выиграл!\n")
    else: return result

def game():
    game_rules()
    player_score = player()
    if player_score:
        dealer_score = dealer()
        if dealer_score:
            print(f'\nИгрок: {player_score}')
            print(f'Дилер: {dealer_score}\n')
            if dealer_score > player_score: print("Дилер победил!")
            elif dealer_score == player_score: print("Ничья!")
            else: print("Игрок победил!")

while input('\n-== Roll the dice! ==-\n\nХотите сыграть? (y/n): ') == 'y': game()