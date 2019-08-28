# LearnPython
这是一个学习Python的项目

## 第四章 Python实战-- 飞机大战

1、目标是强化面向对象设计，体验使用pygame模块游戏开发。

pygame是一个Python模块，专为电子游戏设计

安装pygame

```shell
$ sudo pip3 install pygame
```

验证安装

```shell
$ python3 -m pygame.examples.aliens
```

2、新建项目

在使用PyCharm新建项目的时候，关于项目环境会有两个选项，一个是New environment using...，这个是用来建立项目的虚拟环境的，每个项目配置一个虚拟环境，使用特定的库版本，便于项目部署。另一个选项Existing interpreter用来使用系统中现有环境。

把图像素材目录拷贝到项目主目录中。

3、创建游戏的主窗口

在使用pygame之前，需要初始化，游戏结束之前，需要退出。

```python
import pygame

pygame.init()
print("游戏的代码...")
pygame.quit()

```

pygame坐标系远点位于窗口左上角，向右，向下依次递增。水平方向以x表示，垂直方向以y表示。所有能够见到的元素，都是以矩形区域体现的，这里所有的单位都是一像素为单位。

要描述一个矩形区域，需要有四个元素，(x,y)(width,height)
pygame提供了一个专门类用于描述矩形区域，pygame.Rect。
pygame.Rect是一个特殊的pygame类，不用调用初始化函数即可使用。

```python
import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)
print("英雄的原点 %d %d" % (hero_rect.x, hero_rect.y))
# print("英雄的尺寸 %d %d" % (hero_rect.height, hero_rect.width))
print("英雄的尺寸 %d %d" % hero_rect.size)

```
pygame专门提供了一个模块 pygame.display用于创建，管理游戏窗口
pygame.display.set_mode() 初始化游戏窗口
pygame.display.update() 刷新屏幕内容。
set_mode(resolution=(0,0), flags=0, depth=0)
resolution指定屏幕的宽和高，默认和屏幕大小一样大。
flags指定是否全屏等。
depth指定颜色深度等。
返回值可以理解为游戏屏幕的句柄，需要变量接收。

```python
import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

while True:
    pass

pygame.quit()
```

4、绘制背景图像和英雄

电脑中的游戏一般在60帧/秒以上才能保证高品质的动画效果。
程序中应该有一个无限循环，叫做游戏循环，保证游戏连续。
游戏的框架：分为初始化和游戏循环两大部分。
初始化包括：设置游戏窗口，绘制图像初始位置，设置游戏时钟
游戏循环包括：设置刷新帧率，检测用户交互，更新所有图像位置，更新屏幕显示。

英雄的简单动画，在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置。在游戏循环中每次让英雄的y-1，向上移动。当y<=0的时候移动到屏幕底部。

注意，在每一调用update()方法之前，需要把所有的游戏图像重新绘制一遍，而且应该先绘制背景图像。

5、游戏循环中的监听事件(event)

游戏启动后，用户针对游戏所做的操作，例如，点击关闭按钮，点击鼠标，按下键盘等，都是事件，只有捕获到事件，才能做相应处理。pygame中通过pygame.event.get()方法获取事件列表。

```python
import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 加载图像数据，包括背景和英雄图像
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (200, 500))
# 更新显示区
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()
# 定义rect记录飞机的位置
hero_rect = pygame.rect.Rect(200, 500, 102, 126)
# 游戏循环，意味着游戏正式开始
while True:
    # 指定游戏循环内部的代码执行频率
    clock.tick(60)
    # 捕获事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            # 卸载所有模块
            pygame.quit()
            # 直接终止当前执行的程序
            exit()

    # 修改飞机位置
    hero_rect.y -= 1
    # 判断飞机是否移除游戏窗口
    if hero_rect.y <= -126:
        hero_rect.y = 700
    # 绘制图像,必须先绘制背景图像，否则会有重影
    screen.blit(bg, (0, 0))
    screen.blit(hero, (200, hero_rect.y))
    # 更新显示
    pygame.display.update()

pygame.quit()
```

6、理解精灵和精灵组

图像的加载，位置的变化，绘制图像都需要编写代码处理，为了简化开发，pygame提供了两个类。

pygame.sprite.Sprite 存储图像数据和位置Rect的对象。

pygame.sprite.Group

在游戏初始化中创建精灵，创建精灵组

在游戏循环中，更新精灵组，精灵组重绘，显示更新。

精灵类需要派生获得。

```python
# 飞机大战精灵类
import random
import pygame
# 屏幕大小的常量,常量名用大写字母
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 定义常量--刷新的频率
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENMEY_EVENT = pygame.USEREVENT


class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""
    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class Background(GameSprite):
    """游戏背景精灵"""
    def __init__(self, is_alt=False):
        # 调动父类的方法实现精灵的创建
        super().__init__("./images/background.png")
        # 判断是否是交替图像，如果是需要设置初始化位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法实现
        super().update()
        # 判断是否移出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height


class Enemy(GameSprite):
    """敌机精灵"""
    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始随机位置
        self.rect.bottom = 0
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        # 调用父类方法，保持垂直方向飞行
        super().update()
        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            print("飞机出屏，需要从精灵组删除...")
            
```



```python
# 飞机大战主游戏类

# 首先导入官方包，其次导入第三方pygame包，最后导入自己的包
import pygame
from plane_sprites import *


# 创建主游戏类
class PlaneGame(object):
    """飞机大战主游戏"""
    def __init__(self):
        print("游戏初始化")
        # 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，创建精灵和精灵组
        self.__create_sprites()
        # 设置定时器事件-- 创建敌机 1s
        pygame.time.set_timer(CREATE_ENMEY_EVENT, 1000)

    # 定义私有方法，创建精灵
    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

    # 定义启动游戏方法
    def start_game(self):
        print("游戏开始...")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENMEY_EVENT:
                print("敌机出场...")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到精灵组
                self.enemy_group.add(enemy)

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

    @staticmethod
    def __game_over():
        # 游戏结束
        pygame.quit()
        exit()


# 在pycharm中敲入main会自动提示
if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()

```

496