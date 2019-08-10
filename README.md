# LearnPython
这是一个学习Python的项目

## 第一章

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

