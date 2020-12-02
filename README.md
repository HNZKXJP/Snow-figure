# Python实现雪花飘落雪景图，可带配乐
功能实现用到的 Python 库为 pygame

雪景图的实现基本思路如下：

`1)找一张自己喜欢的图片作为背景图`

`2)添加雪飞飘落效果`

`3)添加音乐效果`

首先，来生成主窗口及设置背景图，代码实现如下：

`bg_img = "bg.jpeg"`

`bg_size = (900, 500)`

`screen = pygame.display.set_mode(bg_size)`

`pygame.display.set_caption("雪景图")`

`bg = pygame.image.load(bg_img)`

窗口的宽、高根据背景的尺寸来设置

接着来实现雪花飘落效果，先来定义一个雪花列表，代码实现如下：

`snow_list = []`
 
 `for i in range(150):`

    x_site = random.randrange(0, bg_size[0])   # 雪花圆心位置
    y_site = random.randrange(0, bg_size[1])   # 雪花圆心位置
    X_shift = random.randint(-1, 1)         # x 轴偏移量
    radius = random.randint(4, 6)           # 半径和 y 周下降量
    snow_list.append([x_site, y_site, X_shift, radius])

再来实现雪花位置更新，实现动态下雪的效果，代码实现如下：

`for i in range(len(snow_list)):`

` pygame.draw.circle(screen, (255, 255, 255), snow_list[i][:2], snow_list[i][3] - 3)`
 
 ```snow_list[i][0] += snow_list[i][2]
 
 snow_list[i][1] += snow_list[i][3]```

 `if snow_list[i][1] > bg_size[1]:
 
  snow_list[i][1] = random.randrange(-50, -10)
  
  snow_list[i][0] = random.randrange(0, bg_size[0])`


因为我们要实现的是雪花不断飘落的效果，因此再来设置一个循环来不断刷新屏幕，代码实现如下：
while not done:
    # 消息事件循环，判断退出
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
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
    clock.tick(20)