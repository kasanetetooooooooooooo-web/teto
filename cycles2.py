# students = ["Дамир", "Райхан", "Глеб", "Кирилл", "Данель", "Елизавета"]

# for student in students:
#     print(f"{student} - красавчик!")

# games = ["Resident Evil", "Silent Hill", "Sonic Adventure", "Little Nightmares"]

# for game in games:
#     print(f"Я играл в {game}! Было круто!")

# for bukva in "tiktok":
#     print(bukva)

# # По числам и True-False нельзя идти циклом фор!
# # for number in 123456789:
# #    print(number)







# # Задание 3. «Энергия робота» У робота есть запас энергии, который начинается с 50 единиц.
# # Каждый час робот тратит энергию: в первый час — 2 единицы, во второй — 4,
# # в третий — 6 и так далее (каждый час на 2 единицы больше).
# # Напишите код, который выведет, сколько энергии останется у робота через 8 часов.

# energy = 100
# number = 8
# cost = 2
# while number > 0:
#     number -=1
#     energy -= cost
#     print(f"Энергия робота = {energy}, стоимость работы - {cost} ед.")
#     cost += 2
    
# energy = 100
# cost = 2
# for hour in range (1,9):
#     energy -= cost
#     print(f"Час {hour}. Энергия робота = {energy}, стоимость работы - {cost} ед.")
#     cost += 2


# 3, 6, 9, 12, 15
for i in range(3, 16, 3):
    print(i)

# # 10, 20, 30, 40, 50
for i in range(10, 51, 10):
    print(i)
    
# 5, 4, 3, 2, 1
for i in range(5, 0, -1):
    print(i)




























# # import datetime, time
# # date = datetime.datetime.strptime('2026-04-04 11:30', '%Y-%m-%d %H:%M')

# # while True:
# #     date_now = datetime.datetime.now()
# #     difference = date - date_now
# #     print(difference)
# #     time.sleep(1)