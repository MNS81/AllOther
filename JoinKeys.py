with open('data/1.txt', encoding='utf-8') as first, open('data/2.txt', encoding='utf-8') as second, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    lst_1 = first.read().splitlines()
    lst_2 = second.read().splitlines()
    for word in lst_1:
        for key in lst_2:
            print(word, key, file=outfile)