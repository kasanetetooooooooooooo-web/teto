users = {}

while True:
    action = input("\n1: Регистрация, 2: Вход, 3: Выход\nВыбор: ")
    if action == "3":
        print("Выход из программы.")
        break
        
    l, p = input("Логин: "), input("Пароль: ")
    
    if action == "1":
        if l in users:
            print("Логин занят!")
        else:
            users[l] = p
            print(users)
            print("Успешно зарегистрирован!")
            
    elif action == "2":
        if users.get(l) == p:
            print("Вход выполнен успешно! Программа завершена.")
            break 
        else:
            print("Неверный логин или пароль!")
