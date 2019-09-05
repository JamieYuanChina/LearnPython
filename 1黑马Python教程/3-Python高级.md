# LearnPython
这是一个学习Python的项目

## 第三章 Python高级

1、面向对象(OOP)基本概念

在面向过程的开发程序就是顺序的调用不同的函数。面向过程并不适合复杂项目的开发。
相比较函数，面向对象就是更大的封装，面向对象注重对象和职责，不同对象承担不同责任
面向对象更适合复杂的需求变化，是专门应对复杂项目开发，提供的固定套路
需要在面向过程的基础上，在学习一些面向对象的语法。

2、类和对象

类是对一群具有相同特征或者行为的事物的一个统称，是抽象的，不能直接使用。
特征被称为属性，行为被称为方法。
类就相当于制造飞机的图纸，是一个模板，是负责创建对象的。

对象是由类创建出来的具体存在，可以直接使用，由哪一个类创建出来的对象，就有哪一个类中定义的属性和方法，对象就相当于用图纸制造的飞机。在程序开发中，应该先有类再有对象

类和对象的关系，类是模板，对象是根据类这个模板创建出来的，应该现有类，再有对象
类只有一个，对象可以有很多个。不同对象之间属性可能会各不相同，类中定义了什么属性和方法，对象中就有什么属性和方法。不可能多，也不可能少。

3、类的设计

在程序开发中，要设计一个类，通常需要满足以下三个要素：

- 类名 这类事物的名字，满足大驼峰命名法
- 属性这类事物具有什么样的特征
- 方法这类事物具有什么样的行为。

大驼峰命名法

每个单词的首字母大写，单词与单词之间没有下划线

类名的确定，名词提炼发，分析整个业务流程，出现的名词，通常就是找到的类

属性和方法的确定，对对象的特征描述，通常可以定义成属性，对象具有的行为(动词)，通常可以定义成方法。在需求中没有涉及的属性或者方法在设计类时，不需要考虑。

面向对象的基础语法

dir内置函数可以列出对象的所有属性和方法

在python中 对象几乎是无所不在的，我们之前学习的变量，数据，函数都是对象。

使用内置函数dir传入标识符/数据，可以查看对象内的所有属性及方法

提示 __ 方法名 __ 格式的方法是Python提供的内置方法/属性。

| 序号 | 方法名    | 类型 | 作用                                  |
| ---- | --------- | ---- | ------------------------------------- |
| 01   | __ new__  | 方法 | 创建对象时，会被自动调用              |
| 02   | __ init__ | 方法 | 对象被初始化时，会被自动调用          |
| 03   | __ del__  | 方法 | 对象被从内存中销毁前，会被自动调用    |
| 04   | __ str__  | 方法 | 返回对象的描述信息，print函数输出使用 |

4、类的定义

定义只包含方法的类

```python
class 类名:
    def 方法1(self, 参数列表):
        pass
    
    def 方法2(self, 参数列表):
        pass    
```

方法的第一个参数必须为self，类名要符合大驼峰命名法。

创建对象

```python
# 定义类
class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")


# 创建对象
tom = Cat()
# 可以使用.属性名 的方式在类的外部，对象上直接增加属性，但是不建议这么使用。
tom.name = "Tom"
# 调用对象的方法
tom.drink()
tom.eat()
# 同一个类创建多个对象。
lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()
```

其中self参数表示当前调用方法的对象自己，在方法内部，可以通过self.访问对象的属性和其他方法。

在类的外部给对象增加属性的方法不推荐使用，原因是如果在运行时，没有找到属性，程序会报错。对象的属性应该由类来定义。

5、初始化方法

当使用类名()创建对象时，会自动执行以下操作：一是为对象咋内存中分配空间，二是为对象属性设置初始值，也就是调用init方法。(这个应该类似与C++中的构造函数)

6、初始化方法内部定义属性

在 init方法内部使用self.属性名 = 属性值的方式定义，使用该类创建的对象都会拥有该属性

```python
class Cat:
    def __init__(self, new_name):  # 相当于C++的构造函数
        self.name = new_name
        print("%s 来了" % self.name)
        
    def eat(self):
        print("%s 爱吃鱼" % self.name)
    def __del__(self):  # 相当于C++的析构函数
        print("%s 我去了" % self.name)
    def __str__(self):
        # 必须返回字符串
        return “我是小猫” % self.name
tom = Cat("Tom")
print(tom.name)
tom.eat()
# 默认输出类和对象地址，使用了__str__后可以输出自定义字符串
print(tom)
# del 关键字可以删除一个对象
del tom
```

在对象的方法内部，可以直接访问对象的属性

同一个类创建的多个对象之间，属性互不干扰。

```python
class Person:

    def __init__(self, name, weight):

        # self.属性 = 等号右侧是形参
        self.name = name
        self.weight = weight

    def __str__(self):

        return "我的名字叫 %s 体重是%.2f 公斤" % (self.name, self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)
        self.weight -= 0.5

    def eat(self):
        print("%s 是吃货，吃完这顿在减肥" % self.name)
        self.weight += 1


xiaoming = Person("小明", 75.0)

xiaoming.run()
xiaoming.eat()
print(xiaoming)

# 小美爱跑步
xiaomei = Person("小美",45)

xiaomei.eat()
xiaomei.run()
print(xiaomei)
print(xiaoming)

```

```python
# 摆放家具案例
class HouseItem:

    def __init__(self, name, area):

        # self.属性 = 等号右侧是形参
        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] 占地 %.2f " % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python 能够自动的将一对括号内的代码连接在一起
        return ("户型： %s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self,item):
        print("要添加 %s", item)
        # 判断家具的面积
        if item.area >self.free_area:
            print("%s 的面积太大了，无法添加" % item.name)
            return
        # 将家具的名称添加到列表
        self.item_list.append(item.name)

        # 计算剩余面积
        self.free_area -= item.area

# 创建家具 ctrl + / 多行注释
bed = HouseItem("席梦思", 40)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 20)

print(bed)
print(chest)
print(table)


# 创建房子对象
my_house = House("两室一厅", 60)
my_house.add_item(bed)
my_house.add_item(chest)
my_house.add_item(table)

print(my_house)

```

一个对象的属性可以是另外一个类创建的对象
在定义属性时，如果不知道设置什么初始值，可以使用Nane关键字，表示什么都没有。
身份运算符用于比较两个对象的内存地址是否一致，也就是对同一个对象的引用。
在Python中针对None比较时，建议使用is判断
is用于判断两个变量引用对象是否为同一个。判断地址
==用于判断引用变量的值是否相同。判断值

```python
class Gun:
    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断子弹数量
        if self.bullet_count <= 0:
            print("[%s] 没有子弹了..." % self.model)
            return
        # 发射子弹
        self.bullet_count -= 1

        # 提示信息
        print("[%s] 突突突... [%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        self.name = name
        # 因为新兵没有枪，所以这个对象赋值为None
        self.gun = None

    def fire(self):
        # 判断是否有枪,针对None 应该使用is 
        # if self.gun == None:
        if self.gun is None:
            print("[%s]" % self.name)
            return
        # 高喊口号
        print("冲啊...[%s]" % self.name)
        # 让枪装填子弹
        self.gun.add_bullet(50)
        # 让枪发射子弹
        self.gun.shoot()


# 创建枪对象
ak47 = Gun("AK47")


# 创建许三多
xusanduo = Soldier("许三多")

xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)

```

7、私有属性和私有方法

如果在开发中，对象的某些属性和方法不希望被外部访问，只希望在内部访问，这就是私有属性和方法。在定义属性和方法的时候，在变量名称前面增加两个下划线即可。

```python
class Woman:
    def __init__(self, name):
        self.name = name
        # 年龄是私有属性前面增加两个下划线
        self.__age = 18

    def __secret(self):
        # 在对象方法的内部是可以访问私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Woman("小芳")
# 私有属性在外部不能访问
# print(xiaofang.__age)
# 私有方法同样不可以在外部访问,但是Python中没有真正意义上的私有
# 在定义私有属性后，实际上解释器对于私有属性和方法做了特殊处理
# 处理方式就是在名称前面增加了 _类名 变成为了 _类名__名称
xiaofang._Woman__secret()

```

8、继承

面向对象三大特点：
封装，根据职责将属性和方法封装到一个抽象的类中
继承，实现代码重用，相同的代码不需要重复编写
多态，不同的对象调用相同的方法，产生不同的结果，增加代码的灵活度
单继承，子类拥有父类的所有方法和属性。

```python
class Animal:
    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog(Animal):
    def bark(self):
        print("汪汪叫")


class XiaoTianQuan(Dog):
    def fly(self):
        print("我会飞")

    # 重写bark 方法
    def bark(self):
        print("叫的跟神一样")
        # 对父类的方法的调用
        super().bark()
        # 在Python2.x中可以使用 父类名.方法 来调用,如果使用本类名调用，会出现递归调用，死循环
        Dog.bark(self)
        print("@%#$%#$%#$%")


xtq = XiaoTianQuan()
xtq.eat()
xtq.drink()
xtq.run()
xtq.sleep()
xtq.bark()
xtq.fly()

```

子类，父类，类继承
派生类，基类，类派生
两种说法而已

9、方法的重写

当父类的方法无法实现子类的功能时，可以对方法进行重写(override)，在子类中直接重写一个同名方法即可。

父类的私有属性和方法，在子类中无法调用。

子类的对象可以通过调用父类的共有方法访问父类的私有属性和方法。

10、多继承

子类继承多个父类，拥有所有父类的属性和方法，就是所继承。

```python
class A:
    def test(self):
        print("A -- test 方法")


class B:
    def demo(self):
        print("demo 方法")

    def test(self):
        print("B -- test 方法")

# 如果不同父类存在同名的方法，尽量避免使用多继承。
class C(B, A):
    pass

c = C()

c.demo()
c.test()

# 确定C类调用方法的顺序,注意这里的C是类，不是对象。 object类是所有类的'祖宗类'
print(C.__mro__)
```

object 是Python为所有对象提供的基类，提供了一些内置的属性和方法，可以使用dir函数查看。
所有一object为基类的类叫做新式类，不以object为基类的类叫做经典类，不推荐使用经典类。
在Python3中，如果不指定基类，默认一object为基类，所以Python3中所有的类都是新式类。
在Python2中，如果不指定基类，则不会一object为基类。
新式类和经典类在多继承时会影响到方法的搜索顺序
为了保证编写的代码能够同时在Python3和Python2中运行，今后定义类时如果没有父类，建议统一继承自object

class 类名(ojbect):

11、多态

不同的子类对象，调用相同的父类方法，产生不同的执行结果。
多态可以增加代码的灵活度
以继承和重写父类方法为前提
是调用方法的技巧，不会影响到类的内部设计。

```python
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name
        
    def game_with_dog(self, dog):
        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        dog.game()


# 创建一个狗对象
# wangcai = Dog("旺财")
wangcai = XiaoTianDog("飞天旺财")
# 创建一个小明对象
xiaoming = Person("小明")
# 让小明调用和狗玩耍
xiaoming.game_with_dog(wangcai)
```

使用面向对象开发，首先设计类，使用类名()创建对象，创建对象有两步，第一步在内存中分配空间，第二步调用初始化方法__ init__。所以Python类的所有属性都必须在 init方法中定义。
对象建立后，内存中就有一个对象的实实在在的存在，也就是实例。
创建对象的过程就是实例化，对象的属性就叫做实例属性，对象的方法就叫做实例方法。
在执行程序时，对象拥有自己的实例属性，调用对象方法，可以通过self.实现访问自己的属性和方法。
每一个对象都有自己独立的内存空间，保存个子不同的属性；
多个对象的方法，在内存中只有一份，在调用方法时，需要把对象的引用传递到方法内部。

12、类是一个特殊的对象（408）

在Python中一切皆对象，类属于类对象，在程序运行时类同样会加载到内存，类对象在内存中只有一份，使用一个类对象可以创建多个实例对象，除了封装实例的属性和方法外，类对象还可以拥有自己的属性和方法，可以乘坐类属性和类方法。通过类名.的方式访问类属性和类方法。

13、类属性

类属性就是给类对象中定义的属性，通常用来记录与这个类相关的特性，比如统计某一个类实例化了多少个对象。

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性值+1
        Tool.count += 1


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")


# 使用 对象名. 也可以访问类属性,但是不推荐使用这种方式
# 如果只是读取，没有问题，如果有赋值，不会改变类属性值，而是会在对象中添加该属性并且赋值
tool2.count = 12
print("工具总数 %d " % tool2.count)

# 使用 类名.属性 的方式访问类属性
print(Tool.count)
```

14、类方法

类方法是针对类对象定义的方法，在类方法内部可以直接访问类属性或者调用其他类方法。
类方法需要使用修饰词 @classmethod 来标识，告诉解释器这是一个类方法
类方法的第一个参数应该为cls，使用其他名称也可以，但是习惯用cls
通过 类名. 的方式来访问类方法，调用方法时，不需要传递cls参数。
在方法内部，可以使用cls.来访问类的属性和其他方法。

```python
class Tool(object):
    # 使用赋值语句定义类属性，记录所有工具对象的数量
    count = 0

    def __init__(self, name):
        self.name = name
        # 让类属性值+1
        Tool.count += 1

    # 定义一个类方法
    @classmethod
    def show_tool_count(cls):
        print("工具对象的数量 %d" % cls.count)


# 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")


# 调用类方法
Tool.show_tool_count()
```

15、静态方法

如果在开发时，需要在类中封装一个方法，这个方法既不需要访问实例属性和实例方法，也不需要访问类属性和类方法，这时候就可以定义一个静态方法。

```python
class Dog(object):

    @staticmethod
    def run():
        print("小狗要跑")


# 调用静态方法,不需要创建对象，直接使用 类名. 的方式即可
Dog.run()

```

16、方法的综合案例

```python
class Game(object):

    # 类属性，历史最高分
    top_score = 0

    def __init__(self,player_name):
        # 定义实例属性，玩家姓名
        self.player_name = player_name

    # 定义静态方法
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    # 定义对象实例方法
    def start_game(self):
        print("%s 开始游戏了..." % self.player_name)


# 查看游戏帮助信息，调用静态方法
Game.show_help()

# 查看历史最高分，调用类方法
Game.show_top_score()

# 创建游戏对象，调用对象的实例方法
game = Game("小明")
game.start_game()
```

17、单例设计模式

设计模式是前人工作的总结和提炼，通常本人们用来解决某一特定问题的成熟方案。使用设计模式是为了可重用代码，让代码更容易被理解，保证代码可靠性。

单例设计模式，目的是让类创建对象，在系统中只有唯一的一个实例，每一次执行类名()返回的对象都是相同的。

单例设计模式应用场景，音乐播放对象，回收站对象，打印机对象等等。

使用类名()创建对象时，Python解释器会首先调用 __ new __ 方法为对象分配空间，这个方法是有object基类提供的内置静态方法，主要作用是分配空间并且返回对象的引用，Python解释器获得对象的引用后，将引用作为第一个参数，传递给 __ init __ 方法。

重写 __ new __ 方法，一定要 return super().__ new __ (cls)，否则解释器获取不到分配了空间的对象引用，就不会调用初始化方法。注意，__ new __ 是一个静态方法，在调用时需要主动传递cls参数

```python
class MusicPlayer(object):

    # 重写 __new__函数
    def __new__(cls, *args, **kwargs):

        # 创建对象时，new方法会被自动调用
        print("创建对象，分配空间")
        # 为对象分配空间
        instance = super().__new__(cls)
        # 返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print(player)
```

单例模式的实现

```python
class MusicPlayer(object):

    # 定义类属性，记录第一个被创建的对象引用
    instance = None
    # 定义类属性，记录是否初始化
    init_flag = False

    # 重写 __new__函数
    def __new__(cls, *args, **kwargs):

        # 盘算类属性是否是空对象
        if cls.instance is None:
            # 为对象分配空间
            cls.instance = super().__new__(cls)
        # 返回对象的引用
        return cls.instance

    def __init__(self):
        # 判断是否初始化过，如果初始化过，直接返回，保证只初始化一次。
        if MusicPlayer.init_flag:
            return
        print("播放器初始化")
        MusicPlayer.init_flag = True


# 创建播放器对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)

```

18、异常

程序运行时，如果Python解释器遇到一个错误，会停止程序运行，并提示一些错误信息，这就是异常。
程序停止并提示错误信息这个动作就叫做抛出(raise)异常
程序开发时，很难将所有特殊情况都处理的面面俱到，通过异常捕获，可以针对突发事件做集中处理，从而保证程序的稳定性和健壮性。

在程序开发中如果对某些代码执行不能确定是否正确，可以增加try来捕获异常。

```python
try:
    # 不能确定执行正确的代码
    num = int(input("请输入一个整数:"))
except:
    # 错误的处理代码
    print("请输入正确的整数")

print("-" * 50)
```

```python
try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数:"))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)

# python 解释器抛出异常时，最后一行的第一个单词，就是错误类型
# 根据不同类型的异常，可以分别进行处理
except ZeroDivisionError:
    print("除零错误")
except ValueError:
    print("请输入正确的整数")
```

捕获未知错误

在程序开发时，要预判到所有的可能出现的错误，还是有一定难度的，如果希望无论出现任何错误，都不会因为Python解释器抛出异常而被终止，可以再增加一个except

```python
try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数:"))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)

# python 解释器抛出异常时，最后一行的第一个单词，就是错误类型
# 根据不同类型的异常，可以分别进行处理

except ValueError:
    print("请输入正确的整数")

# 捕获未知错误
except Exception as result:
    print("未知错误 %s" % result)

```

异常的完整语法

```Python
try:
    # 提示用户输入一个整数
    num = int(input("输入一个整数:"))
    # 使用8除以用户输入的整数并且输出
    result = 8 / num
    print(result)

# python 解释器抛出异常时，最后一行的第一个单词，就是错误类型
# 根据不同类型的异常，可以分别进行处理

except ValueError:
    print("请输入正确的整数")

# 捕获未知错误
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行")

print("-" * 50)
```

异常的传递

当函数或者方法出现异常，会将异常传递给函数的调用一方，如果传递到主函数，依然没有处理，程序才会终止，根据这个特性，可以在主函数中增加异常处理，捕获异常，这样在代码中不需要增加大量的异常捕获，能够保证代码的整洁。

```python
def demo1():
    return int(input("输入整数："))


def demo2():
    return demo1()

# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())

except Exception as result:
    print("未知错误 %s" % result)
```

抛出异常

一般在特有业务需求时使用，比如输入密码函数，输入合法的密码，返回密码到主函数，如果输入密码长度不够，可以主动抛出异常给主函数，告诉主函数密码长度不够。

Python中提供了一个Exception异常类，如果需要抛出异常，首先使用Exception 创建异常对象，然后使用raise关键字抛出异常对象即可。

```Python
def input_password():
    # 提示用户输入密码
    pwd = input("请输入密码：")
    # 判断密码长度，如果大于等于8，返回用户输入密码
    if len(pwd) >=8:
        return pwd
    # 如果密码小于8 主动抛出异常
    print("主动抛出异常")
    # 创建异常对象
    ex = Exception("密码长度不够")
    # 抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as result:
    print(result)

```

19、模块

模块是Python程序框架的核心概念，每一个以扩展名py结尾的Python源代码文件就是一个模块，模块名同样也是一个标识符，需要符合标识符命名规则；模块中的全局变量，函数，类都是提供给外接直接使用的工具，模块就好比工具包，想要使用这个工具包中的工具就需要先导入这个模块。

导入方法一

```Python
import 模块名1
import 模块名2
```

可以使用 模块名. 的方式使用模块中的全局变量，函数，类了。

如果模块的名字太长，可以使用as关键字指定模块的别名，以方便在代码中使用

```python
import 模块1 as 模块别名
```

注意，模块别名应该符合大驼峰命名法

导入方法二

如果希望从某一个模块中导入部分工具，就可以使用from ... import 方式导入

import 模块名 方式是一次性导入模块中的全部工具，并且通过模块名来访问。

```python
# 从模块导入某一个工具
from 模块名 import 工具名
```

如此导入后，不需要使用模块名，可以直接使用模块提供的工具，包括全局变量，函数，类。

如果两个模块，存在同名的函数，那么后导入的模块函数，会覆盖掉先导入的函数。

如果确实需要使用同名函数，可以把其中一个使用as 关键字定义一个别名，两个函数名称就不冲突了

```
# 从模块导入某一个工具
from 模块名1 import 工具名 as 新工具
from 模块名2 import 工具名
```

开发时 import 代码应该统一写在代码顶部，更容易发现冲突，一旦发现冲突，可以使用as关键字起一个别名。

使用from ... import 也可以一次性导入模块多有工具

```python
# 导入模块中所有工具
from 模块名 import * 
```

但是不推荐如此使用，因为函数重名并没有任何提示，出现问题不好排查。

模块的搜索顺序，Python解释器在导入模块时，会搜索当前目录指定模块名的文件，如果有就直接导入，如果没有再搜索系统目录。所以在开发时，不要给文件起一个和系统文件同名的名称，否则可能导致程序异常无法执行。

Python中每个模块都有一个内置属性__ file __ 可以查看模块完整路径。

```Python
import random
# 查看模块全路径
print(random.__file__)
# 如果当前目录下有一个random.py的文件，那么下面代码会异常。
rand = random.randint(0, 10)
print(rand)
```

Python设计原则，每一个文件都应该是可以被导入的。

一个独立的Python文件就是一个模块，导入文件时，文件中所有没有任何缩进的代码都会被执行一遍。

实际开发中每个模块都是独立开发的，大多都有专人负责，开发人员通常会在模块增加一些测试代码。这些测试代码只在模块内使用，而被导入时不需要执行。此时可以使用__ name __属性实现。

__ name __ 属性可以做到，测试模块的代码只在测试下运行，被导入时不会被执行！

__ name __ 是一个Python内置属性，记录着一个字符串，如果被导入，__ name __ 就是模块名，如果是当前执行程序，__ name __ 就是 __ main __

模块代码:

```Python
# 全局变量，函数，类,注意，直接执行代码不是向外界提供的工具！


def say_hello():
    print("你好，你好，我是 say_hello")


# 定义模块测试函数
def main():
    print("这是小明开发模块的测试函数")


# 根据 __name__ 判断是否执行下列代码
if __name__ == "__main__":
    main()

```

调用代码：

```python
import my_模块 as mod1

mod1.say_hello()
```

20、包

包是一个包含多个模块的特殊目录，目录下有一个特殊的文件 __ init __.py ，包的命名方式和变量名一致，小写字母+ _。包的好处是可以一次导入包中所有模块，使用方法为 import 包名。要在外接使用保重的模块，需要在  _ _ init _ _ .py中指定对外界提供的模块列表。

```python
# send_message.py
def send(text):
    print("正在发送 %s ..." % text)
```

```python
# receive_message.py
def receive():
    return "这是来自100xx 的短信"
```

```python
# 把当前目录下的多个模块导入到__init__.py，才能对外提供相应模块功能
from . import send_message
from . import receive_message

```

```python
# my_导入包.py

# 导入my_message 包
import my_message

# 使用 包名.模块名.方法名 调用包中的方法
my_message.send_message.send("hello")
txt = my_message.receive_message.receive()
print(txt)
```

21、发布模块

创建setup.py文件

```python
from distutils.core import setup
setup(name="my_message",  # 包名
     version=“1.6”，  # 版本
     ......)
```

构建模块

```shell
$ python3 setup.py build
```

生成发布压缩包

```shell
$ python3 setup.py sdist
```

最后生成 my_message.tar.gz的压缩包

22、安装模块

解压缩发布的压缩包，得到的目录中有PKG-INFO文件，描述了包的信息。

```shell
$ sudo python3 setup.py install
```

此时模块就会被安装到Python的系统目录/usr/local/lib/python3.5/dist-packages/ 下

23、删除包

直接使用rm -rf 被安装到目录下的所有文件即可。

24、pip安装第三方模块

第三方模块是指由知名的第三方团队开发的并且被程序员广泛认可的Python包/模块。例如pygame就是一个非常成熟的游戏开发模块。pip是一个现代的，通用的Python包管理工具，提供了对于Python包的查找，下载，安装，卸载等功能。

在Deepin中安装pip

```shell
$ sudo apt install  python3-pip
```

在Python2.x环境使用pip命令，在Python3.x环境使用pip3命令。

```shell
$ sudo pip3 install pygame
```

25、文件(448)

计算机文件分为文本文件和二进制文件。

对文件的操作都是按照三步骤执行，

打开，读写，关闭。

Python中操作文件的1个函数和3个方法

| 序号 | 函数、方法 | 说明                       |
| ---- | ---------- | -------------------------- |
| 01   | open       | 打开文件，返回文件操作对象 |
| 02   | read       | 将文件内容读取到内存       |
| 03   | write      | 将指定内容写入到文件       |
| 04   | close      | 关闭文件                   |

open函数负责打开文件，并且返回文件对象
其他三个方法都需要通过文件对象来调用。
open函数第一个参数是要打看的文件名，区分大小写，如果文件存在，返回文件操作对象，如果文件不存在，抛出异常；
read方法可以一次性读入并且返回文件的所有内容
close负责关闭文件
如果忘记关闭文件，会造成系统资源消耗，而且会影响到后续对文件的访问，注意，方法执行后，会把文件指针移动到文件尾部。
在开发中，通常都是先编写文件打开和关闭的代码，再编写中间针对文件的读写操作。

```python
# 打开文件
file = open("README")
# 读取文件内容
text = file.read()
print(text)
print(len(text))

print("-" * 50)

text = file.read()  # 调用过read方法后文件指针默认到了文件尾部，此时再次read将得不到任何数据
print(text)
print(len(text))

# 关闭文件
file.close()
```

文件指针标记从哪个位置开始读取数据，第一次打开文件时，通常文件指针会指向文件的开始位置

当执行了read方法后，文件指针会移动到文件末尾。

open函数默认以只读方式打开文件，第二个参数为打开方式。

| 访问方式 | 说明                                                         |
| -------- | ------------------------------------------------------------ |
| r        | 只读方式打开文件，默认值，如果文件不存在，抛出异常           |
| w        | 只写方式打开，如果文件存在，会被覆盖，不存在则新建           |
| a        | 追加的方式打开，如果文件存在，指针放在文件结尾，不存在创建并写入 |
| r+       | 读写方式打开，文件指针在开头，不存在，抛异常                 |
| w+       | 读写方式打开，文件存在会覆盖，不存在创建                     |
| a+       | 读写方式打开，文件存在文件指针放到文件尾部，不存在创建并且写入 |

```python
# 打开文件
file = open("README", "w")
# 写入文件内容
text = file.write("hello")


# 关闭文件
file.close()
```

频繁的移动文件指针，会影响文件的读写效率，开发中更多的是以只读/只写的方式来操作文件。

安行读取文件内容

read方法会默认把文件的所有内容读取到内存。如果文件太大，对内存的占用非常严重。

readline方法可以一次只读取一行，方法执行后，文件指针自动下移一行，准备再次读取。

```Python
# 打开文件
file = open("README", "r")

# 按照行读取
while True:
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    
    print(text)

# 关闭文件
file.close()

```

文件读写案例--复制文件

```Python
# 打开文件
file_read = open("README")
file_write = open("README.MD", "w")

# 小文件读写
# text = file_read.read()
# file_write.write(text)

# 大文件读写
while True:
    # 读取一行内容
    text = file_read.readline()
    # 判断是否读取到内容
    if not text:
        break

    file_write.write(text)
    
    
# 关闭文件
file_read.close()
file_write.close()
```

文件目录的常用管理操作

在Python中如果希望通过程序实现文件的创建，删除，重命名，该路径，查看目录内容等操作，需要导入os 模块

文件操作：
改名：os.rename(源文件名，目标文件名)
删除：os.remove(文件名)

目录操作：
列目录：os.listdir(目录名)
创建目录：os.mkdir(目录名)
删除目录：os.rmdir(目录名)
获取当前目录：os.getcwd
修改工作目录：os.chdir(目标目录名)
判断是否是文件：os.path.isdir(文件路径)

26、文本文件的编码格式

常见编码有ASCII编码，UNICODE编码，Python2.x默认使用ASCII编码，Python3.x默认使用UNICODE编码。UTF-8是UNICODE编码的一中编码格式。

UTF-8 使用1-6个字节表示一个字符，几乎涵盖了地球上的所有文字。大多数汉字会使用3个字节表示。

27、如何在Python2中使用中文

如果要在Python2中使用UTF-8编码，需要在Python源文件的第一行增加一行特殊注释

```python
# *-* coding:utf8 *-*

# 引号前面的u告诉解释器这是一个utf8编码的字符串
hello_str = u"hello 世界"
print(hello_str)

for c in hello_str:
    print(c)
```

28、eval函数

eval()函数功能十分强大，能够将字符串当成有效的表达式来求值，并返回计算结果。

```python
input_str = input("请输入算术题：")
print(eval(input_str))
```

不要滥用eval，千万不要使用eval直接转换input的结果。如果用户输入以下字符串，可能造成系统安全问题。

```shell
__import__('os').system('rm -rf mydir')
```

