import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")

def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_graph)

draw_spirograph(5)


screen = t.Screen()
screen .exitonclick()
# for _ in range(50):
#    tim.forward(5)
#    tim.penup()
#    tim.forward(5)
#    tim.pendown()

# colors = ["AliceBlue", "azure2", "brown2", "SteelBlue1", "PapayaWhip", "khaki3", "firebrick1", "IndianRed1"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#    tim.color(random_color())
#    tim.forward(25)
#    tim.setheading(random.choice(directions))

# def draw_shape(num_sides):
#    deg = 360 / num_sides
#    for _ in range(num_sides):
#        tim.forward(100)
#        tim.right(deg)

# for shape_side_n in range(3,10):
#    tim.color(random.choice(colors))
#    draw_shape(shape_side_n)
