from turtle import *
from random import randrange
from freegames import square, vector
import os

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
audio = "F:\VS_Code\PYTHON\jassa.wav"

getscreen().bgcolor("orange")
forward(100)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -340 < head.x < 320 and -280 < head.y < 280

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    
    if not inside(head) or head in snake:
        square(head.x, head.y, 11, 'red')
        update()
        os.system(audio)
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake)-1)
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear() 

    for body in snake:
        square(body.x, body.y, 11, 'green')

    square(food.x, food.y, 11, 'purple')
    
    update()
    ontimer(move, 100)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), "d"), onkey(lambda: change(10, 0), "Right")
onkey(lambda: change(-10, 0), "a"), onkey(lambda: change(-10, 0), "Left")
onkey(lambda: change(0, 10), "w"), onkey(lambda: change(0, 10), "Up")
onkey(lambda: change(0, -10), "s"), onkey(lambda: change(0, -10), "Down")
move()
exitonclick()
# done()