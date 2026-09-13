


def say_hello():
    print("Привет!")
def time_to_eat():
    print("Пора покушать!")
def time_to_sleep():
    print("Спать пора!")

def my_function():
    x = 10 # x - локальная переменная внутри функции
    print("Значение x внутри функции:", x)

y = 20  # y - глобальная переменная
def my_function():
    print("Значение y внутри функции:", y)
    
z = 30  # z - глобальная переменная
def my_function():
    global z
    z = 40  # Изменение значения глобальной переменной
    print("Значение z внутри функции:", z)

print("Значение z за пределами функции:", z)
my_function()
print("Значение z за пределами функции:", z)  # Значение z изменилось на 40


game = "не пройдена"
def play_game():
    global game
    game = "пройдена"
    print("Вызвали функцию ", game)

print("До: ", game)
play_game()
print("После: ", game)






