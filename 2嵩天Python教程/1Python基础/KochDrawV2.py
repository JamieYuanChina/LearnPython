# KochDrawV2.py
import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angel in[0, 60, -120, 60]:
            turtle.left(angel)
            koch(size/3, n-1)


def main():
    turtle.setup(800, 600)
    turtle.delay(0)
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.hideturtle()
    level = 5
    koch(400, level)  # 三阶科赫曲线
    turtle.right(120)
    koch(400, level)  # 三阶科赫曲线
    turtle.right(120)
    koch(400, level)  # 三阶科赫曲线
    turtle.hideturtle()
    turtle.done()


main()
