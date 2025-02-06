login= input("Введите логин: ")
address= input("Введите резервный адрес: ")
if "@" in login:
    print ("Некорректный логин!")
else:
    print ("Корректный логин")
if "@" in address:
    print ("Корректный адрес!")
else:
    print ("Некорректный адрес!")
