import turtle as t
import os

y = "Rana"
z = "Jassa"
# Score
player_a_score = 0
player_b_score = 0

win = t.Screen()    # window
win.title("------------------------------------------------------------------Jassa-------------------------------------------------------------------")
win.bgcolor('pink')
win.setup(width=800, height=600)
win.tracer(10)   # speed

# Left paddle
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('red')
paddle_left.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Right paddle
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=6, stretch_len=0.8)
paddle_right.color('blue')
paddle_right.penup()
paddle_right.goto(350, 0)

# Ball
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0, 0)
ball_dx = 1.0  # Speed
ball_dy = 1.0

# Pen
pen = t.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}: 0                 {}: 0 ".format(y, z),
          align="center", font=('Monaco', 24, "normal"))


def paddle_left_up():
    y = paddle_left.ycor()
    y = y + 90
    paddle_left.sety(y)


def paddle_left_down():
    y = paddle_left.ycor()
    y = y - 90
    paddle_left.sety(y)


def paddle_right_up():
    y = paddle_right.ycor()
    y = y + 90
    paddle_right.sety(y)


def paddle_right_down():
    y = paddle_right.ycor()
    y = y - 90
    paddle_right.sety(y)


win.listen()
win.onkeypress(paddle_left_up, "w")
win.onkeypress(paddle_left_down, "s")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")
# Main
while True:
    win.update()
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border
    if ball.ycor() > 290:   # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1

    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1

    if ball.xcor() > 390:   # right width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("{}: {}                 {}: {} ".format(
            y, player_a_score, z, player_b_score), align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    if(ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("{}: {}                 {}: {} ".format(
            y, player_a_score, z, player_b_score), align="center", font=('Monaco', 24, "normal"))
        os.system("afplay wallhit.wav&")

    # Handling the collisions with paddles.
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_right.ycor() + 90 and ball.ycor() > paddle_right.ycor() - 90):
        ball.setx(340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")

    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < paddle_left.ycor() + 90 and ball.ycor() > paddle_left.ycor() - 90):
        ball.setx(-340)
        ball_dx = ball_dx * -1
        os.system("afplay paddle.wav&")
