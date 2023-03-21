with open('data/in.txt', encoding='utf-8') as file, open('data/out.txt', 'w', encoding='utf-8') as outfile:
    lines = file.read().splitlines()
    res = set()
    for line in lines:
        temp = line.split()
        for i in temp: res.add(i)
    print(*sorted(res), file=outfile, sep='\n')