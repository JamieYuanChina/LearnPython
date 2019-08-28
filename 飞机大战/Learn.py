import pygame

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))
# 加载图像数据
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 绘制图像
screen.blit(bg, (0, 0))
screen.blit(hero, (200, 500))
# 更新显示区
pygame.display.update()
# 创建时钟对象
clock = pygame.time.Clock()

while True:
    clock.tick(60)

pygame.quit()
