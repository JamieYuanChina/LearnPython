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
turtle.circle(r, extent=None)，根据半径r绘制 extent角度的弧形。默认圆心在海龟左侧。
turtle.done()保持窗口

3、整数

pow(x,y)函数，计算x^y^ 。
浮点数判等于使用rount(x,d)进行辅助。即对x进行四舍五入，d为小数截取位数。
使用e或者E作为幂的符号，以10为基数格式如下：
<a>e<b> 表示a*10^b^
python支持虚数4+5j
x //y整数除功能，10//3结果为3
x%y余数，模运算10%3结果是1
x**y幂运算，x的y次幂
abs(x) 取绝对值
divmod(x,y)商余，同时输出商和余数，divmod(10,3)结果(3, 1)
pow(3,pow(3,99))  幂余，
round(x[,d]) 四舍五入，d是保留的小数位。
max(x1,x2,...,xn)
min(x1,x2,...,xn)

int(x),将x变成整数，舍弃小舒部分，可以将字符串转换为数字。
float(x),变成浮点数，增加小舒部分，可以将字符串转换为数字
complex(x)变成复数，增加虚数部分，可以将字符串转换为数字

4、字符串

字符串处理函数
len(x)计算字符串长度
str(x)把数组转换为字符串
hex(x)或者oct(x)转换为十六进制或者八进制
chr(u) u为Unicode编码，返回起对应的字符
ord(x)x为字符，返回对应的UNICODE编码

UNICODE编码从0到1114111(0x10FFFF)空间每个编码对应一个字符。

```
>>> "1 + 1 = 2 " + chr(10004)
'1 + 1 = 2 ✔'
```

字符串处理方法

str.lower()或者str.upper()返回字符串副本，全部大些或者小写
str.split(sep=None)返回一个列表，由str根据sep被分割的组成部分。
str.count(sub)返回子串sub在str中出现的次数
str.replace(old, new)替换字符串
str.center(width[,fillchar]) "python".center(20,"="),结果‘= = = = = = = python= = = = = = =’
str.strip(chars)从str中去掉其左侧和右侧chars中列出的字符
str.join(iter) 在iter变量除最后元素外每个元素后增加一个str，",".join("12345")结果"1,2,3,4,5",主要用来分隔字符串

5、字符串的槽：

“{ }:计算机{ }的cpu占用率为{}%”.format("2018=10-10","C",10)

槽内部对格式化的配置方式

{<参数序号>:<格式控制标记>}

| :      | <填充>   | <对齐>  | <宽度>  | <,>      | <.精度>  | <类型>   |
| ------ | ------- | ------ | ------  | -------  | ------- | -------- |
| 引导符号 | 单个字符 | <左对齐 | 输出宽度 | 千位分隔符 | 小数精度 | 整数类型  |
|         |        | >右^居中|       |      |     | b,c,d,o,x,X,e,E,F,%|

"{0:=^20}".format("PYTHON")  ；0为format中的序号，:引导符号；=为填充字符；^为中间对齐；20为输出宽度

 输出为‘= = = = = = = PYTHON = = = = = = =’

“{:10}”.format("BIT")，默认序号0，默认填充空格，默认左对齐 

6、time库

time()获取当前时间戳
ctime()获取人类可读时间
gmtime()获取程序可读时间

```
>>> time.time()
1567774350.7066476
>>> time.ctime()
'Fri Sep  6 20:53:33 2019'
>>> time.gmtime()
time.struct_time(tm_year=2019, tm_mon=9, tm_mday=6, tm_hour=12, tm_min=54, tm_sec=5, tm_wday=4, tm_yday=249, tm_isdst=0)
```
strftime(tpl.ts)格式化时间戳。
strptime(str,tpl)根据给定的字符串获得时间戳值。

```
>>> t = time.gmtime()
>>> time.strftime("%Y-%m-%d %H:%M:%S",t)
'2019-09-06 12:57:14'
```

程序计时函数，perf_counter()
休眠sleep()

```
>>> start = time.perf_counter()
>>> end = time.perf_counter()
>>> end-start
23.288312510999276
>>> time.sleep(4)
```

文本进度条

```python
# TextProBarV1.py
import time
scale = 10
print("-----执行开始------")
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.5)

print("-----执行结束------")
```

```python
# TextProBarV2.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end="")
    time.sleep(0.1)
```

```python
# TextProBarV3.py
import time
scale = 50
print("执行开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = "*" * i
    b = "." * (scale - i)
    c = (i/scale) * 100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end="")
    time.sleep(0.1)

print("\n"+"执行结束".center(scale//2, "-"))
```

7、分支结构

单分支 if
二分支 if ……else……
紧凑形式的二分支  ，如果if后面的城西，返回if前面的表达式，否则返回else后面的表达式，类似于C中的 ? :

```
guess = enal(input()) 
print("猜{}了".format("对" if guess == 99 else "错"))
```

多分支 if……elif……else……

条件判断使用的操作符：

| 操作符 | 数学符号 | 描述     |
| ------ | -------- | -------- |
| <      | <        | 小于     |
| <=     | ≤        | 小于等于 |
| >=     | ≥        | 大于等于 |
| >      | >        | 大于     |
| ==     | =        | 等于     |
| !=     | ≠        | 不等于   |

三个条件保留字

| 操作符以及使用 | 描述                  |
| -------------- | --------------------- |
| x and y        | 两个条件 x和y的逻辑与 |
| x or y         | 两个条件 x和y的逻辑或 |
| not x          | 条件x的逻辑非         |

95