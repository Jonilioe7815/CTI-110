import turtle
import random

win = turtle.Screen()
qq = turtle.Turtle()
colors = ["red", "black", "blue", "green", "yellow"]

qq.pensize(2)
qq.shape("circle")

def main():

    def flake (sf_draw):
        for i in range (1, 19):
            qq.forward(50)
            qq.right(120)
            qq.forward(50)
            qq.right(50)


    for i in range(20):
        x = random.randrange(-300, 300)
        y = random.randrange(-300, 300)
        sf_draw = random.randint(1, 2)
        qq.penup()
        qq.goto(x, y)
        qq.color(random.choice(colors))
        qq.pendown()
        flake (sf_draw)

main()

