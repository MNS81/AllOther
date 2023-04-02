import time
from progress.bar import IncrementalBar
with open('data/in.txt', encoding='utf-8') as f_in, open('data/minus.txt', encoding='utf-8') as f_minus, open('data/out.txt', 'w', encoding='utf-8') as f_out:
    print('*** Remove Strings With Keys ***')
    print()
    print('Программа удаляет из файла "in.txt" все строки, в которых содержатся ключи из файла "minus.txt".')
    print('Для использования необходимо положить файлы "in.txt" и "minus.txt" в папку "data".')
    print()
    lst_in = f_in.read().splitlines()
    lst_minus = f_minus.read().splitlines()
    bar = IncrementalBar('Пум-пум-пи-дум...', max=len(lst_minus))
    for row in lst_in:
        if any(word in row for word in lst_minus): lst_in.remove(row)
    print(*lst_in, file=f_out, sep='\n')
    for row in range(len(lst_minus)):
        bar.next()
        time.sleep(0.01)
input(f'\n\nCписок сохранен в файл "out.txt" в папке "data".\n\nНажмите Enter для выхода')