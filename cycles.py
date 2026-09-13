import time 


# number = 1
# summa = 0
# while number <= 5: # повторять пока наше число меньше или равно 5
#     print(number)
#     summa += number
#     number += 1
# print("Программа закончилась")


num = 1
factorial = 1
while num <= 5:
    factorial *= num
    num += 1
print(f"Факториал 5 = {factorial}")




# counter = 10
# while counter >= 1:
#     print(counter)
#     counter -= 1
#     time.sleep(1)