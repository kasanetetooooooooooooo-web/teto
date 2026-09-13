import turtle

t = turtle.Turtle() # карандаш
t.speed(0)
t.shape('turtle')

def square():
    for i in range(4):
        t.forward(100) # вперед
        t.left(90) # налево

def rectangle():
    for i in range(2):
        t.forward(200)
        t.left(90)
        t.forward(100)
        t.left(90)

def triangle():
    for i in range(3):
        t.forward(200)
        t.left(120)


def polygon(side, distance=100):
    for i in range(side):
        t.forward(distance)
        t.left(360/side)

def star():
    for i in range(5):
        t.forward(100)
        t.left(144)

def center():
    t.setpos(0,0)

def up():
    t.setheading(90)
    t.forward(10)





t.screen.onkeypress(square, "1")
t.screen.onkeypress(center, "c")
t.screen.onkeypress(up, "Up")



t.screen.listen()
t.screen.mainloop() # цикл обработки событий (нажатие на клавиши, перемещение мышки)
