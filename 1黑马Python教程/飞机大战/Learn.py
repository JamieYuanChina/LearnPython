import pygame
from plane_sprites import *

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

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png", 2)
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy, enemy1)
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
    screen.blit(hero, hero_rect)

    # 让精灵组调用两个方法
    enemy_group.update()
    enemy_group.draw(screen)
    # 更新显示
    pygame.display.update()

pygame.quit()
