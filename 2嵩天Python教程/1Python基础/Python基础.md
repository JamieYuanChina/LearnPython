1、温度转换例程

eval为评估函数，会吧参数中最外层引号去掉，并且尝试执行。

int函数会把字符串类型的数字转换为整形，如果字符串中含有非数字字符，会报错。

print("%s 摄氏度等于 {:.2f} 华氏度！".format(F) % Temp_str[0:-1])

print（）函数用槽格式和format（）方法将变量和字符串结合到一起输出

2、画蟒蛇图

使用turtle库，这个库是为python2.x准备的，在python3.x中安装会报错，修改安装文件setup.py中低40行，添加括号后适应python3.x语法即可使用。（except (ValueError, ve):）

下载地址：

```
https://files.pythonhosted.org/packages/ff/f0/21a42e9e424d24bdd0e509d5ed3c7dfb8f47d962d9c044dba903b0b4a26f/turtle-0.0.2.tar.gz
```

解压缩后使用如下语句安装：

```
pip3 install -e ./turtle-0.0.2/
```

turtle.setup(weith,heigth,startx,starty)

这个函数生成一块画布（窗体）,这个函数不是必须的，如果不用修改参数，可以不调用。不调用该语句会在屏幕中间生成一个窗体。最小绘图单位为像素。

在turtle中，以窗体中心为坐标原点，向右为x正直，向左为x值负值，向上为y值正值，想下为y值负值。

在turtle中还支持相对坐标系，即向前，向后，向左，向右运动。

颜色系统采用RGB，可以使用0 ~ 255范围，也可使用0 ~ 1范围。使用turtle.colormode(mode) 1.0/255

```python
import turtle
turtle.goto(100, 100)
turtle.goto(100, -100)
turtle.goto(-100, -100)
turtle.goto(-100, 100)
turtle.goto(0, 0)
```

turtle可是使用角坐标

turtle.seth(angel)改变海龟的方向，x轴方向为0度，y轴方向为90度。

```python
import turtle
turtle.left(45)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turgle.left(135)
turtle.fd(150)
```

turtle.penup()抬起画笔，别名turtle.pu()

turgle.pendown()l落下画笔,别名turtle.pd()

turtle.pensize(width)设置画笔宽度，别名 turtle.width(width)

turtle.pencolor(“purple”)设置颜色

turtle.pencolor(0.63, 0.13, 0.94)

turtle.forward(d)  向前走直线，别名turtle.fd(d)

turtle.circle(r, extent=None)，根据半径r绘制 extent角度的弧形。默认圆心在海龟左侧距离位置。

turtle.done()保持窗口







