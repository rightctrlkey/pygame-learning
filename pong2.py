import pygame, sys

pygame.init()

screen_width = 600
screen_height = 600
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ball = pygame.Rect(0,0,20,20)
ball.midtop = (screen_width/2, 0)

player = pygame.Rect(0,0,80,20)
player.midbottom = (screen_width/2, screen_height)

while True:
    # event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    # poaition updating

    # drawing
    pygame.draw.rect(window, (255,255,255), player, border_radius=10)
    pygame.draw.ellipse(window, (255,255,255), ball)
    


    pygame.display.update()
    clock.tick(60)