import time
from progress.bar import IncrementalBar
print(f'*** Список покупок ***\n')
buy_list = {1: ['Колбаса', 450], 2: ['Молоко', 100], 3: ['Картошка', 80], 4: ['Макароны', 80], 5: ['Помидоры', 65], 6: ['Майонез', 120], 7: ['Морковь', 50], 8: ['Хлеб', 80], 9: ['Курица', 350]}
print('Список товаров:')
[print('\t', k, v[0]) for k, v in buy_list.items()]
print(f'\t 0 выход')

summ, count = 0, 0
while (s := int(input('\nВведите номер товара: '))) != 0:
    if s in buy_list:
        summ += buy_list[s][1]
        count += 1
        print(f'Вы добавили: {buy_list[s][0]} всего за {buy_list[s][1]}руб.')
    else:
        print('Такого товара нет в списке')
print(f'\nСумма покупок: {summ}\nКоличество товаров: {count}\n')
bar = IncrementalBar('Пум-пум-пи-дум...отправляем письмо курьеру...пум-пум-пи-дум-пум...', max=100)
for i in range(100):
    bar.next()
    time.sleep(0.05)
print('\nПисьмо отправлено')
input('\nНажмите Enter для выхода...')