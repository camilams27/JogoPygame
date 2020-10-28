import pygame
import random

class Blue(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bird2.png")
        self.image = pygame.transform.scale(self.image, [70, 70])
        self.rect = pygame.Rect(100, 100, 100, 100)

        self.rect.x = 1000 + random.randint(1, 570)
        self.rect.y = random.randint(2, 570)
        #velocidade altera durante o percuso
        self.speed = 3 + random.random()*2
    #passaros azuis vem de lugares aléatórios da parte direita da tela
    def update(self, *args):
        self.rect.x -= self.speed
        #caso passe da tela, objeto eh excluido
        if self.rect.right < 0:
            self.kill()







