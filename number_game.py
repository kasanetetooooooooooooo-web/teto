import random # библиотека


print("Привет! Я загадаю число от 1 до 100. Тебе надо отгадать его")
tries = 7
secret_number = random.randint(1, 100)
while tries > 0:
    user_number = input("Введи число: ") # str - строка
    user_number = int(user_number)

    if user_number > secret_number:
        print("Ваше число больше секретного")
    elif user_number < secret_number:
        print("Ваше число меньше секретного")
    else:
        print("Вау! Вы угадали!")
        break
    tries -= 1
    print(f"У вас осталось попыток: {tries}")






