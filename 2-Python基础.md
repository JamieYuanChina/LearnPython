# LearnPython
这是一个学习Python的项目

## 第二章 Python基础

1、Python代码默认一行只能写一条语句，语句结束没有显示的结束符，这一点和C语言不同。

HelloPython.py

```python
print("hello python")
```

2、缩进检查非常严格，多一个空格也会报错。代码应该定格写。

3、Python2.x默认不支持中文，Python3支持。

4、Python2.7为最后一个2.x版本。

5、官方解释器为cpython

6、交互式运行Python，适合小程序，无法保存代码，exit()或者ctrl+d退出。

7、IPython比官方的shell好用很多，支持自动补全，代码缩进，bash命令等。

8、Python的IDE工具PyCharm，可以自动补全，代码缩进，断点调试等等。

9、PyCharm配置文件都保存在了用户目录的.PyCharmxxx.x目录下，删除该目录可以恢复PyCharm。

10、文件名称建议全部小写，数字，下划线，并且数字不能开头。

11、Python的注释分为单行和多行，单行注释以"#"号开头空格隔开，多行注释为一对三个连续的引号

```python
# 这是一个单行注释
“”“
这是一个多行注释 
”“”
```

12、代码规范，PEP 8
谷歌的中文版Python代码规范地址：
http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules

13、算数运算符 

| 运算符 | 描述   | 示例          |
| :----- | ------ | ------------- |
| +      | 加     | 10 + 20 = 30  |
| -      | 减     | 10 - 20 = -10 |
| *      | 乘     | 10 * 20 = 200 |
| /      | 除     | 10 / 20 = 0.5 |
| //     | 取整除 | 9 // 2  = 4   |
| %      | 取余数 | 9 % 2 = 1     |
| **     | 幂     | 2 ** 3 = 8    |

*号可以用于字符串，用来显示多个字符串，相当于字符串的拼接。

```python
“对不起” * 100
```

14、变量的定义

```python
qq_number = "12345678"
print(qq_number)
```

在Python中，定义变量不需要指定数据类型，在运行的时候，解释器会根据等号右侧的数据自动推导出变量中保存数据的准确类型。

常用的类型有：数字型------bool(布尔);int(整形);float(浮点);complex(复数)

非数字型：str(字符串);

在ipython中使用type()函数查看变量的类型。

在Python3中，数字类型不区分int和long，全部统一为int，即使计算诸如2**1000这样的大数据。

数字类型的变量之间可以直接计算，boot的True为1，False为0；

字符串类型的变量可以使用+号进行拼接。

```python
first_name = "三"
last_name = "张"
(last_name + first_name) * 10 
```

数字型变量和字符串之间除了"+"和"*"之外，不能进行其他计算。

15、变量的输入，使用input()函数，输入类型全部都是字符串类型。

```python
passwd = input("请输入密码")
```

可以使用int(x)或者float(x)把字符串转换为相应类型。

```python
type(input("12.3"))
```

16、字符串的格式化输出

print("格式化字符串" % 变量1)

```python
name = "小明"
age = 18
height = 173.5

print("我的名字叫%s，年龄%d岁，身高%.1f厘米" % (name, age, height))
```

17、标识符和关键字

标识符只能由字母，数字，下划线组成，数字不能在开头。

```python
import keyword
print(keyword.kwlist)
```

18、变量的命名规则

Python中标识符是区分大小写的，定义变量时在=的左右边各保留一个空格；

变量名由多个单词组成，每个单词小写，单词之间使用下滑下连接，如：first_name

19、if语句

缩进建议使用四个空格。Tab和空格不要混用。if语句和后面的缩进看成一个完整代码块。

```python
if age >= 18:
    print("happy")
    print("very happy")
else:
    print(" no happy ")
    print("out")
print("结束了")
```

20、逻辑运算

Python中的逻辑运算符有：与and或or非not，逻辑判断可以使用if ，elif，else。

```python
# 导入随机工具包
import random
# 从控制台输入信息
player = int(input("请输入您要出的拳 石头(1)/剪刀 (2) /布(3):"))
# 电脑随机出拳
computer = random.randint(1, 3)
print("玩家选择的拳头是 %d - 电脑出的拳头是 %d" % (player, computer))
# 比较胜负
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("电脑弱爆了！")
elif player == computer:
    print("心有灵犀啊！")
else:
    print("电脑胜利了！")
```

21、循环

程序中的三大流程：顺序，分支，循环

```python
count = 0  # type: int
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        count += i
    i += 1
print("0~100内偶数的和为:%d" % count)
```

循环语句支持break和continue语句。需要注意的是continue时不会执行自增语句，多以在continue之前需要增加自增语句。

print("*", end="")，这样不会换行。end=“---”也是可以的。

```python
row = 1
print("表1\n九九乘法表")
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    print("")  # 添加换行
    row += 1
```

22、函数

定义方法：

```python
def 函数名():
    封装的代码
```

​    调用方法：

```python
import 包名(文件名)
包名.函数名()
```

23、调试

在PyCharm中F8为单步越过，F7为单步进入。

24、函数的注释

在函数名上方需要预留两个空行。函数说明在函数名下方，使用""" 函数的说明"""

 25、函数的参数

```python
def my_add(num1, num2):
    """两个数字求和"""
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))
    return result


res = my_add(12, 23)
```

函数定义时的参数叫形参，调用函数的参数叫实参。

```python
def print_line(char, times):
    """打印一行分隔符

    :param char: 分隔符使用的字符
    :param times: 分隔符打印的次数
    """
    print(char * times)


print_line("^8", 60)
```

在函数调用处，使用**Ctrl+Q**可以查看函数帮助

26、模块

模块是Python程序架构中的一个核心概念

模块就好比工具包，想要使用这个工具包中的工具，比如导入import这个模块

每个一py结尾的python文件都是一个模块

在模块中定义的全局变量和函数都是模块能够提供给外接直接使用的工具

使用import导入过的文件，会把文件编译为pyc文件，以提高运行速度。

27、高级变量

非数字变量：列表，元组，字典，字符串

公共方法，变量高级

在Python中，所有非数字变量都有一下特点

都是一个序列(sequence)，也可以理解为容器

取值[]

遍历 for in

计算长度，大小，最值，比较，删除

链接+和重复*

切片

28、列表

List**列表**是Python中使用最频繁的数据类型，在其他语言中通常叫做**数组**

```python
name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[1])
```

29、列表的常用操作

```python
# 定义列表
name_list = ["zhangsan", "lisi", "wangwu"]
num_list = [1, 2, 8, 4]
# 取值和取索引
print(name_list[1])
print(name_list.index("lisi"))
# 修改列表数据
name_list[1] = "李四"
# 增加列表数据
name_list.append("赵六")  # 列表末尾追加数据
name_list.insert(1, "陈二麻子")  # 列表指定位置插入数据
temp_list = ["孙悟空", "二师兄", "沙师弟"]  # 定义临时列表
name_list.extend(temp_list)  # 扩展列表
# 列表数据统计
list_len = len(name_list)
print("列表中有%d个元素" % list_len)  # 获取列表长度
count = name_list.count("zhangsan")  # 统计张三出现的次数
print("zhangsan出现了%d次" % count)
# 列表的排序
# 升序
name_list.sort()
num_list.sort()
# 降序排列
name_list.sort(reverse=True)
num_list.sort(reverse=True)
# 逆序，翻转
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)
# 列表删除数据
name_list.remove("wangwu")  # 删除指定数据，如果有多个，删除第一个
name_list.pop()  # pop默认删除最后一个数据
name_list.pop(1)  # 根据指定的索引删除数据
name_list.clear()  # 清空列表
# 打印列表
print(name_list)
# 删除变量
del name_list
```

30、关键字，函数，方法

Python中有33个关键字，在ipython中import keyword，打印输出，print(keyword.kwlist)
关键字后面不需要使用括号。
函数封装了独立的功能，可以直接调用，必须送括号。必须死记硬背
方法需要通过对象来调用，不需要死记硬背。

31、列表的循环遍历

```python
# 定义列表
name_list = ["zhangsan", "lisi", "wangwu"]
# 使用迭代遍历列表
for my_name in name_list:
    print("我的名字是：%s" % my_name)
```

列表虽然也能存储不同数据类型的数据，但是通常都是存储相同类型的数据，然后进行迭代遍历操作。

32、元组

Tuple元组与列表类似，不同之处在于元组中的元素不能修改。元组使用小括号()定义。元组通常存储不同数据类型的变量，有特定的应用场景。
在Python中可以使用for循环遍历所有非数字性变量：列表，元组，字典，字符串。
但是在元组数据中使用for循环遍历并不常见，除非能够确认元组中的数据类型。
元组的应用场景：
1.函数的参数和返回值
2.格式字符串，在格式化字符串时，小括号中就是一个元组
3.让列表不可以修改，保护数据安全

```python
info_tuple = ("小明", 21, 1.75)
# 格式化字符串后面的“()” 本质上就是元组
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
# 拼接字符串
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
# 元组转换为列表
info_list = list(info_tuple)
# 列表转换为元组
info_tuple2 = tuple(info_list)
```

33、字典

字典可以存储多个数据，和列表的区别，列表通常存储有序的对象集合。字典通常是存储无序的对象集合，字典用{}定义，字典使用键值对存储数据，键值对之间使用，分隔。

Key是索引，value是数据，两者之间使用:分隔，键必须是唯一的。值可以是任何数据，但是键只能使用字符串，数字或者元组。

字典变量通常是用来描述一个物体的相关信息。

```python
# 字典是一个无序的数据集合，使用print函数输出字典时，通常输出的顺序和定义顺序不一致
xiaoming_dict = {"name": "小明",
                 "age": 18,
                 "gender": True,
                 "height": 1.75}
# 字典的取值
print(xiaoming_dict["name"])
# 字典的修改和增加
xiaoming_dict["weight"] = 75  # 字典中没有该项，就是新增键值对
xiaoming_dict["age"] = 20  # 字典中已经有了该项，那么就是修改键值对。
# 删除键值对
xiaoming_dict.pop("gender")
# 统计键值对数量
print(len(xiaoming_dict))
# 定义临时字典
temp_dict = {"gender": True,
             "age": 22}
# 合并字典，如果合并的字典中有原字典中的键值，则更新该键值对。
xiaoming_dict.update(temp_dict)
# 情况字典
xiaoming_dict.clear()
print(xiaoming_dict)
# 字典的遍历
xiaojing_dict = {"name": "小静",
                 "qq": "33238771",
                 "phone": "139"}
for k in xiaojing_dict:
    print("%s - %s" % (k, xiaojing_dict[k]))
```

可以将多个字典放在一个列表中，在进行遍历，在循环内部，针对每一个字典进行相同的处理。

```python
card_list =[
    {"name": "张三",
     "qq": "12345",
     "phone": "110"},
    {"name": "李四",
     "qq": "67890",
     "phone": "120"}
]
for card_info in card_list:
    print(card_info)
```

34、字符串

在Python中，字符串的定义可以使用单引号也可以使用双引号，因为在大多数语言中都是使用双引号，所以建议平时使用双引号定义字符串，只有当引号需要嵌套时，外部使用单引号，内部使用双引号。

```python
str1 = "hello python"
str2 = '我的外号是"大西瓜"'
print(str2)
print(str1[6])
for char in str2:
    print(char)
```

288