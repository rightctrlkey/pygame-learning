import pygame, sys, time

pygame.init()

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.midtop = (screen_width/2, 0)
    ball_speed_x = 5
    ball_speed_y = 5


def ball_animate():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.bottom >= screen_height:
        time.sleep(0.5)
        ball_reset()


def player_animate():
    global player_speed
    player.x += player_speed

    if player.right >= screen_width:
        player.right = screen_width
    if player.left <= 0:
        player.left = 0

screen_width = 700
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

ball = pygame.Rect(0,0,20,20)
ball.midtop = (screen_width/2, 0)
ball_speed_x = 5
ball_speed_y = 5

player = pygame.Rect(0,0,80,20)
player.midbottom = (screen_width/2, screen_height)
player_speed = 0

while True:
    # event handeling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        keys = pygame.key.get_pressed()
        player_speed = 0
        if keys[pygame.K_LEFT]:
            player_speed = -5
        if keys[pygame.K_RIGHT]:
            player_speed = 5

    if ball.colliderect(player):
            ball_speed_y *= -1    

        

    # poaition updating
    ball_animate()
    player_animate()
    

    # drawing
    window.fill('black')
    pygame.draw.rect(window, (255,255,255), player, border_radius=10)
    pygame.draw.ellipse(window, (255,255,255), ball)
    

    pygame.display.update()
    clock.tick(60)