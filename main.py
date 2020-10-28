import pygame

import random

#classe dos passaros
from birds import Birds
from bluebirds import Blue
from player import Piloto
from star import Star

pygame.init()

#grupo de desenho e passaros
drawGroup = pygame.sprite.Group()
birdsGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()
starGroup = pygame.sprite.Group()

#tela e imagens
tela = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("jogo")
papel = pygame.sprite.Sprite(drawGroup)
papel.image = pygame.image.load("data/BG.png")
papel.image = pygame.transform.scale(papel.image, [1000, 600])
papel.rect = papel.image.get_rect()

#piloto e passaros
player = Piloto(drawGroup)
bird1 = Birds(drawGroup)
bird2 = Blue(drawGroup)
estrela = Star(drawGroup)

#pontos do jogo
fonte = pygame.font.SysFont('roboto', 40, True, False)
pontos = 0

#gameover
font = pygame.font.SysFont('roboto', 40, True, False)

#musica e sons
musica = pygame.mixer.music.load("data/ambiente.ogg")
pygame.mixer.music.set_volume(0.08)
pygame.mixer.music.play(-1)

estrelinha = pygame.mixer.Sound("data/coin.wav")
gameO = pygame.mixer.Sound("data/gameover.wav")

tempo = 20
relogio = pygame.time.Clock()


gameLoop = True
gameover = False
while gameLoop:
    relogio.tick(50)
    #pontos
    mensagem = f'Pontos: {pontos}'
    texto = fonte.render(mensagem, True, (0,0,0))
    #gameover
    mensage = f'Game Over!'
    text = fonte.render(mensage, True, (255, 0, 0))

    drawGroup.draw(tela)
    #sair do jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    if not gameover:

        drawGroup.update()

        tempo += 1
        if tempo > 2:
            tempo =0
        if random.random() < 0.01:
            newbird = Birds(drawGroup, birdsGroup)
            novopass = Blue(drawGroup, birdsGroup)

        elif tempo > 1:
            if random.random() < 0.10:
                newstar = Star(drawGroup, starGroup)

        #colisão do jogador com a estrela
        star = pygame.sprite.spritecollide(player, starGroup, True, pygame.sprite.collide_mask)
        if star:
            estrelinha.play()
            pontos += 1
            #
        collisions = pygame.sprite.spritecollide(player, birdsGroup, False, pygame.sprite.collide_mask)
        if collisions:
            gameover = True
            pygame.mixer.music.set_volume(0.00)
            gameO.play()
            tela.blit(text, (400,300))
            print("bateu")

        # pontos
        tela.blit(texto, (800, 25))

        pygame.display.update()
