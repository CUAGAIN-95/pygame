# screen의 기본 데이터를 저장하는 클래스
import pygame


class Screen:
    def __init__(self, image_path):
        self.width = 640
        self.height = 480
        self.display = pygame.display.set_mode((self.width, self.height))
        self.background_image = pygame.image.load(image_path / "background.jpg")

        self.stage_image = pygame.image.load(image_path / "stage.jpg")
        self.stage_size = self.stage_image.get_rect().size
        self.stage_width = self.stage_size[0]
        self.stage_height = self.stage_size[1]

    def __del__(self):
        pass
