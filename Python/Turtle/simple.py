import turtle

turtle.speed(10)
turtle.color('blue','cyan')
turtle.pensize(2)
# turtle.forward(100)

turtle.begin_fill()
for i in range(37):
    turtle.forward(100)
    turtle.left(170)
turtle.end_fill()

turtle.done() 