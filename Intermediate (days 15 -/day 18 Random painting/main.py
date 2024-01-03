
import turtle
import random
# import colorgram

# colorgram_colors = colorgram.extract('skynews-damien-hirst-art-the-currency_5906968.jpg', 30)
# colors = []
# for color in colorgram_colors:
#     colors.append(tuple(color.rgb))

colors = [(255,255,255), (223, 159, 80), (39, 107, 149), (118, 164, 192), (150, 63, 88), (207, 134, 157), 
          (180, 160, 35), (28, 133, 96), (213, 86, 59), (120, 181, 152), (164, 80, 52), (200, 84, 111), 
          (208, 225, 215), (143, 31, 40), (54, 167, 135), (232, 198, 110), (201, 219, 227), (229, 206, 214), 
          (6, 109, 90), (41, 160, 185), (117, 114, 163), (238, 159, 174), (30, 62, 112), (153, 211, 199), (235, 169, 158), 
          (26, 64, 57), (125, 38, 35), (28, 58, 84), (150, 208, 217), (69, 39, 50)]

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
turtle.colormode(255)

dot_spacing = 50
dot_num = 10

x_coord = -(dot_num*dot_spacing)/2
y_coord = x_coord
timmy.setpos(x_coord, y_coord)


for _ in range(dot_num):
    timmy.setpos(x_coord, timmy.pos()[1] + dot_spacing)
    for _ in range(dot_num):
        timmy.forward(dot_spacing)
        timmy.dot(20, random.choice(colors))

screen.exitonclick()
