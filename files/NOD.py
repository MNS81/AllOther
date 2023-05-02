a, b = map(int, input().split())
k = 0
while a != 0 and b != 0:
    if a > b: a %= b
    else: b %= a
    k += 1
print (a + b, k)