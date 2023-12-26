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
    pygame.draw.line(tela,preto,(78,78), (250,390),3)
    pygame.draw.circle(tela,preto,(90,90),40)
    pygame.draw.circle(tela,branco,(90,90),37)
    
    pygame.draw.line(tela,preto,(280,370),(450,285),3)
    pygame.draw.circle(tela,preto,(250,390),40)
    pygame.draw.circle(tela,branco,(250,390),37)
    
    pygame.draw.line(tela,preto,(400,270),(650,245),3)
    pygame.draw.circle(tela,preto,(440,265),40)
    pygame.draw.circle(tela,branco,(440,265),37)

    pygame.draw.circle(tela,preto,(650,245),40)
    pygame.draw.circle(tela,branco,(650,245),37)



    
    
    pygame.display.update()
pygame.quit()
