from turtle import Turtle
import random

tim = Turtle()

colors = ["cornflower blue","deep sky blue","red","blue","pink","yellow"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side in range(3, 10):
#     tim.color(random.choice(color))
#     draw_shape(shape_side)

direction = [0,90,180,270]

tim.pensize(7)
tim.speed(10)
for _ in range(1000):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(direction))