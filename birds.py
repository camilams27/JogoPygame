import pygame
import random

class Birds(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bird1.png")
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = pygame.Rect(200, 400, 400, 400)

        self.rect.x = 1000 + random.randint(1, 570)
        self.rect.y = random.randint(2, 570)

        self.speed = 5

    def update(self, *args):
        # movimento dos passaros
        self.rect.x -= self.speed

        if self.rect.right < 0:
            self.kill()



