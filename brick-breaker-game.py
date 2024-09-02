import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("打砖块")

# 颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 砖块颜色
MACARON_COLORS = [
    (255, 179, 200),  # 深粉红
    (255, 204, 153),  # 橙色
    (255, 230, 153),  # 黄色
    (179, 255, 198),  # 绿色
    (153, 204, 255),  # 蓝色
    (230, 179, 255),  # 紫色
]

# 挡板
paddle_width = 100
paddle_height = 10
paddle = pygame.Rect(width // 2 - paddle_width // 2, height - 20, paddle_width, paddle_height)

# 球
ball_size = 10
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x = 3
ball_speed_y = -3

# 砖块
brick_width = 80
brick_height = 30
bricks = []
for i in range(5):
    for j in range(10):
        brick = pygame.Rect(j * (brick_width + 5) + 5, i * (brick_height + 5) + 5, brick_width, brick_height)
        color = random.choice(MACARON_COLORS)
        bricks.append((brick, color))

# 游戏循环
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 移动挡板
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.right < width:
        paddle.x += 5

    # 移动球
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # 球碰到墙壁
    if ball.left <= 0 or ball.right >= width:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # 球碰到挡板
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # 球碰到砖块
    for brick, color in bricks[:]:
        if ball.colliderect(brick):
            bricks.remove((brick, color))
            ball_speed_y = -ball_speed_y
            break

    # 游戏结束条件
    if ball.bottom >= height:
        running = False

    # 绘制
    screen.fill((230, 230, 230))  # 使用稍深一点的背景色
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick, color in bricks:
        pygame.draw.rect(screen, color, brick)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("游戏结束")
