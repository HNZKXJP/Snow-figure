import pygame
import sys
import random

pygame.init()#初始化pygame
bg_img ="C:/Users/YOGA/Pictures/AlbertaThanksgiving_ROW3027926486_1920x1200.jpg"
bg_size = (900, 500)
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("雪景图")
bg = pygame.image.load(bg_img)
snow_list = []
for i in range(150):
    x_site = random.randrange(0, bg_size[0])   # 雪花圆心位置
    y_site = random.randrange(0, bg_size[1])   # 雪花圆心位置
    X_shift = random.randint(-1, 1)         # x 轴偏移量
    radius = random.randint(4, 6)           # 半径和 y 周下降量
    snow_list.append([x_site, y_site, X_shift, radius])
for i in range(len(snow_list)):
 # 绘制雪花，颜色、位置、大小
   pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - 3)
 # 移动雪花位置（下一次循环起效）
   snow_list[i][0] += snow_list[i][2]
   snow_list[i][1] += snow_list[i][3]
 # 如果雪花落出屏幕，重设位置
   if snow_list[i][1] > bg_size[1]:
     snow_list[i][1] = random.randrange(-50, -10)
     snow_list[i][0] = random.randrange(0, bg_size[0])
while True:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
    screen.blit(bg, (0, 0))
    # 雪花列表循环
    for i in range(len(snow_list)):
        # 绘制雪花，颜色、位置、大小
        pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - 3)
        # 移动雪花位置（下一次循环起效）
        snow_list[i][0] += snow_list[i][2]
        snow_list[i][1] += snow_list[i][3]
        # 如果雪花落出屏幕，重设位置
        if snow_list[i][1] > bg_size[1]:
            snow_list[i][1] = random.randrange(-50, -10)
            snow_list[i][0] = random.randrange(0, bg_size[0])
    # 刷新屏幕
    pygame.display.flip()
    clock = pygame.time.Clock()  
    clock.tick(20)  