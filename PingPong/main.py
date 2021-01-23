from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title('Ping pong')
screen.tracer(0)

turtle_r = Paddle(350, 0)
turtle_l = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle_l.go_up, 'Up')
screen.onkey(turtle_l.go_down, 'Down')
screen.onkey(turtle_r.go_up, 'w')
screen.onkey(turtle_r.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(turtle_r) < 50 and ball.xcor() > 320 or ball.distance(turtle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()

screen.exitonclick()
