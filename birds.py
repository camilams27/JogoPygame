import pygame

class birds(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bird1.png")
        self.image = pygame.transform.scale(self.image, [90, 90])
        self.rect = pygame.Rect(500, 500, 400, 400)

        # self.image = pygame.image.load("data/bird2.png")
        # self.image = pygame.transform.scale(self.image, [90, 90])
        # self.rect = pygame.Rect(600, 600, 500, 500)

        self.speed = 5

    def update(self, *args):
        # movimento dos passaros
        self.rect.x-=self.speed

