while True:
    passwd = input('Введите пароль: ')
    confirm = input('Повторите пароль: ')
    if len(passwd)<8 :
        print('Короткий!')
    elif '123' in passwd:
        print('Простой!')
    elif passwd != confirm:
        print('Различаются!')
    else:
        print('OK')
        break