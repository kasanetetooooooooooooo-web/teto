score = 0
answer = input("Какая столица у Франции? ")
true_answer = "Париж"
if answer.strip() == true_answer:
    print("Молодец!")
    score += 1
else:
    print("Не угадал")
print(f"Ваш счет: {score}")



answer = input("Какая столица у Италии? ")
true_answer = "Рим"
if answer.strip() == true_answer:
    print("Молодец!")
    score += 1
else:
    print("Не угадал")
print(f"Ваш счет: {score}")

answer = input("Какая столица у России? ")
true_answer = "Москва"
if answer.strip() == true_answer:
    print("Молодец!")
    score += 1
else:
    print("Не угадал")
print(f"Ваш счет: {score}")

answer = input("Какая столица у Нидерландов? ")
true_answer = "Амстердам"
if answer.strip() == true_answer:
    print("Молодец!")
    score += 1
else:
    print("Не угадал")
print(f"Ваш счет: {score}")

answer = input("В каком городе находится монумент 'Родина-мать'? ")
true_answer = "Волгоград"
true_answer2 = "Набережные Челны"
if answer.strip() == true_answer or answer.strip() == true_answer2:
    print("Молодец!")
    score += 1
else:
    print("Не угадал")
print(f"Ваш счет: {score}")





if score == 5:
    print("Феноменально! Всё правильно")
if score == 4: 
    print("Ошибся 1 раз. Не плохо")