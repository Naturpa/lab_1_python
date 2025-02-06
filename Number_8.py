height = input("Введите рост: ")
k = 0
MIN = 190
MAX = 150
while height != '!':
    height = int(height)
    if height >= 150 and height <= 190:
        k += 1
        if height >= MAX:
            MAX = height
        elif height <= MIN:
            MIN = height
    height = input("Введите рост: ")
print(k)
print(MIN, MAX)