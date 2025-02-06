import math
while True:
    s1 = input("Введите число: ")
    s2 = input("Введите знак операции: ")
    if s2=='+':
        s3 = input("Введите число: ")
        print(int(s1)+int(s3))
    if s2=='-':
        s3 = input("Введите число: ")
        print(int(s1)-int(s3))
    if s2=='*':
        s3 = input("Введите число: ")
        print(int(s1)*int(s3))
    if s2=='/':
        s3 = input("Введите число: ")
        if int(s3)!=0:
            print(int(s1)//int(s3))
    if s2 == '%':
        s3 = input("Введите число: ")
        if int(s3) != 0:
            print(int(s1) % int(s3))
    if s2=='!' and int(s1)>=0:
        print(math.factorial(int(s1)))
    if s2 == 'x':
        print(s1)
        break
