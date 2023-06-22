
#__version__ = “1.0.3”
import pygame
pygame.init()
fenster = pygame.display.set_mode([1100,700])
running = True


pic = pygame.image.load("assets/player.png")
back = pygame.image.load("assets/back.png")
back = pygame.transform.scale(back, (1100, 700))
pic = pygame.transform.scale(pic, (80, 120))


picx = 0
picy = 0
flip = False

timer = pygame.time.Clock()





while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False



    fenster.blit(back, (0, 0))
    fenster.blit(pygame.transform.flip(pic, flip, False), (picx, picy))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            picy = picy + 6
            picx = picx + 20

    pygame.display.update()

    timer.tick(60)

pygame.quit()