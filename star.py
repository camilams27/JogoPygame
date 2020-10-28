import pygame
import random

class Star(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/star.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(40, 40, 40, 40)

        self.rect.x = 1000 + random.randint(1, 570)
        self.rect.y = random.randint(2, 570)
        #VELOCIDADE
        self.speed = 5
        #estrelas vem aleatoriamente da parte direita da tela
    def update(self, *args):
        self.rect.x -= self.speed
        #caso passe da tela, objeto eh excluido
        if self.rect.right < 0:
            self.kill()



