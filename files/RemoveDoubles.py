import time
from progress.bar import IncrementalBar
with open('data/receipt.txt', encoding='utf-8') as file, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    print('*** Remove Doubles ***')
    print()
    print('Программа удаляет дубликаты ключей в списке.')
    print('Для использования необходимо положить файлы "receipt.txt" в папку "data".')
    print()
    lines = file.read().splitlines()
    result = set()
    for line in lines:
        temp = line.split()
        for word in temp: result.add(word)
    print(*sorted(result), file=outfile, sep='\n')
    bar = IncrementalBar('Пум-пум-пи-дум...', max=len(result))
    for row in sorted(result):
        bar.next()
        time.sleep(0.01)
input(f'\n\nСписок сохранен в файл "out.txt" в папке "data".\n\nНажмите Enter для выхода')