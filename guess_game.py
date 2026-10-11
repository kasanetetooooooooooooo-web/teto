print("загадай число. пусть пк отгадает число")
low=int(input("выбери минимальное число: "))
max_number=int(input("выьерите максимальное число: "))
print(f"теперь загадай число от {low} до {max_number}")
number_pc=(low+max_number)//2
print(number_pc)