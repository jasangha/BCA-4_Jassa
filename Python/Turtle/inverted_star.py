import turtle
line=turtle.Turtle()

line.getscreen().bgcolor("brown")
line.speed(10)
line.penup()
line.color('pink')
line.goto((-200,100))
line.pendown()

line.begin_fill()
for i in range(5):
	line.forward(360)
	line.left(216)
line.end_fill()

turtle.done()