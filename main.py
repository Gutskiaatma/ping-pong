from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PINGPONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

bal = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(bal.move_speed)
    screen.update()
    bal.move()


    # Detect wall collision
    if bal.ycor() > 280 or bal.ycor()< -280:
        bal.bounce_y()

    # Detect collision with the right paddle
    if bal.distance(r_paddle) < 50 and bal.xcor() > 320 or bal.distance(l_paddle) < 50 and bal.xcor() < -320:
        bal.bounce_x()

    # Detect r_paddle miss
    if bal.xcor() > 380:
        bal.reset_position()
        scoreboard.l_point()


    # Detect l_paddle miss
    if bal.xcor() < -380:
        bal.reset_position()
        scoreboard.r_point()

screen.exitonclick()