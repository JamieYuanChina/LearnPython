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

401