temp = input("Сколько сейчас градусов? ")
temp = int(temp)
if temp < -30:
    print("Очень холодно, не стоит выходить из дома")
elif temp < -15:
    print("Довольно холодно, но гулять можно")
elif temp < 0:
    print("Прохладно, нужно надеть куртку теплее")
elif temp < 5:
    print("...")
else:
    print("Очень жарко")    