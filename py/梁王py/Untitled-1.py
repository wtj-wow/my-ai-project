import pygame
import time
import random
import sys  # 用來正常退出

# 初始化 pygame
pygame.init()

# 顏色定義
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 遊戲畫面尺寸
width = 600
height = 400

# 建立畫面
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('🐍 貪食蛇遊戲 by ChatGPT')

# 控制遊戲速度
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 30  # 初始設定速度，可以後面根據需要修改

# 字體
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# 顯示分數
def score_display(score):
    value = score_font.render("得分: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

# 畫出蛇
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

# 顯示訊息
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# 遊戲循環
def gameLoop():
    while True:
        game_over = False
        game_close = False

        # 初始位置
        x = width / 2
        y = height / 2

        dx = 0
        dy = 0

        snake_list = []
        length_of_snake = 1

        # 隨機生成食物
        food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

        while not game_over:

            while game_close:
                screen.fill(blue)
                message("遊戲結束！按 Q 離開 或 C 再來一次", red)
                score_display(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            sys.exit()  # 正確退出遊戲
                        if event.key == pygame.K_c:
                            game_over = True
                            game_close = False

            # 監聽按鍵
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # 正確退出遊戲
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT and dx == 0:
                        dx = -snake_block
                        dy = 0
                    elif event.key == pygame.K_RIGHT and dx == 0:
                        dx = snake_block
                        dy = 0
                    elif event.key == pygame.K_UP and dy == 0:
                        dy = -snake_block
                        dx = 0
                    elif event.key == pygame.K_DOWN and dy == 0:
                        dy = snake_block
                        dx = 0

            x += dx
            y += dy

            # 撞牆或撞自己
            if x >= width or x < 0 or y >= height or y < 0:
                game_close = True

            screen.fill(black)
            pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])  # 畫食物
            snake_head = [x, y]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            # 撞到自己
            for block in snake_list[:-1]:
                if block == snake_head:
                    game_close = True

            draw_snake(snake_block, snake_list)
            score_display(length_of_snake - 1)

            pygame.display.update()

            # 吃到食物，生成新的食物
            if x == food_x and y == food_y:
                while [food_x, food_y] in snake_list:
                    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
                    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
                length_of_snake += 1

            clock.tick(snake_speed)

# 啟動遊戲
gameLoop()
