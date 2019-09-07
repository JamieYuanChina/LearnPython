import turtle


def draw_gap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)


def draw_line(draw):  # 绘制单段数码管
    draw_gap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    draw_gap()
    turtle.right(90)


def draw_digit(digit):  # 根据数字绘制七段数码管
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 6, 8] else draw_line(False)
    turtle.left(90)
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.left(180)
    turtle.penup()  # 为绘制后续数字确定位置
    turtle.fd(20)  # 为绘制后续数字确定位置


def draw_data(data):  # 获得要输出的数字
    for i in data:
        draw_digit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    turtle.pencolor("red")
    draw_data("20181010")
    turtle.hideturtle()
    turtle.done()


main()
