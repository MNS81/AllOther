print('*** Join Keys ***')
print()
print('Для использования необходимо положить файлы "1.txt" и "2.txt" в папку "data".')
print('Программа получает списки ключей и объединяет их в отсортированный список уникальных комбинаций.')

with open('data/1.txt', encoding='utf-8') as first, open('data/2.txt', encoding='utf-8') as second, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    lst_1 = first.read().splitlines()
    lst_2 = second.read().splitlines()
    lst_out = []
    for word in lst_1:
        for key in lst_2:
            lst_out.append(f'{word} {key}')

for row in lst_out:
    outfile.write(row + '\n')
print('Список уникальных комбинаций сохранен в файл "out.txt" в папке "data".')
print()
input('Нажмите Enter для выхода')