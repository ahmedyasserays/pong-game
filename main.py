import turtle


window = turtle.Screen()
window.title("ping pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# first player (right)
right = turtle.Turtle()
right.speed(0)
right.shape("square")
right.color("blue")
right.penup()
right.goto(350, 0)
right.shapesize(stretch_wid=5, stretch_len=1)
right_score = 0


# second player (left)
left = turtle.Turtle()
left.speed(0)
left.shape("square")
left.color("red")
left.penup()
left.goto(-350, 0)
left.shapesize(stretch_wid=5, stretch_len=1)
left_score = 0


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4


# moving
dy = 0.5
players_speed = 30
right_new_pos = right.ycor()
left_new_pos = left.ycor()


def right_up():
    global right_new_pos
    right_new_pos += players_speed


def right_down():
    global right_new_pos
    right_new_pos -= players_speed


def left_up():
    global left_new_pos
    left_new_pos += players_speed


def left_down():
    global left_new_pos
    left_new_pos -= players_speed


# keyboard
window.listen()
window.onkeypress(left_up, "w")
window.onkeypress(left_down, "s")
window.onkeypress(right_up, "Up")
window.onkeypress(right_down, "Down")

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle()
score.penup()
score.goto(0, 260)
score.write("player one: {} player two: {}".format(left_score, right_score), align="center",
            font=("courier", 24, "normal"))

# game logic loop
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if right_new_pos >= 250:
        right_new_pos = 250
    elif right_new_pos <= -250:
        right_new_pos = -250
    elif left_new_pos >= 250:
        left_new_pos = 250
    elif left_new_pos <= -250:
        left_new_pos = -250

    if right.ycor() < right_new_pos:
        right.sety(right.ycor() + dy)
    elif right.ycor() > right_new_pos:
        right.sety(right.ycor() - dy)

    if left.ycor() < left_new_pos:
        left.sety(left.ycor() + dy)
    elif left.ycor() > left_new_pos:
        left.sety(left.ycor() - dy)

    if right.ycor() >= 250:
        right.sety(250)

    if right.ycor() <= -250:
        right.sety(-250)

    if left.ycor() >= 250:
        left.sety(250)

    if left.ycor() <= -250:
        left.sety(-250)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            left_score += 1
            score.clear()
            score.write("player one: {} player two: {}".format(left_score, right_score), align="center",
                        font=("courier", 24, "normal"))

        else:
            right_score += 1
            score.clear()
            score.write("player one: {} player two: {}".format(left_score, right_score), align="center",
                        font=("courier", 24, "normal"))

        ball.goto(0, 0)
        ball.dx *= -1

    if (330 <= ball.xcor() <= 350) and (right.ycor() - 50 <= ball.ycor() <= right.ycor() + 50):
        ball.setx(330)
        ball.dx *= -1

    if (-330 >= ball.xcor() >= -350) and (
            left.ycor() + 50 >= ball.ycor() >= left.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

    if (350 <= ball.xcor() <= 360) and (
            right.ycor() - 50 <= ball.ycor() <= right.ycor() + 50):
        ball.dy *= -1

    if (-350 >= ball.xcor() >= -360) and (
            left.ycor() - 50 <= ball.ycor() <= left.ycor() + 50):
        ball.dy *= -1

    if right_score == 10:
        right_score = 0
        left_score = 0
        score.clear()
        score.write("player one wins", align="center",
                    font=("courier", 24, "normal"))

    if left_score == 10:
        right_score = 0
        left_score = 0
        score.clear()
        score.write("player one wins", align="center",
                    font=("courier", 24, "normal"))
