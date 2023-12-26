import pygame

pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
tela = pygame.display.set_mode(tamanho)
running = True
while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,300), (800,300),2)

    pygame.display.update()
pygame.quit()