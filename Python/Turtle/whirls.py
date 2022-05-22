from contextlib import redirect_stderr
from re import I
from turtle import *

bgcolor('black')
speed(0)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(i*.8)
    right(3)
    forward(3)
done()
