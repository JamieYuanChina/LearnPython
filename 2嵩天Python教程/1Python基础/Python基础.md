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
< a > e < b > 表示a*10^b^
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

8、循环

遍历循环，for …… in ……

for i in range(1,6)  # 其中的range函数的作用是产生一个数字序列；
for line in fi 对文件进行遍历。

无限循环，while 表达式 :

循环保留字：break和continue

9、random库

random包含两类共计8个函数

基本随机数函数：seed(),random()

扩展随机数函数：randint(),getrandbits(),uniform(),randrange(),choice(),shuffle()

seed(a=None) 初始化给定的随机数种子，默认为当前的系统时间。

种子数相同，产生随机数的序列相同。

```python
>>> import random
>>> random.seed(10)
>>> random.random()
0.5714025946899135
>>> random.random()
0.4288890546751146
```

扩展随机数函数

randint(a,b)生成a,b之间的随机整数

randrange(m,n[,k])生成一个[m,n)之间以K为步长的随机整数

getrandbits(k)生成一个Kbit长的随机整数

uniform(a,b)生成一个[a,b]之间的随机小数

choice(seq)从序列seq中随机选择一个元素

shuffle(seq)将序列seq中的元素随机排列，返回打乱后的序列。

```python
>>> random.randint(10,100)
83
>>> random.randrange(10,100,10)
10
>>> random.getrandbits(16)
13506
>>> random.uniform(10,100)
51.632245728365426
>>> random.choice([1,2,3,4,5,6,7,8,9])
8
>>> s=[1,2,3,4,5,6,7,8,9];random.shuffle(s);print(s)
[8, 7, 9, 3, 5, 2, 4, 1, 6]
```

如果多行代码需要放在一行，那么每一个语句后面增加分号即可。

10、圆周率的计算

圆周率近似计算公式

```python
# CalPiV1.py
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16, k) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
print("圆周率值是：{}".format(pi))

```

蒙特卡洛方法计算圆周率

```python
# CalPiV2.py
from random import random
from time import  perf_counter
DARTS = 1000 * 1000
hits = 0.0
start = perf_counter()
for i in range(1, DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率的值是：{}".format(pi))
print("运行时间是：{:.5}s".format(perf_counter() - start))
```

11、函数

lambda函数，一般用于简单表达式定义为函数，正常函数建议使用def定义。

<函数名> = lambda<参数>:<表达式>

```python
>>> f = lambda x,y:x+y
>>> f(4,5)
9
```

12、绘制七段数码管

```python
# SevenDigitsDrawV2.py
import turtle,time


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
    turtle.pencolor("red")
    for i in data:
        if i == "-":
            turtle.write("年", font=("Arial", 18, "normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == "=":
            turtle.write("月", font=("Arial", 18, "normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == "+":
            turtle.write("日", font=("Arial", 18, "normal"))
        else:
            draw_digit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    draw_data(time.strftime("%Y-%m=%d+", time.gmtime()))
    turtle.hideturtle()
    turtle.done()


main()
```

13、Pyinstall库

```shell
pip install pyinstaller
pyinstaller -F SevenDigitsDrawV2.py
```

pyinstaller参数

-h 查看帮助

--clean 清理打包过程中的临时文件

-D ，--onedir 默认值，生成dist文件夹

-F ，--onefile 只生成独立的打包文件

-i <图标文件名.ico> 指定打包程序使用的图标文件

pyinstaller -i curve.ico -F SevenDigitsDrawV2.py

14、科赫雪花

```python
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
    turtle.penup()
    turtle.goto(-200, 100)
    turtle.pendown()
    turtle.pensize(2)
    level = 3
    koch(400, level)  # 三阶科赫曲线
    turtle.right(120)
    koch(400, level)  # 三阶科赫曲线
    turtle.right(120)
    koch(400, level)  # 三阶科赫曲线
    turtle.hideturtle()
    turtle.done()


main()
```

分形几何：康托尔集，希尔宾斯基三角形，门格海绵，龙形曲线，空间填充曲线

15、集合

集合是多个元素的无序组合，使用大括号{}表示，元素间用逗号分隔。
集合不能包含相同的元素，所有元素唯一且无序。
建立集合类型使用{}或者set()，建立空即可，必须使用set()函数。

```python
>>> A = {"python",123,("python",123)}
>>> A
{123, 'python', ('python', 123)}
>>> B = set("pypy123")  # 使用set()建立集合
>>> B
{'2', 'p', '1', '3', 'y'}
```

集合的操作符

| 操作符以及应用 | 描述                                             |
| -------------- | ------------------------------------------------ |
| S\|T           | 返回一个新集合，包括在集合S和T中的所有元素，并集 |
| S-T            | 返回一个新集合，包括在集合S但不在T中的元素，差集 |
| S&T            | 返回一个新集合，包括同时在集合S和T中的元素，交集 |
| S^T            | 返回一个新集合，包括集合S和T中的非相同元素，补集 |
| S<=T或S<T      | 返回True/False，判断S和T的子集关系，比较         |
| S>=T或S>T      | 返回True/False，判断S和T的包含关系               |

 4个增强操作符

| 操作符以及应用 | 描述                                  |
| -------------- | ------------------------------------- |
| S\|=T          | 更新集合S，包括在集合S和T中的所有元素 |
| S-=T           | 更新集合S，包括在集合S但不在T中的元素 |
| S&=T           | 更新集合S，包括同时在集合S和T中的元素 |
| S^=T           | 更新集合S，包括集合S和T中的非相同元素 |

集合的处理方法

| 操作函数或方法 | 描述                                                  |
| -------------- | ----------------------------------------------------- |
| S.add(x)       | 如果x不在集合S中，将x增加到S                          |
| S.discard(x)   | 移除S中的元素x，如果x不在集合S中，不报错              |
| S.remove(x)    | 移除S中的元素x，如果x不在集合S中，产生KeyError异常    |
| S.clear()      | 移除S中的所有元素                                     |
| S.pop()        | 随机返回S的一个元素，更新S，若S为空，产生KeyError异常 |
| S.copy()       | 返回集合S的一个副本                                   |
| len(S)         | 返回集合S的元素个数                                   |
| x in S         | 判断S中元素x，x在集合S中，返回True，否则返回False     |
| x not in S     | 判断S中元素x，x不在集合S中，返回True，否则返回False   |
| set(x)         | 将其他类型的变量x转变为集合类型                       |

集合一个重要的应用场景就是数据去重

```python
>>> ls = ["p","p","y","y",123]
>>> s = set(ls)  # 利用了集合的无重复元素的特点
>>> s
{'p', 123, 'y'}
>>> ls = list(s)  # 将集合转换为列表
>>> ls
['p', 123, 'y']
```

序列类型的定义

序列是具有先后关系的一组元素，是一维元素向量，元素类型可以不同，元素间由序号引导，通过下标访问。序列是一个基类类型，一般不直接使用，而是使用其衍生类型，比如字**符串类型**，**元组类型**，**列表类型**。

序列类型通用操作符

| 操作符及应用     | 描述                                         |
| ---------------- | -------------------------------------------- |
| x in s           | 如果x是序列s的元素，返回True，否则返回False  |
| x not in s       | 如果x是序列s的元素，返回False，否则返回True  |
| s+t              | 连接两个序列s和t                             |
| s * n 或 n * s   | 将序列s复制n次                               |
| s[i]             | 索引，返回s中的第i个元素，i是序列的序号      |
| s[i:j]或s[i:j:k] | 切片，返回序列s中第i到j以k为步长的元素子序列 |

序列类型的通用函数和方法

| 函数和方法 | 描述                                     |
| ---------- | ---------------------------------------- |
| len(s)     | 返回序列s的长度                          |
| min(s)     | 返回序列s的最小元素，s中元素需要可以比较 |
| max(s)     | 返回序列s的最大元素，s中元素需要可以比较 |
| s.index(x) | 返回序列s中第一次出现x的位置             |
| s.count(x) | 返回序列s中出现x的总次数                 |

元组类型的定义

元组是序列类型的一中扩展，一旦创建就不能修改，使用小括号()或者tuple()创建，元素间用逗号,分隔，可以使用或者不使用小括号。因为元素不能修改，所以没有特殊的元素函数和方法。

列表的定义

列表是序列类型的一中扩展，十分常用，列表是一种序列类型，创建后可以随意修改。使用方括号[]或者list()创建，元素使用逗号分隔，列表中元素类型可以不同，无长度限制。

列表类型的操作函数和方法

 

| 函数或方法     | 描述                                   |
| -------------- | -------------------------------------- |
| ls[i] = x      | 替换列表ls中的第i个元素为x             |
| ls[i:j:k] = lt | 用列表lt替换ls切片后所对应元组子列表   |
| del ls[i]      | 删除列表ls中的第i个元素                |
| del ls[i:j:k]  | 删除列表ls中第i到第j以k为步长的元素    |
| ls+=lt         | 更新列表ls，将列表lt元素增加到列表ls中 |
| ls*=n          | 更新列表ls，其元素重复n次              |

列表类型操作函数和方法

| 函数或方法     | 描述                                  |
| -------------- | ------------------------------------- |
| ls.append(x)   | 在列表ls最后增加一个元素x             |
| ls.clear()     | 删除列表ls中所有元素                  |
| ls.copy()      | 生成一个新列表，赋值ls中所有元素      |
| ls.insert(i,x) | 在列表ls的第i位置增加元素x            |
| ls.pop(i)      | 将列表ls中第i位置元素取出丙删除该元素 |
| ls.remove(x)   | 将列表ls中出现的第一个元素x删除       |
| ls.reverse()   | 将列表ls中的元素反转                  |

154