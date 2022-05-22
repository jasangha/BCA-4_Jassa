import turtle
line=turtle.Turtle()
line.getscreen().bgcolor("brown")
line.speed(15)
line.color('pink')
line.penup()
line.goto((-200,100))
line.pendown()

def star(turtle, size):
	if size <= 10:
		return 0
	else:
		turtle.begin_fill()
		for i in range(5):

			turtle.forward(size)
			star(turtle, size/5)
			turtle.left(216)
		turtle.end_fill()

# star(line,100)
star(line,360)

turtle.done()