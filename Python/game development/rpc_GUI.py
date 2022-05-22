import random
def lost():
    import turtle
    turtle.speed(20)
    turtle.color('blue','cyan')
    turtle.pensize(3)

    # upper left
    turtle.penup()
    turtle.left(180)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(130)
    turtle.left(270)
    turtle.forward(40)
    turtle.pendown()

    # Y
    turtle.begin_fill()
    turtle.left(-45)
    turtle.forward(57)
    turtle.left(90)
    turtle.penup()
    turtle.forward(56)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(57)
    turtle.left(45)
    turtle.forward(60)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()

    # O
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()

    # U
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.pendown()

    # L
    turtle.begin_fill()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

    # O
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()

    # S
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    
    # T
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(180)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.exitonclick() 
def won():
    import turtle
    turtle.speed(10)
    turtle.color('blue','cyan')
    turtle.pensize(3)

    turtle.penup()
    turtle.left(180)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(130)
    turtle.left(270)
    turtle.forward(60)
    turtle.pendown()

    # Y
    turtle.begin_fill()
    turtle.left(-45)
    turtle.forward(57)
    turtle.left(90)
    turtle.penup()
    turtle.forward(56)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(57)
    turtle.left(45)
    turtle.forward(60)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()

    # O
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.pendown()

    # U
    turtle.begin_fill()
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.right(90)
    turtle.forward(60)
    turtle.pendown()

    #W
    turtle.begin_fill()
    turtle.right(80)
    turtle.forward(100)
    turtle.left(150)
    turtle.forward(50)
    turtle.right(138)
    turtle.forward(50)
    turtle.left(148)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.right(180)
    turtle.forward(102)
    turtle.left(100)
    turtle.forward(30)
    turtle.pendown()

    # O
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.end_fill()

    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.pendown()

    # N
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.right(155)
    turtle.forward(110)
    turtle.left(155)
    turtle.forward(100)
    turtle.end_fill()

    turtle.exitonclick()
def draw():
    import turtle
    turtle.speed(10)
    turtle.color('blue','cyan')
    turtle.pensize(3)

    turtle.penup()
    turtle.left(180)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(170)
    turtle.left(90)
    turtle.pendown()

    # D
    turtle.begin_fill()
    turtle.forward(100)
    turtle.right(100)
    turtle.forward(50)
    turtle.right(80)
    turtle.forward(80)
    turtle.right(77)
    turtle.forward(50)
    turtle.end_fill()

    turtle.penup()
    turtle.right(183)
    turtle.forward(60)
    turtle.pendown()

    # R
    turtle.begin_fill()
    turtle.left(80)
    turtle.forward(85)
    turtle.right(93)
    turtle.forward(40)
    turtle.right(87)
    turtle.forward(40)
    turtle.right(85)
    turtle.forward(40)
    turtle.left(131)
    turtle.forward(60)
    turtle.end_fill()

    turtle.penup()
    turtle.left(45)
    turtle.forward(15)
    turtle.pendown()

    # A
    turtle.begin_fill()
    turtle.left(72)
    turtle.forward(90)
    turtle.right(146)
    turtle.forward(60)
    turtle.penup()
    turtle.right(107)
    turtle.forward(34)
    turtle.pendown()
    turtle.left(180)
    turtle.forward(34)
    turtle.right(72)
    turtle.forward(30)
    turtle.end_fill()

    turtle.penup()
    turtle.left(160)
    turtle.forward(90)
    turtle.pendown()

    # W
    turtle.begin_fill()
    turtle.right(165)
    turtle.forward(90)
    turtle.left(145)
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(142)
    turtle.forward(90)
    turtle.end_fill()

    turtle.exitonclick()

l=['r','p','s']
a=input('choose(r,p,s): ')
num=random.choice(l)
def pcturn(x):
    print('pc chose (',x,')')

if a=='r':
    pcturn(num)
    if num=='p':
        print('you lost !!!')
        lost()
    elif num=='r':
        print('match draw !!!')
        draw()
    else:
        print('you won !!!')
        won()
elif a=='p':
    pcturn(num)
    if num=='s':
        print('you lost !!!')
        lost()
    elif num=='p':
        print('match draw !!!')
        draw()
    else:
        print('you won !!!')
        won()
elif a=='s':
    pcturn(num)
    if num=='r':
        print('you lost !!!')
        lost()
    elif num=='s':
        print('match draw !!!')
        draw()
    else:
        print('you won !!!')
        won()
else:
    print("values sahi bhar !!!")
    
print()     
