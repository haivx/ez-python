from turtle import Turtle, Screen, colormode
import colorgram
import random
timmy = Turtle()

# Draw square
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.seth(90)
# timmy.forward(100)
# timmy.seth(180)
# timmy.forward(100)
# timmy.seth(270)
# timmy.forward(100)
# ---------------------------------------------------#

# Draw dashes line
# def dashes(t, num_dashes, dash_length):
#     for i in range(num_dashes):
#         t.pendown()
#         t.forward(dash_length)
#         t.penup()
#         t.forward(dash_length)

# dashes(timmy, 10, 5)
# ---------------------------------------------------#

# Draw different shape

# timmy.shape("turtle")
# timmy.forward(100)
# timmy.seth(72) # 72 * 1
# timmy.forward(100)
# timmy.seth(144) # 72 * 2
# timmy.forward(100)
# timmy.seth(216) # 72 * 3
# timmy.forward(100)
# timmy.seth(288) # 72 * 4
# timmy.forward(100)
# 360 / n

# rgb_colors = []
# colors = colorgram.extract('spotpainting.jpg', 30)
#
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
              (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
              (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
              (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244),
              (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105)]

colormode(255)
timmy.penup()
timmy.hideturtle()

timmy.backward(300)


def draw(space, colors):
    x = len(colors)
    for i in range(x):
        for j in range(x):

            timmy.dot(20, random.choice(colors))
            timmy.forward(space)
        timmy.backward(space*x)
        timmy.left(90)
        timmy.forward(space)
        timmy.right(90)


draw(30, color_list)

screen = Screen()
screen.exitonclick()