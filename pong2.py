import pygame, sys, time

pygame.init()

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.midtop = (screen_width/2, 0)
    ball_speed_x = 5
    ball_speed_y = 5


def ball_animate():
    global ball_speed_x, ball_speed_y, points
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
    if ball.bottom >= screen_height:
        points += 1
        time.sleep(0.5)
        ball_reset()


def player_animate():
    global player_speed
    player.x += player_speed

    if player.right >= screen_width:
        player.right = screen_width
    if player.left <= 0:
        player.left = 0

def score():
    lives = 3 - points

    if lives >= 1:
        window.blit(heart1, (5, 5))
    if lives >= 2:
        window.blit(heart2, (30, 5))
    if lives >= 3:
        window.blit(heart3, (55, 5))

    if lives <= 0:
        pygame.quit()
        sys.exit()


screen_width = 700
screen_height = 500
window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aman's Pong Game")
clock = pygame.time.Clock()

heart = pygame.image.load('Graphics/heart.png').convert_alpha()
heart1 = pygame.transform.scale(heart, (35,35))
heart2 = pygame.transform.scale(heart, (35,35))
heart3 = pygame.transform.scale(heart, (35,35))

ball = pygame.Rect(0,0,20,20)
ball.midtop = (screen_width/2, 0)
ball_speed_x = 5
ball_speed_y = 5
points = 0

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
            ball.bottom = player.top
            ball_speed_y *= -1    

        

    # poaition updating
    ball_animate()
    player_animate()
    
    

    # drawing
    window.fill('black')
    score()
    pygame.draw.rect(window, (255,255,255), player, border_radius=10)
    pygame.draw.ellipse(window, (255,255,255), ball)
    
    

    pygame.display.update()
    clock.tick(60)