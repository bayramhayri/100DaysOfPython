import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(59, 106, 147), (223, 234, 230), (224, 201, 111), (235, 227, 207), (133, 84, 59), (221, 144, 68), (195, 145, 171), (142, 177, 202), (237, 224, 233), (139, 80, 104), (212, 92, 65), (69, 107, 90), (187, 80, 119), (133, 181, 135), (129, 135, 75), (64, 156, 93), (45, 156, 191), (183, 191, 201), (217, 176, 191), (20, 61, 96), (19, 68, 114), (117, 122, 148), (231, 175, 164), (171, 204, 183), (150, 209, 218), (53, 72, 66), (79, 66, 46), (105, 52, 46), (71, 55, 42)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()