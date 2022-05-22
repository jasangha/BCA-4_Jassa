from turtle import *
import turtle
speed(20)
color('cyan')
bgcolor('black')

penup()
goto((105,-90))
pendown()

a = 200
while a>0:
    left(a)
    forward(a * 1)
    a = a - 1

penup()
forward(10)
pendown()

b=200
while b>0:
    left(b)
    forward(b * 1)
    b = b - 1

penup()
forward(10)
pendown()

c=200
while c>0:
    left(c)
    forward(c * 1)
    c = c - 1

penup()
forward(10)
pendown()

d=200
while d>0:
    left(d)
    forward(d * 1)
    d = d - 1

penup()
forward(10)
pendown()

e=200
while e>0:
    left(e)
    forward(e * 1)
    e = e - 1

penup()
forward(10)
pendown()

f=200
while f>0:
    left(f)
    forward(f * 1)
    f = f - 1

turtle.exitonclick()

