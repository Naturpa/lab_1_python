n = int(input('Введите высоту прямоугольника: '))
m = int(input('Введите ширину прямоугольника: '))
s = input('Введите символ контура: ')
for i in range(m):
    print(s, end='')
print()
for i in range(n - 2):
    print(s, end='')
    for j in range(m - 2):
        print(' ', end='')
    print(s)
for i in range(m):
    print(s, end='')
