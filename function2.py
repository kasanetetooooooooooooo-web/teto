import time

def cook(dish_name):
    print(f"Начинаем готовку блюда {dish_name}")
    time.sleep(1)
    print(f"Блюдо {dish_name} готово!")


def greet(name): # name - это параметр
    print(f"Hello, {name}")
    
def farewell(name):
    print(f"Bye-bye, {name}")


cook("пельмени")
cook("шашлык")
cook("уха")
