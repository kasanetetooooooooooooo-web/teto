# counter=100
# while counter>=90:    
#     print(f"{counter}")
#     counter-=1
counter=10
summa=0
while counter<=20:
    summa+=counter
    counter+=1
print(f"{summa}")
summa=0
while True:
    number=input("введети число: ")
    if number=="stop":
        break
    number=int(number)
    summa+=number
    print(f"новая сумма={summa}")
