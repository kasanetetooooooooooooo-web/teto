
span = False
sword = False
key1 = False
key2 = False
levitation_power = 0
health = 100


def action1_bring_span():
    global span
    answer = input("Взять ложку? ")
    if answer.lower() == "да":
        print("Вы взяли ложку")
        span = True
    else:
        print("Вы пошли дальше")
    
def action8_eating():
    global span, levitation_power
    loop = True
    while loop:
        answer = input("Вы нашли еду: гриб незнамо какой и суп. Что будете есть?")
        if answer == "суп":
            if span == True:
                print("Суп оказался волшебным. У тебя появилась сила левитации")
                levitation_power = 1
                loop = False
            else:
                print("Ты не можешь есть суп")
        elif answer == "гриб":
            print("Вы умерли")