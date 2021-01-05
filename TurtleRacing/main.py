from turtle import  Turtle, Screen
import random
screen = Screen()

#
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def turn_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#
#
# screen.listen()
#
# screen.onkey(key="W", fun=move_forwards)
# screen.onkey(key="S", fun=move_backwards)
# screen.onkey(key="A", fun=turn_left)
# screen.onkey(key="D", fun=turn_right)
# screen.onkey(key="C", fun=clear)

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
temp = -150
all_turtle = []
for i in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(i)
    tim.goto(x=-230, y=temp)
    temp += 50
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in all_turtle:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner")
            else:
                print(f"You've lost!! The {winning_color} turtle is the winner")

        random_distance = random.randint(0, 8)
        t.forward(random_distance)


screen.exitonclick()

