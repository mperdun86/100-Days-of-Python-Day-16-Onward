import turtle as t
import random
import colorgram

bob = t.Turtle()
bob.speed("fastest")
t.colormode(255)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51), (6, 68, 42), (176, 176, 233), (239, 168, 161), (249, 8, 48), (5, 246, 222), (15, 76, 110), (243, 15, 14), (38, 43, 221)]

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
# # def spyrograph(gap):
#     for i in range (int(360 / gap)):
#         bob.color(random_color())
#         bob.circle(100)
#         bob.setheading(tim.heading() + gap)
#
# spyrograph(5)
#
# colors = colorgram.extract('image.jpg', 40)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

bob.setheading(225)
number_of_dots = 100
bob.hideturtle()
bob.up()
bob.forward(300)
bob.setheading(0)

for dot_count in range(1, number_of_dots + 1):
    bob.dot(20, random.choice(color_list))
    bob.forward(50)
    if dot_count % 10 == 0:
        bob.setheading(90)
        bob.forward(50)
        bob.setheading(180)
        bob.forward(500)
        bob.setheading(0)

screen = t.Screen()
screen.exitonclick()

