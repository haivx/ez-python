from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)
start_position = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for i in start_position:
    segment_1 = Turtle(shape="square")
    segment_1.color("white")
    segment_1.penup()
    segment_1.goto(i)
    segments.append(segment_1)


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(10)




screen.exitonclick()
