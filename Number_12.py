N = int(input("Введите число: "))
q = 1
s = 1
k = 0
while q <= N:
    print(q, end=' ')
    q = q + 1
    k = k + 1
    if k == s:
        print()
        s = s + 1
        k = 0