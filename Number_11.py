h = int(input("Введите высоту: "))
for i in range(1, h+1):
    print((h-i) * ' ', (2 * i - 1) * '*', sep='')
