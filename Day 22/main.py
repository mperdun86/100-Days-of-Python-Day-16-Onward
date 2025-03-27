from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_PADDLE_HOME = (-350, 0)
RIGHT_PADDLE_HOME= (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()

right_paddle = Paddle(RIGHT_PADDLE_HOME)
left_paddle = Paddle(LEFT_PADDLE_HOME)

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_increase()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_increase()









screen.exitonclick()