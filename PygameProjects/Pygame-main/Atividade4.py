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
        elif evento.type == pygame.KEYDOWN and evento.key== pygame.K_ESCAPE:
            running = False

    tela.fill(branco)
    pygame.draw.line(tela,preto,(0,300), (800,300),2)
    pygame.draw.line(tela,preto,(70,70), (70,450),2)
    pygame.draw.line(tela,preto,(70,70), (170,370),2)
    pygame.draw.line(tela,preto,(170,370), (200,150),2)
    pygame.draw.line(tela,preto,(200,150), (250,400),2)
    pygame.draw.line(tela,preto,(255,400), (400,50),2)
    pygame.draw.line(tela,preto,(400,50), (700,400),2)
    pygame.display.update()
pygame.quit()