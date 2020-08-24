import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Salam Waddah")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle Left
paddle_l = turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.shapesize(stretch_wid=5, stretch_len=1)
paddle_l.penup()
paddle_l.goto(-350, 0)

# Scores
score_r = 0
score_l = 0

# Paddle Right
paddle_r = turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.shapesize(stretch_wid=5, stretch_len=1)
paddle_r.penup()
paddle_r.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)


# Functions
def paddle_l_up():
    y = paddle_l.ycor()
    y += 30
    paddle_l.sety(y)


def paddle_l_down():
    y = paddle_l.ycor()
    y -= 30
    paddle_l.sety(y)


def paddle_r_up():
    y = paddle_r.ycor()
    y += 30
    paddle_r.sety(y)


def paddle_r_down():
    y = paddle_r.ycor()
    y -= 30
    paddle_r.sety(y)


def update_score():
    pen.clear()
    pen.write(
        "Player Right: {} Player Left: {}".format(score_r, score_l),
        align="center",
        font=("Courier", 24, "normal")
    )


def play_bounce_audio():
    os.system("afplay bounce.wav&")  # OSX
    # os.system("aplay bounce.wav&") # Linux
    # winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)  # Windows


update_score()

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # screen size 600 / 2 minus the ball size
        ball.sety(290)
        ball.dy *= -1
        play_bounce_audio()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_bounce_audio()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        update_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_l += 1
        update_score()

    # Paddle and ball collisions
    if (340 < ball.xcor() < 350) and (paddle_r.ycor() + 40 > ball.ycor() > paddle_r.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350) and (paddle_l.ycor() + 40 > ball.ycor() > paddle_l.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
