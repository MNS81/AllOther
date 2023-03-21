with open('data/in.txt', encoding='utf-8') as f_in, open('data/minus.txt', encoding='utf-8') as f_minus, open('data/out.txt', 'w', encoding='utf-8') as f_out:
    lst_in = f_in.read().splitlines()
    lst_minus = f_minus.read().splitlines()
    for row in lst_in:
        if any(word in row for word in lst_minus): lst_in.remove(row)
    print(*lst_in, file=f_out, sep='\n')