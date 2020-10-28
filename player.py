import pygame

class Piloto(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/fly1.png')
        self.image = pygame.transform.scale(self.image, [90, 80])
        self.rect = pygame.Rect(50, 50, 100, 100)

    def update(self, *args):
        #movimentação do piloto/jogador
        movement = pygame.key.get_pressed()
        if movement[pygame.K_UP]:
            self.rect.y -= 6
        elif movement[pygame.K_DOWN]:
            self.rect.y += 6
        elif movement[pygame.K_LEFT]:
            self.rect.x -= 6
        elif movement[pygame.K_RIGHT]:
            self.rect.x += 6
        #nao ultrapassar a tela
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > 600:
            self.rect.bottom = 600
        elif self.rect.right > 900:
            self.rect.right = 800
        elif self.rect.left <0:
            self.rect.left = 0
