
points = 0
def add():
    global points
    points += 1

def show():
    print(f"У тебя сейчас очков: {points}")
    
def boat_sail_forward():
    print("Лодочка плывет вперед")
    add()

def boat_sail_backward():
    print("Лодочка плывет назад")
    add()

def boat_sail_left():
    print("Лодочка поворачивает налево")
    add()
    
def boat_sail_right():
    print("Лодочка поворачивает направо")
    add()

import msvcrt
while True:
    byte_key = msvcrt.getch() # клавиша, но в байтовом виде
    key = byte_key.decode()
    print(f"Нажата клавиша {key}")
    if key == 'q':
        print("До свидания!")
        exit()
    elif key == 'w':
        boat_sail_forward()
    elif key == 's':
        boat_sail_backward()
    elif key == 'a':
        boat_sail_left()
    elif key == 'd':
        boat_sail_right()
    elif key == "1":
        add()
    elif key == '2':
        show()
        
        


    
