n = int(input())
s = 'программист'
if 2 <= n % 10 <= 4 and not 12 <= n % 100 <= 14: print(n, s + 'а')
elif n % 10 == 1 and n % 100 != 11: print(n, s)
else: print(n, s + 'ов')