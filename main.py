import pygame
import random 

pygame.init()
dis_width = 800
dis_height = 600

screen = pygame.display.set_mode([dis_width,dis_height])
pygame.display.set_caption('Coin Collector')

bg_img = pygame.image.load('bg.jpg')
bg_img = pygame.transform.scale(bg_img,(800,800))

sprite = pygame.image.load('sprite.png')
sprite = pygame.transform.scale(sprite,(100,100))

coin =pygame.image.load('coin.png')
coin = pygame.transform.scale(coin,(40,40))

# define sprite dimention and starting position
sprite_width = sprite.get_width()
sprite_height = sprite.get_height()

sprite_x = dis_width//2 - sprite_width//2
sprite_y = dis_height//2 - sprite_height//2

coin_width = coin.get_width()
coin_height = coin.get_height()

coin_x = random.randint(0,dis_width-coin_width)
coin_y = -coin_height

# initializing speed
sprite_speed = 1
coin_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # handle sprite movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_x > 0:
        sprite_x -= sprite_speed
    if keys[pygame.K_RIGHT] and sprite_x < dis_width - sprite_width:
        sprite_x += sprite_speed
    
    #  update the coin position
    coin_y +=coin_speed
    if coin_y > dis_width:
        coin_x = random.randint(0,dis_width- coin_width)
        coin_y =- coin_height
        


    # draw other screens
    screen.blit(bg_img,(0,0))
    screen.blit(sprite,(sprite_x,sprite_y))
    screen.blit(coin,(coin_x,coin_y))

    pygame.display.update()

pygame.quit






