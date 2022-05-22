import turtle
import math

a = turtle.Turtle()
a.color('blue')
a.pensize(2)
a.speed(20)

for i in range(2000):
	a.forward(math.sqrt(i))
	a.left(i%180)

turtle.done() 