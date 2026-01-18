import pygame,sys

pygame.init()

circle_x = 20
circle_y = 150
circle_radius = 10
circle_x_speed = 0
circle_y_speed = 0

window = pygame.display.set_mode((300,300))
pygame.display.set_caption('My first pygame project')
clock = pygame.time.Clock()

# game loop
while True:

    # 1 Event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                circle_y_speed = -1
            if event.key == pygame.K_DOWN:
                circle_y_speed = 1
            if event.key == pygame.K_RIGHT: 
                circle_x_speed = 1
            if event.key == pygame.K_LEFT: 
                circle_x_speed = -1

    # 2 Updating positions
    circle_x += circle_x_speed
    circle_y += circle_y_speed


    # 3 Drawing
    window.fill((140,200,0))
    pygame.draw.circle(window, (255,255,255), (circle_x,circle_y), circle_radius)




    pygame.display.update()
    clock.tick(60)