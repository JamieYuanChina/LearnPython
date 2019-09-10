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

基本统计值计算

```python
# CalStatisticsV1.py


def getNum():  # 获取用户输入数据
    nums = []
    iNumber = input("请输入数字(回车退出)： ")
    while iNumber != "":
        nums.append(eval(iNumber))
        iNumber = input("请输入数字(回车退出)： ")
    return nums


def mean(numbers):  # 计算平均值
    s = 0.0
    for num in numbers:
        s = s + num
    return s/len(numbers)


def dev(numbers,mean):  # 计算方差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1), 0.5)


def median(numbers):  # 计算中位数
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med


n = getNum()
m = mean(n)
print("平均值：{}，方差：{:.2}，中位数：{}.".format(m, dev(n, m), median(n)))
```

字典类型

字典类型是映射的体现，键值对，键是数据索引的扩展，字典是键值对的集合，键值对之间无序，采用大括号{}和dict()创建，键值对使用冒号:表示。

生成空字典 de = {}； type(de)

集合类型也是有大括号表示，注意区分

字典类型操作函数和方法

| 函数或方法         | 描述                                        |
| ------------------ | ------------------------------------------- |
| del d[k]           | 删除字典d中键k对应的数据值                  |
| k in d             | 判断键k是否在字典d中，如果在返回True        |
| d.keys()           | 返回字典d中所有的键信息                     |
| d.values()         | 返回字典d中所有的值信息                     |
| d.items()          | 返回字典d中所有的键值对信息                 |
| d.get(k,<default>) | 键k存在，返回相应值，不存在返回默认值       |
| d.pop(k,<default>) | 键k存在，取出相应值，不存在返回默认值       |
| d.popitem()        | 随机从字典d中取出一个键值对，以元组形式返回 |
| d.clear            | 删除所有键值对                              |
| len(d)             | 返回字典d中元素的个数                       |

16、jieba库

jieba分词依靠中文词库。分为精确模式，全模式，搜索引擎模式三中。

jieba常用函数：

| 函数                       | 描述                                               |
| -------------------------- | -------------------------------------------------- |
| jieba.lcut(s)              | 精确模式返回一个列表类型的分词结果                 |
|                            | jieba.lcut("中国是一个伟大的国家")                 |
|                            | [‘中国’,‘是’,‘一个’,‘伟大’,‘的’,‘国家’]            |
| jieba.lcut(s,cut_all=True) | 全模式，返回一个列表类型的分词结果，存在冗余       |
|                            | jieba.lcut("中国是一个伟大的国家", cut_all=True)   |
|                            | [‘中国’,‘国是’,‘一个’,‘伟大’,‘的’,‘国家’]          |
| jieba.lcut_for_search(s)   | 搜索引擎模式，返回一个列表类型的分词结果，存在冗余 |
|                            | jieba.lcut_for_search("中华人民共和国是伟大的")    |
|                            | ['中华','华人','人民','共和','国','是','伟大','的] |
| jieba.add_word(w)          | 向分词词典增加新词w                                |
|                            | jieba.add_word("蟒蛇语言")                         |

jieba的安装

1，Python 2.x 下的安装
全自动安装 ：easy_install jieba 或者 pip install jieba 
半自动安装 ：先下载http://pypi.python.org/pypi/jieba/ ，解压后运行python setup.py install
手动安装 ：将jieba目录放置于当前目录或者site-packages目录 
通过import jieba 来引用

2，Python 3.x 下的安装
目前master分支是只支持Python2.x 的 
Python3.x 版本的分支也已经基本可用： https://github.com/fxsjy/jieba/tree/jieba3k 

git clone https://github.com/fxsjy/jieba.git
git checkout jieba3k
sudo python3 setup.py install

文本词频统计

```python
# CalHamletV1.py


def get_text():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamlet_txt = get_text()
words = hamlet_txt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

```

三国演义任务出场统计：

```python
# CalThreekingdomsV2.py

import jieba
txt = open("threekingdoms.txt", "r", encoding="utf-8").read()
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此"}
words = jieba.cut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
```

17、文件和数据格式化

文件是数据的抽象和集合，是存储在辅助存储器上的数据序列，是数据的一种存储形式，通常分为文本文件和二进制文件。

文件处理步骤：打开-操作-关闭

读文件：
a.read(size)
a.readline(size)
a.readlines(hint)
写文件：
a.write(s)
a.writelines(lines)
a.seek(offset)

文件的打开

<变量名> = open(<文件名>, <打开模式>)

文件句柄     文件路径和名称   文本or二进制，读or写

在windows中使用反斜杠\分隔路径，但是在Python中这个反斜杠表示转义，所以通常使用斜杠替代，或者使用两个反斜杠进行转义。

例如 ： D:\PYE\f.txt  在python中可以"D:/PYE/f.txt"或者  "D:\ \PYE\ \f.txt" 或者使用相对路径"./PYE/f.txt"

打开模式：

| 文件打开的模式 | 描述                                                      |
| -------------- | --------------------------------------------------------- |
| "r"            | 只读模式，默认值，入股欧文件不存在，返回FileNotFouneError |
| "w"            | 覆盖写模式，文件不存在则创建，存在则完全覆盖              |
| "x"            | 创建写模式，文件不存在则创建，存在则返回FileExistsError   |
| "a"            | 追加写模式，文件不存在则创建，存在则在文件最后追加内容    |
| "b"            | 二进制文件模式                                            |
| "t"            | 文本文件模式，默认值                                      |
| ”+“            | 与r/w/x/a一同使用，在原功能基础上增加同时读写功能         |

f = open("f.txt")  -文本形式，只读模式，默认

f = open("f.txt", "rt") -文本形式，只读

f = open("f.txt", "w")  - 文本形式，覆盖写

f = open("f.txt", "a+") -文本形式，追加写模式+读文件

文件关闭：<变量名>.close()

```
# 文本形式打开文件
tf = open("f.txt", "rt")
print(tf.readline())
tf.close()
```

文件的读取：

| 操作方法                 | 描述                                                         |
| ------------------------ | ------------------------------------------------------------ |
| < f >.read(size = -1)    | 读入全部内容，如果给出参数，读入前size长度                   |
| < f >.readline()         | 读入一行内容，如果给出参数，读入改行前size长度               |
| < f >.readlines(hint=-1) | 读入文件所有行，以每行为元素形成列表，如果给出参数，读入前hint行 |

文件的全文本操作

```python
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read()
# 对全文txt进行处理
fo.close()
```

```python
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
txt = fo.read(2)
while txt != "":
    # 对txt进行处理
    txt = fo.read(2)
fo.close()
```

文件的逐行处理操作

```python
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
for line in fo.readlines():  # 一次读入，逐行处理
    print(line)
fo.close()
```
```python
fname = input("请输入要打开的文件名称：")
fo = open(fname,"r")
for line in fo:  # 分行读入，逐行处理
    print(line)
fo.close()
```

数据的写入：


| 操作方法               | 描述                                           |
| ---------------------- | ---------------------------------------------- |
| < f >.write(s)         | 向文件写入一个字符串或者字节流                 |
| < f >.readlines(lines) | 将一个元素全为字符串的列表写入文件             |
| < f >.seek(offset)     | 改变当前文件操作指针的位置，                   |
|                        | offset含义：0-文件开头；1-当前位置；2-文件结尾 |

```python
fo = open("output.txt","w+")
ls = ["中国", “法国”, “美国”]
fo.writelines(ls)
fo.seek(0)  # 把文件指针设置到文件开头
for line in fo:
    print(line)
fo.close()
```

自动轨迹绘制

```python
#AutoTraceDraw.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800, 600,0,0)
t.pencolor("red")
t.pensize(5)
# 数据读取
datals = []
f = open("data.txt")
for line in f:
    line = line.replace("\n","")
    detals.append(list(map(eval, line.split(","))))
f.close()
# 自动绘制
for i in range(len(detals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][2]
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
 
```
data.txt
```
300,0,144,1,0,0
300,0,144,0,1,0
300,0,144,0,0,1
300,0,144,1,1,0
300,0,108,0,1,1
184,0,72,1,0,1
184,0,72,0,0,0
184,0,72,0,0,0
184,0,72,0,0,0
184,1,72,1,0,1
184,1,72,0,0,0
184,1,72,0,0,0
184,1,72,0,0,0
184,1,72,0,0,0
184,1,72,0,0,0
```

数据组织的维度

一维数据有对等关系的有序或无序数据构成，采用线性方式组织，对应表、数组、集合等概念。
二维数据是由多个一维数据构成，是一维数据的组合形式，
多维数据是由一维或者二维数据在新维度上的扩展形成。
高位数据仅利用最基本的二元关系展示数据间的复杂结构。
一维数据的表示，如果数据间有序，使用列表类型，for循环可以遍历数据，进而对数据处理。
一维数据如果无序，可以使用集合表示，同样使用for循环遍历。
一维数据的存储，通常采用空格，逗号，$符号等特殊字符间隔，不换行。缺点是数据中不能有间隔采用的字符。

```python
#一维数据的读入处理
txt = open(fname).read()
ls = txt.split()  # 分割符号可以使用"," "$"等
f.close()
```

```python
# 一维数据的写入处理
ls = ["中国","美国", "日本"]
f = open(fname,"w")
f.write(" ".join(ls))  # 采用空格分隔方式将数据写入文件
f.close()
```

二维数据

二维数据可以使用列表进行表示，使用两层for循环进行遍历每一个元素。
外层列表中每个元素可以对应一行或者一列。
一二维数据的python表示：数据维度是数据的组织形式
一维数据：列表和集合类型
    [0.1396, 3.1659]  数据间有序
    {0.1396, 3.1659} 数据间无序
二维数据：列表类型
    [ [0.1396,  3.1659], [0.1396,  3.1659] ]
二维数据的存储，通用.csv格式，逗号分隔的多行文本格式，无空行，空数据也需要使用逗号占位。
一般搜索习惯，ls [ row ] [ column ]，采用先行后列方式。外层列表每个元素是一行。
二维数据的读入处理

```python
# 从csv格式文件读入数据
fo = open(fname)
ls = []
for line in fo:
    line = line.replace("\n","")
    ls.append(line.split(","))
fo.close()
```

```python
# 将数据写入csv格式文件
ls = [[],[],[]]  # 二维列表
fo = open(fname, "w")
for item in ls:
    f.write(",".join(item) + "\n")
fo.close()
```

```python
# 二维数据的逐一处理，采用二层循环
ls = [[1, 2],[3, 4],[5, 6]]  # 二维列表
for row in ls:
    forcolumn in row:
        print(column)
```

词云展示库wordcloud

```
pip install wordcloud
```

wordcloud库把词云当做一个WordCloud对象

wordcloud.WordCloud()代表一个文本对应的词云，可以根据文本中词语出现的频率等参数绘制词云，绘制词云的形状、尺寸和颜色都可以设定。

w = wordcloud.WordCloud()

| 方法                | 描述                               |
| ------------------- | ---------------------------------- |
| w.generate(txt)     | 向WordCloud对象w中加载文本txt      |
| w.to_file(filename) | 将词云输出为图像文件，png或jpg格式 |

分三个步骤：配置对象参数；加载词云文本；输出词云文件。

```python
import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud by Python")
c.to_file("pywordcloud.png")
```

生成词云图片，默认宽度400像素，高度200像素。

词云库处理过程：

1分隔：以空格分隔单词
2统计：单词出现次数并过滤
3字体：根据统计配置字号
4布局：颜色环境尺寸

c = wordcloud.WordCloud(<参数>)

| 参数             | 描述                                              |
| ---------------- | ------------------------------------------------- |
| width            | 指定词云对象生成图片的宽度，默认400像素           |
| height           | 指定词云对象生成图片的高度，默认200像素           |
| min_font_size    | 指定词云中字体的最小字号，默认4号                 |
| max_font_size    | 指定次云中字体的最大字号，根据高度自动调节        |
| font_setp        | 指定词云中字体号的步进间隔，默认为1               |
| font_path        | 指定字体文件的路径，默认None                      |
|                  | w=wordcloud.WordCloud(font_path="msyh.ttc")       |
| max_words        | 指定词云显示的最大单词数量，默认200               |
| stop_words       | 指定词云的排除词列表，即不显示的单词列表          |
| mask             | 指定词云形状，默认Wie长方形，需要引用imread()函数 |
| background_color | 指定词云图片背景颜色，默认为黑色                  |

英文词云案例

```Python
import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud(background_color = "white")
w.generate(txt)
w.to_file("pywcloud.png")
```

中文词云案例：

```python
import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一中交互体系，\
它按照戈丁规则组织计算机指令，使计算机能够自动进行跟中运算处理。"
w = wordcloud.WordCloud(width = 1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.cut(txt)))
w.to_file("pywcloud.png")
```

政府工作报告词云见案例GovRptWordCloudv1.py

竞技分析案例见MatchAnalysis.py

更大的python世界

python社区： https://pypi.org 在这里可以搜索任何主题的python第三方库。

pypi:python package index

例如开发区块链相关程序，可以在pypi.org 搜索blockchain

pip安装工具

常用pip命令

pip install <第三方库名>     安装
pip install -U <第三方库名>  更新
pip uninstall <第三方库名>  卸载
pip download <第三方库名>  下载
pip show <第三方库>  显示
pip search <关键词>  搜索
pip list  列出本机安装的第三方库
使用pip安装可以解决99%的库问题。

继承安装方法

Anaconda  https://www.continuum.io

支持近800个第三方库，包含多个主流工具，适合数据计算领域开发。

文件安装方法

http://www.lfd.uci.edu/~gohlke/pythonlibs    

OS库

os库提供通用的，基本的操作系统交互功能，有几百个函数。
os.path子库以path为入口，用于曹邹和处理文件路径
import os.path
import os.path as op

| 函数                       | 描述                                                |
| -------------------------- | --------------------------------------------------- |
| os.path.abspath(path)      | 返回path在当前系统中的绝对路径                      |
| os.path.normpath(path)     | 归一化path的表示形式，统一用 \ \ 分隔路径           |
| os.path,relpath(path)      | 返回当前程序与文件之间的相对路径(relative path)     |
| os.path.dirname(path)      | 返回path中的目录名称                                |
| os.path.basename(path)     | 返回paht中最后的文件名                              |
| os.path.join(path, *paths) | 组合path与paths，返回一个路径字符串                 |
| os.path.exists(path)       | 判断path对应文件或者目录是否存在，返回True或者False |
| os.path.isfile(path)       | 是否是文件                                          |
| os.path.isdir(path)        | 是否是目录                                          |
| os.path.getatime(path)     | 目录或文件上一次访问时间                            |
| os.path.getmtime(path)     | 修改时间                                            |
| os.path.getctime(path)     | 创建时间                                            |
| os.path.getsize(path)      | 返回对应文件的大小，一字节为单位                    |

进程管理

os.system(command)

```
import os
os.system("c:\\windows\\System32\\calc.exe")
os.system("c:\\windows\\System32\\mspaint.exe d:\\grwordcloud.png")
```

环境参数

| 函数           | 描述                                        |
| -------------- | ------------------------------------------- |
| os.chdir(path) | 修改当前程序操作的路径                      |
| os.getcwd()    | 返回程序当前路径                            |
| os.getlogin()  | 获得当前系统登录用户名                      |
| os.cpu_count() | 获得当前系统cpu数量                         |
| os.urandom(n)  | 获得n个字节长度的随机字符串，通常用于加解密 |

第三方库自动安装

常用第三方库列表

| 库名           | 用户                         | pip安装指令                |
| -------------- | ---------------------------- | -------------------------- |
| NumPy          | N维数据表示和运算            | pip install numpy          |
| Matplotlib     | 二维数据可视化               | pip install matplotlib     |
| PIL            | 图像处理                     | pip install pillow         |
| Scikit-Learn   | 机器学习和数据挖掘           | pip install sklearn        |
| Request        | HTTP协议访问以及网络爬虫     | pip install requests       |
| Jieba          | 中文分词                     | pip install jieba          |
| Beautiful Soup | HTML和XML解析器              | pip install beautifulsoup4 |
| Wheel          | python第三方文件打包工具     | pip install wheel          |
| PyInstall      | 打包python源文件为可执行文件 | pip install pyinstaller    |
| Django         | python最流行的web开发框架    | pip install django         |
| Flask          | 轻量级web开发框架            | pip install flask          |
| WeRoBot        | 微信机器人开发框架           | pip install werobot        |
| SymPy          | 数学符号计算工具             | pip install sympy          |
| Pandas         | 高效数据分析和计算           | pip install pandas         |
| Networdx       | 复杂网络和图结构的建模分析   | pip install networkx       |
| PyQt           | 基于Qt的专业级GUI开发框架    | pip install pyqt5          |
| PyOpenGl       | 多平台OpenGL开发接口         | pip install pyopengl       |
| PyPDF2         | PDF文件内容提取以及处理      | pip install pypdf2         |
| docopt         | Python命令行解析             | pip install docopt         |
| PyGame         | 简单小游戏开发框架           | pip install pygame         |

```python
# BatchInstall.py
import os
libs = {"numpy", "matplotlib", "pillow", "sklearn", "requests",\
        "jieba", "beautifulsoup4", "wheel", "networkx", "sympy",\
        "pyinstaller", "django", "flask", "werobot", "pyqt5",\
        "pandas", "pyopengl", "pypdf2", "docopt", "pygame",\
        "scipy", "mxnet", "mayavi", "nltk", "python-docx",\
        "scikit_learn", "tensorflow", "seaborn"}
try:
    for lib in libs:
        os.system("pip3 install " + lib)
        print("Successful")
except:
    print("Failed somehow")

```

 从数据处理到人工智能

数据表示->数据清洗->数据统计->数据可视化->数据挖掘->人工智能

python库之数据分析

Numpy:表达N维数组的最基础库，使用C语言实现，Python接口，计算速度优异，是Python数据分析以及科学计算的基础库，支撑Pandas等库，提供直接的矩阵运算，广播函数，线性代数等功能。Numpy可以直接对数据进行平方等操作，不需要对数组中每一个数据进行分布操作。减少了for循环的使用。

pandas库是python数据分析高层次应用库提供了简单易用的数据结构和数据分析工具，理解数据类型和索引的关系，操作索引即操作数据，是Python最主要的数据分析功能库，基于Numpy开发。Series = 索引 + 一维数据；DataFrame = 行列索引 + 二维数据

SciPy：数学，科学和工程计算功能库，提供了一批数学而算法以及工程数据运算功能，类似matlab，可用于如傅里叶变换，信号处理等应用，是Python最主要的科学计算功能库，基于NumPy开发。

Matplotlib:高质量的二位数据可视化功能库，提供超过100种数据可视化展示效果，通过matplotlib.pyplot字库调用各个可视化效果，是最主要的数据可视化功能库，基于Numpy开发。

Seaborn:统计类数据可视化功能库，提供了一批高层次的统计类数据可视化展示效果，主要展示数据间分布，分类和线性关系等内容，基于Matplotlib开发，支持Numpy和Pandas

Mayavi:三维可续数据可视化功能库，提供了一批简单易用的3D科学计算数据可视化展示效果，目前版本是Mayavi2，三维可视化最主要的第三方库，支持Numpy，TVTK，Traits，Envisage等第三方库

pyPDF2：用来处理pdf文件的工具集，提供了一批处理PDF文件的计算功能，支持获取信息，分隔/整合文件，加密解密等等。 完全使用Python语言实现，不需要额外依赖，功能稳定。

```python
from PyPDF2 import PdfFileReader, PdfFileMerger
merger = PdfFileMerger()
input1 = open("document1.pdf", "rb")
input2 = open("document2.pdf", "rb")
merger.append(fileobj = input1, pages = (0,3))
merger.merge(position = 2, fileobj = input2, page = (0, 1))
output = open("document-output.pdf", "wb")
merger.write(oupput)
```

NLTK:自然语言文本处理第三方库，提供了一批简单易用的自然语言文本处理功能，支持语言文本分类，标记，语法句法予以分析等，是最优秀的Python自然语言处理库

```python
from nltk.corpus import treebank
t = treebank.parsed_sents("wsj_0001.mrg")[0]
t.draw()
```

Python-docx:创建或更新Microsoft Word 文件的第三方库，提供创建或更新.doc,docx等文件计算功能，增加并且配置段落，图片，表格，文字等，功能全面

```python
from docx import Document
document = Document()
document.add_heading("Document Title", 0)
p = document.add_paragraph("A plain paragraph having some")
document.add_page_break()
document.save("dome.docx")
```

Scikit_learn:机器学习方法工具，提供一批统一化的机器学习方法功能接口，提供聚类，分类，回归，强化学习等计算功能，是机器学习最基本最优秀的Python第三方库。

TensorFlow:AlphaGo背后的机器学习计算框架，谷歌公司推动的开源机器学习框架，将数据留图作为基础，图节点代表运算，边代表张量，应用机器学习方法的一中方式，支撑谷歌人工智能应用。

```python
import tensorflow as tf
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
res = sess.run(result)
print("result:", res)
```

MXNet:基于森警网络的深度学习计算框架，提供可扩展的神经网络及深度学习计算功能，可用于自动驾驶，机器翻译，语音识别等众多领域，是Python最重要的深度学习计算框架。

霍兰德分析雷达图

代码见 HollandRadarDraw.py

linux下Matplotlib库中文字体支持方法：

获取matplotlibrc文件所在路径。

```python
import matplotlib
print(matplotlib.matplotlib_fname())
exit()
```

查看可用字体

```python
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)
print(mat_fonts)
output = subprocess.check_output('fc-list :lang=zh -f "%{family}\n"', shell=True)
print('*' * 10, '系统可用的中文字体', '*' * 10)
print(output)
zh_fonts = set(f.split(',', 1)[0] for f in output.decode().split('\n'))
available = mat_fonts & zh_fonts
print('*' * 10, '可用的字体', '*' * 10)
for f in available:
    print(f)

```

233