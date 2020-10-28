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
        #velocidade do objeto
        self.speed = 5
        #passaros vermelhos vem de Lugares aleatorios na parte direita da tela
    def update(self, *args):
        self.rect.x -= self.speed
        #caso passe da tela, objeto eh excluido
        if self.rect.right < 0:
            self.kill()



