import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()



all_sprites = pygame.sprite.Group()

#game loop

running = True
while running:
    
    #keep running at right speed
    clock.tick(FPS)

    #process input (events)
    for event in pygame.event.get():
        #check for close x
        if (event.type == pygame.QUIT):
            running = False
    #update
    all_sprites.update()
    
    #draw/render
    screen.fill((BLACK))
    all_sprites.draw(screen)

    #after drawing flip the display
    pygame.display.flip()

pygame.quit()
