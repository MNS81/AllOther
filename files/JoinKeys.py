import time
from progress.bar import IncrementalBar
with open('data/1.txt', encoding='utf-8') as first, open('data/2.txt', encoding='utf-8') as second, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    print('*** Join Keys ***')
    print()
    print('Программа получает списки ключей и объединяет их в отсортированный список уникальных комбинаций.')
    print('Для использования необходимо положить файлы "1.txt" и "2.txt" в папку "data".')
    print()
    lst_1 = first.read().splitlines()
    lst_2 = second.read().splitlines()
    lst_out = []
    for word in lst_1:
        for key in lst_2:
            lst_out.append(f'{word} {key}')
    i_bar = IncrementalBar('Пум-пум-пи-дум...', max=len(lst_out))
    for row in sorted(lst_out):
        outfile.write(row + '\n')
        i_bar.next()
        time.sleep(0.01)

input(f'\n\nСписок уникальных комбинаций сохранен в файл "out.txt" в папке "data".\nНажмите Enter для выхода.')