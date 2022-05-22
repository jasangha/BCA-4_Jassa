import turtle
import math

a = turtle.Turtle()
a.color('dark blue')
a.pensize(2)
a.speed(20)

for i in range(340):
	a.forward(10)
	a.left(math.sin(i/10)*25)
	a.left(20)

turtle.done()