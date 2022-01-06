from pathlib import Path
import sys
import pygame
from Screen import Screen
from Unit import Player


# 초기화 필수
pygame.init()

# 화면 제목 설정
pygame.display.set_caption("pygame_pang")

# 이미지 경로
image_path = Path.joinpath(Path.cwd(), "images")

# 배경
screen = Screen(image_path)

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

    screen.display.blit(screen.background_image, (0, 0))
    screen.display.blit(screen.stage_image, (0, screen.height - screen.stage_height))
    pygame.draw.rect(screen.display, player.color, (player.x_pos, player.y_pos, player.width, player.height))
    # 창 새로고침
    pygame.display.update()
