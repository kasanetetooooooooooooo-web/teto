import math
print("загадай число. пусть пк отгадает число")
low=int(input("выбери минимальное число: "))
max_number=int(input("выьерите максимальное число: "))
attempts=math.ceil(math.log2(max_number-low))#ceil -это округление в большую сторону(7.1-8), log2 - это логарифм это степинь двойки
print(f"теперь загадай число от {low} до {max_number}")#1-100 65
print(f"я справлюсь за {attempts} попыток")
counter=1
while True:
    number_pc=(low+max_number)//2
    user=input(f"ваше число-{number_pc}. да, больше меньше?: ")
    if (user=="больше"):
        low=number_pc+1
        print(f"хорошо буду искать от {low} до {max_number}")

    elif (user=="меньше"):
        max_number=number_pc-1
        print(f"хорошо буду искать от {low} до {max_number}")

    elif (user=="да"):
        print(f"ура я отгадал твоё число за {counter} попыток ")
        break
    else:
        print("Доступные ответы только больше меньше или да")
        continue
    counter+=1
