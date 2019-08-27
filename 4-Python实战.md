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

468