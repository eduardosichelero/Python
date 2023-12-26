import pygame
import winsound
import random
pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
clock = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
running = True
direita = True
posicaoXbolinha = 0
velocidadebolinha = 1
posicaoYbolinha = 300
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False

    tela.fill(branco)
    pygame.draw.circle(tela,preto,(posicaoXbolinha,posicaoYbolinha),30)

    if posicaoXbolinha >= 800:
        direita = False
        velocidadebolinha = velocidadebolinha +1
        posicaoYbolinha = random.randint(0,600)
        winsound.Beep(500,300)
    elif posicaoXbolinha <=0:
        direita = True
        velocidadebolinha = velocidadebolinha +1
    
    if direita: 
        posicaoXbolinha = posicaoXbolinha + velocidadebolinha
    else: 
        posicaoXbolinha = posicaoXbolinha - velocidadebolinha
    
        pygame.draw.line(tela,preto,(30,30), (100,300),2)


    pygame.display.update()
    clock.tick(60)
pygame.quit()