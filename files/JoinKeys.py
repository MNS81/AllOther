import time
from progress.bar import IncrementalBar
with open('data/1.txt', encoding='utf-8') as first, open('data/2.txt', encoding='utf-8') as second, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    print('*** Join Keys ***')
    print()
    print('Для использования необходимо положить файлы "1.txt" и "2.txt" в папку "data".')
    print('Программа получает списки ключей и объединяет их в отсортированный список уникальных комбинаций.')
    print()
    lst_1 = first.read().splitlines()
    lst_2 = second.read().splitlines()
    lst_out = []
    for word in lst_1:
        for key in lst_2:
            lst_out.append(f'{word} {key}')
    bar = IncrementalBar('Работаем: ', max=len(lst_out))
    for row in sorted(lst_out):
        bar.next()
        time.sleep(0.01)
        outfile.write(row + '\n')
    bar.finish()
input(f'\n\nСписок уникальных комбинаций сохранен в файл "out.txt" в папке "data".\n\nНажмите Enter для выхода')