import pygame, sys

pygame.init()

screen_width = 600
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

while True:
    # event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # poaition updating

    # drawing
    




    clock.tick(60)