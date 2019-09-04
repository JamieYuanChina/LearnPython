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

| and    | as   | assert | break  | class | continue | def    | elif     | else | except | finally |
| ------ | ---- | ------ | ------ | ----- | -------- | ------ | -------- | ---- | ------ | ------- |
| for    | from | if     | import | in    | is       | lambda | not      | or   | pass   | raise   |
| return | try  | while  | with   | yield | del      | global | nonlocal | True | False  | None    |

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

字符串变量内置了足够多的方法，可以很方便的处理字符串变量。

```python
hello_str = "hello world"
# 判断是否以指定字符串开始
print(hello_str.startswith("hello"))
# 判断是否一指定字符串结束
print(hello_str.endswith("world"))
# 查找字符串
# index方法同样可以查找字符串，但是如果找不大会报错。
print(hello_str.find("llo"))
# 替换字符串
# replace方法执行后会返回一个新的字符串，不会修改原来自的字符串。
print(hello_str.replace("world", "python"))
print(hello_str)

poem = ["登鹳雀楼\r\n",  # 网络爬取的数据很有可能有空白字符
        "王之涣",
        "白日依山尽\t\n",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]
for poem_str in poem:
    # print("|%s|" % poem_str.strip().center(10,"　"))  # 10个字符，填充中文空格
    print("|%s|" % poem_str.strip().ljust(10,"　"))  # strip方法可以去除空白字符
    # print("|%s|" % poem_str.rjust(10,"　"))  # 10

```

35、字符串的拼接和拆分

```python
# 假设以下内容是从网络抓取得到的
# 要求把字符串中的空白字符去掉，再使用空格作为分隔符，拼接成一个整齐的字符串

poem_str = "登鹳雀楼\t 王之涣 \t 白日依山尽\t\n 黄河入海流 \t 欲穷千里目\t 更上一层楼"

print(poem_str)

# 拆分字符串
poem_list = poem_str.split()
print(poem_list)
# 合并字符串
resule = " ".join(poem_list)
print(resule)
```

36、字符串的切片

切片方法适用于字符串，列表，元组，切片使用索引值来限定范围。

字符串[开始索引:结束索引:步长]

正向索引从0开始，倒序从-1开始，想要切到结尾，结束字符留空即可。

```python
num_str = "0123456789"
print(num_str[2:6])
print(num_str[::2])
print(num_str[-1])  # 取最后一个字符
print(num_str[::-1])  # 逆序输出
```

37、公共方法

len(item)
del(item)
max(item)
min(item)
cmp(item1,item2)

```python
a = [1, 3, 5, 7, 9]
del a[1]
print(a)
# del(a)
t_srt = "qweqweqwesdsldkfj"
print(max(t_srt))
print(min(t_srt))
print(max(a))
print("1" > "2")

```

字符串，列表，元组都能够切片

```python
print([0, 1, 2, 3, 4, 5][::-1])
```

38、运算符

| 运算符       | python表达式          | 结果                       | 描述           | 支持的数据类型           |
| ------------ | --------------------- | -------------------------- | -------------- | ------------------------ |
| +            | [1, 2] + [3, 4]       | [1, 2, 3, 4]               | 合并           | 字符串、列表、元组       |
| *            | ['Hi!']*4             | ['Hi!';'Hi!';'Hi!';'Hi!';] | 重复           | 字符串、列表、元组       |
| in           | 3 in (1, 2, 3)        | True                       | 元素是否存在   | 字符串、列表、元组、字典 |
| not in       | 4 not in (1, 2, 3)    | True                       | 元素是否不存在 | 字符串、列表、元组、字典 |
| > >= == < <= | (1, 2, 3) < (2, 2, 3) | True                       | 元素比较       | 字符串、列表、元组       |

39 、完整的for循环语法

for 变量 in 集合：
    循环提代码
else:
    没有通过break退出循环，循环结束后，会执行的代码。

应用场景：循环遍历，如果存在，提示退出循环，如果不存在，希望得到一个统一的提示。

```Python
students = [
    {"name": "阿土"},
    {"name": "小美"}
]
find_name = "小美"
for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了 %s" % find_name)
        # 如果找到,应该退出循环
        break
else:
    print("抱歉，没有找到 %s" % find_name)
print("循环结束")

```

40、综合应用--名片管理系统

cards_main.py

```python
#! /usr/bin/python3
# 第一行增加shebang符号和python3命令的完整路径
import cards_tools

# 无限循环，由用户决定什么时候退出
while True:

    # TODO(小明) 显示功能菜单，这里使用TODO可以创建一个待完成工作列表
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的功能是 %s" % action_str)

    # 1,2,3针对名片操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        if action_str == "2":
            cards_tools.show_all()
        # 查询名片
        if action_str == "3":
            cards_tools.search_card()
    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【名片管理系统】")

        break
        # 如果在开发过程中不希望立刻编写分支内部代码
        # 可以使用pass关键字，表示一个占位符，能够保证代码的结构正确。
        # 程序运行时，pass关键字不会执行任何操作。
        # pass
    # 其他内容，输入错误，提示用户
    else:
        print("您输入错误，请重新输入:")

```

cards_tools.py

```python
# 定义全局列表，保存数据，列表中保存多个用户信息字典
card_list = [{"name": "小明",
              "phone": "120",
              "qq": "123",
              "email": "123@qq.com"}]


def show_menu():
    """ 显示菜单 """
    print("*" * 50)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*" * 50)

    
def new_card():
    """"新增名片"""
    print("-" * 50)
    print("新增名片")
    # 提示用户输入信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ:")
    email_str = input("请输入邮件地址：")
    # 根据用户信息建立名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 将名片字典添加到列表中
    card_list.append(card_dict)
    # 提示用户添加成功
    print("添加 %s 的名片成功" % name_str)

    
def show_all():
    """ 显示全部"""
    print("-" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list)==0:
        print("当前没有任何名片记录，请使用新增功能添加")
        return
    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")
    # 输出一个空行，相当于换行
    print("")
    # 打印分隔符
    print("=" * 50)
    # 遍历名片列表，一次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

        
def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")

    # 遍历名片列表，查询要搜索的姓名，如果没有找到，提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("*" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # 针对找到名片记录记性修改和删除操作
            deal_card(card_dict)
            break
    else:
        print("抱歉没有找到 %s " % find_name)

        
def deal_card(find_dict):
    """

    :param find_dict: 找到的字典
    """
    # print(find_dict)
    action_str = input("请输入要执行的操作"
                       " 【1】 修改 【2】 删除 【0】 返回 :")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "QQ：")
        find_dict["email"] = input_card_info(find_dict["email"], "邮箱：")
        print("修改名片成功！")
    elif action_str == "2":

        card_list.remove(find_dict)

        print("删除名片成功！")

        
def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典中的原有值
    :param tip_message: 输入的提示文字
    :return: 输入的信息，如果没有输入，返回原有值
    """
    # 提示用户输入内容
    result_str = input(tip_message)
    # 针对用户输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str)>0:
        return result_str
    # 如果用户没有输入内容，返回字典原有值
    else:
        return dict_value
```

41、变量的引用

- 在Python中，函数的参数传递以及返回值都是靠引用传递的；
- 在Python中，变量和数据是分开存储的
- 数据保存在内存中的一个位置
- 变量中保存这数据在内存中的地址
- 变量中记录数据的地址，就叫做引用
- 使用id()函数可以查看变量中保存数据所在的内存地址。

注意，如果变量已经定义，当给一个变量赋值的时候，本质上是修改了数据的引用

变量不在对之前的数据引用

变量改为对新赋值的数据引用

42、可变和不可变类型

不可变类型，内存中的数据不允许被修改：

- ​    数字类型 int， bool，float，complex，long
- ​    字符串 str
- ​    元组 tuple

可变类型，内存中的数据可以被修改：

- ​    列表 list
- ​    字典 dict

字典的key 只能使用不可变类型的数据

可变类型的数据变化，是通过方法来实现的

在Python中，设置字典的键值对时，会首先对key进行hash，已决定如何在内存中保存字典的数据，以方便后续对字典的操作，增删改查

而hash函数只接收不可变类型的变量，所以键值对key比如为不可变类型，键值对的value可以是任何类型数据。

43、局部变量和全局变量。

函数内部定义并使用的变量为局部变量，在所有函数外部定义的变量可以被所有函数使用，为全局变量。在函数执行结束后，函数内部的局部变量会被系统回收，不同的函数可以定义相同的名字，通常用来临时保存函数内部需要使用的数据。

在函数执行时，需处理变量时会首先查找函数内部是否存在指定名称的局部变量，如果有直接使用。

如果没有，查找函数外部是否存在指定名称的全局变量，如果有直接使用，如果还没有，报错。

函数不能直接修改全局变量的引用，但是所有函数都可以在函数内部引用全局变量，如果一定要在函数内部修改全局变量，可以使用global关键字。

```python
# 在开发时，应该把模块中的所有全局变量定义在所有函数上方
# 这就可以保证所有的函数都能正常访问到每一个全局变量了
num = 10


def demo1():
    # 希望修改全局变量的值 - 使用global 声明一下变量即可
    # global 关键字会告诉编译器后面的变量是全局变量
    # 再使用赋值语句就不会创建新的局部变量
    global num
    num = 99
    print("demo1 ==> %d" % num)


def demo2():
    print("demo2 ==> %d" % num)


demo1()
demo2()

```

代码结构示意图

| shebang     |
| ----------- |
| import 模块 |
| 全局变量    |
| 函数定义    |
| 执行代码    |

全局变量的命名建议

为了避免和局部变量出现混淆，在定义全局变量时，有些公司会有一些开发要求，例如在全局比莱昂名称前面增加 g_ 或者 gl_ 的前缀，修改变量名称可以使用shift + F6快捷键。

44、函数的参数

定义函数时，是否接收参数，或者是否返回结果，是根据实际的功能需求来决定的

- 如果函数内部处理的数据不能确定，就可以将外接的数据以参数的形式传递到函数内部
- 如果希望一个而函数执行完成后，向外界汇报执行结果，就可以增加函数的返回值

45、函数的返回值

在Python中的函数，使用return关键字可以返回结果，函数的调用一方，可以使用变量来接收函数的返回结果。

如果需要函数返回多个结果，可以利用元组返回。

```python
def measure():
    """测量温度和湿度"""
    print("测量开始...")
    temp = 28
    wetness = 50
    print("测量结束...")
    # 元组-可以包含多个数据，因此可使用元组让函数一次返回多个值
    # 如果返回的是元组，小括号可以省略
    # return (temp,wetness)
    return temp, wetness


# 元组接收
result = measure()
print(result)
# 需要单独处理温度和湿度
print(result[0])
print(result[1])
# 如果函数返回类型是元组，同时希望单独处理元组中的数据
# 可以使用多个变量一次性接收函数的返回值
# 注意：使用多个变量接收结果时，变量的个数应该和元组中的元素的个数保持一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)

```

46、交换两个变量的值

```python
a = 6
b = 100
# 解法1: - 使用其他变量
# c = a
# a = b
# b = c

# 解法: - 不使用其他变量
# a = a + b
# b = a - b
# a = a - b

# 解法3: - Python 专有
# a, b = (b, a)
# 等号右边是一个元组，只是省略了括号
a, b = b, a

print(a)
print(b)
```

在函数内部，针对参数使用赋值语句，会不会影响调用函数时传递的实参变量，--不会
无论传递的参数是可变还是不可变，都不会改变实参变量的值。
只要针对参数使用赋值语句，就会在函数内部修改局部变量的引用，不会影响到外部变量的引用

如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据。

```python
def mutable(num_list):
    # num_list = {1, 2, 3}
    num_list.extend([1, 2, 3])
    print(num_list)


gl_list = [6, 7, 8]
mutable(gl_list)
print(gl_list)
```

在python中，列表变量的调用+=本质上实在执行列表变量的extend方法，不会修改变量的引用。

47、缺省参数

定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定的参数默认值
函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用

```python
gl_list = [6, 3, 9]

# 默认按照升序排序 - 可能更多一些
gl_list.sort()
# 如果需要降序排列，需要执行reverse参数
gl_list.sort(reverse=True)
print(gl_list)

```

在函数定义时，参数后面使用赋值语句，可以指定参数的缺省值。

```python
def print_info(name, gender=True):
    """

    :param name: 班上同学的姓名
    :param gender: True 男生 False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print(("%s 是 %s") % (name, gender_text))

# 假设半生同学男生居多
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小米")
print_info("老王")
print_info("小美", False)
```

缺省参数，需要使用最常见的值作为默认值！

如果一个参数的值不能确定，则不应该设置默认值，具体的数值在调用函数时，由外界传递！

 缺省参数应该在参数列表的末尾；如果有多个缺省参数，需要指定参数名，这样解释器才能够知道对应关系。

48、多值参数

有时候可能一个函数能够处理的参数个数是不确定的，这个时候就可以使用多值参数。
Python中有两种多值参数，参数名前面增加一个*可以接收元组，两个 *可以接收字典
一般在给多值参数命名时，习惯使用以下两个名字
*args --存放元组参数。前面有一个 *
**kwargs --存放字典参数，前面有两个 *
args是arguments的缩写，有变量的含义
kw是keyword的缩写，kwargs可以记忆键值对参数

```python
def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)
```

结果：

```
1
(2, 3, 4, 5)
{'age': 18, 'gender': True, 'name': '小明'}
```

```python
# 定义一个函数可以接收任意个整数，返回累加结果
def sum_numbers(*args):

    num = 0
    print(args)
    # 循环遍历
    for n in args:
        num += n

    return  num


result = sum_numbers(1, 2, 3, 4, 5)
print(result)
```

拆包

```python
def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元组变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)
# 拆包语法
# demo(*gl_nums, **gl_dict)
demo(1, 2, 3, name="小明", age=18)
```

49、递归

一个函数内部调动自己，就叫递归。
函数内部代码相同，只针对参数不同，处理的结果不同
当参数满足一个条件时，函数不再执行。这个非常重要，通常被称为递归的出口，否则会出现死循环。

```python
def sum_number(num):
    print(num)
    # 递归的出口，当参数满足条件时，不再执行函数
    if num == 1:
        return
    sum_number(num - 1)


sum_number(3)
```

递归案例，计算数字累加

```python
# 定义一个函数 sum_numbers
# 能够接收一个 num 的整数参数
# 计算1+2+... num 的结果


def sum_number(num):

    # 出口
    if num == 1:
        return 1
    # 数字的累加 num + (1...num -1)
    temp = sum_number(num -1)
    return num + temp


result = sum_number(100)
print(result)

```

递归是一个变成技巧，在处理不确定的循环条件时，非常有用，比如遍历文件目录。