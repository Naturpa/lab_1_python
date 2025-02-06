number=input("Введите трехзначное число: ")
number1=[int(n) for n in number]
if (max(number1)+min(number1))/2 == sum(number1)-max(number1)-min(number1):
    print("Вы ввели красивое число!")
else:
    print("Жаль, вы ввели обычное число:(")