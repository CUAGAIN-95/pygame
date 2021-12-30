import sys
import pygame
from Screen import Screen
from Player import Player


# 초기화 필수
pygame.init()

# 화면 제목 설정
pygame.display.set_caption("pygame")

# 배경
screen = Screen()
screen.display = pygame.display.set_mode((screen.width, screen.height))

# 캐릭터
player = Player(screen)

# 프레임
clock = pygame.time.Clock()

while True:
    # 프레임 넣기
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.to_x -= player.speed
            elif event.key == pygame.K_RIGHT:
                player.to_x += player.speed
            elif event.key == pygame.K_UP:
                player.to_y -= player.speed
            elif event.key == pygame.K_DOWN:
                player.to_y += player.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.to_y = 0

    player.move(screen, dt)

    screen.display.fill(screen.color)
    pygame.draw.rect(screen.display, player.color, (player.x_pos, player.y_pos, player.width, player.height))
    # 창 새로고침
    pygame.display.update()
