print('*** Игра "Чудо - риэлтер" ***')
print()
print('''Приветствуем вас в игре "Чудо - риэлтер".
Здесь вы сможете реализовать все свои тайные желания и рассчитать стоимость квартиры своей мечты.''')
print()
summ = 0
cash = int(input('Ваша зарплата в месяц: '))
price = int(input('Сколько планируется потратить: '))
print()
house = int(input('Выберите дом (0 - старый, 1 - пофиг, 2 - новый): '))
print()
price = price - 1000000 * house
summ = summ + 1000000 * house
if price < 0: print('Не укладываемся в бюджет')
else:
    rooms = int(input('Выберите количество комнат (1 - 9): '))
    print()
    price = price - 4000000 - 1000000 * rooms
    summ = summ + 4000000 + 1000000 * rooms
    if price < 0: print('Не укладываемся в бюджет')
    else:
        area = int(input('Выберите этаж (1 - 9): '))
        print()
        if 3 < area < 6:
            price = price - 1000000
            summ = summ + 1000000
        if price < 0: print('Не укладываемся в бюджет')
        else:
            print('\n' + 'Стоимость квартиры:', summ)
            print(f'Чтобы купить квартиру своей мечты вам осталось не кушать примерно: {int(summ // cash // 12)} лет и {int(summ / cash % 12)} месяцев.')
input()