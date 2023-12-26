import pygame

pygame.init()
tamanho = (800,600)
branco = (255,255,255)
preto = (0,0,0)
tela = pygame.display.set_mode(tamanho)
running = True
posicaoXbolinha = 400
posicaoYbolinha = 300

while running:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False

    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,600), (800,0),2)
    pygame.draw.circle(tela,preto,(posicaoXbolinha,posicaoYbolinha),60)
    pygame.draw.circle(tela,branco,(posicaoXbolinha,posicaoYbolinha),58)
    



    pygame.display.update()
pygame.quit()