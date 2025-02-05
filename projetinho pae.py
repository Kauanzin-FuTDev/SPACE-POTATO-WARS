import pygame
from random import randint
from random import Random
from time import sleep

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600 , 900 ))

pygame.display.set_caption("SPACE POTATO WARS")


shot_Scoop = False

enimy_x = 230
enimy_y = 100
speed_enimy = 8

#shoots
x_shoot = 30
y_shoot = 30
speed_y_shoot = 30

shoot = []

Score = 0



#Imagens e sonds
potatoImg_Player = pygame.image.load("D:\progaming\Pygame\Baked_Potato_JE4_BE2.webp")
BackImg = pygame.image.load("D:\progaming\Pygame\quadrodecorativoretangularplanetaterraspaceazul.webp")
enimyPotatoImg = pygame.image.load("D:\progaming\Pygame\Poisonous_Potato_JE3_BE2.webp")
shootImg = pygame.image.load("D:\progaming\Pygame\pngtree-golden-yellow-fast-food-potato-fries-png-image_2707911.jpg")
shootImg = pygame.transform.scale( shootImg, (30,30)) #Mudando a escala 
sondOfShoot = pygame.mixer.Sound("D:/progaming/Pygame/sound-effects-single-gun-shot-247124.mp3")









#POSITION 
player_x = 230
player_y = 700

#Movimatation
speed_player = 10
clock = pygame.time.Clock()


#Enimy movimatation
enimy_x += 10







running = True
while running:


    for event in pygame.event.get():       #fechar o pygame
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #key movimatation
    if keys[pygame.K_UP]:
     player_y -= speed_player
    if keys[pygame.K_DOWN]:
        player_y += speed_player
    if keys[pygame.K_LEFT]:
        player_x -= speed_player
    if keys[pygame.K_RIGHT]:
        player_x += speed_player

    #Enimy movimatation
    enimy_y += 2

    if enimy_y > 800:
        random_x = randint(-22,450)
        random_y = randint(-50,-30)
        
        enimy_y = random_y
        enimy_x = random_x
    
    
    if keys[pygame.K_SPACE] and not shot_Scoop:  
     shot_Scoop = True
     sondOfShoot.play()  
     y_shoot = player_y
     x_shoot = player_x
     shoot.append([player_x + 20, player_y])

    for missile in shoot:
        missile[1] -= speed_y_shoot  # Move o tiro para cima
        screen.blit(shootImg, (missile[0], missile[1]))  # Desenha o tiro







 # Restringir jogador aos limites da tela
    if player_y <= -30:
        player_y = -30

    if player_y >= 751:
        player_y = 751

    if player_x <= -22:
        player_x = -22

    if player_x >= 450:
        player_x = 450




    screen.blit(BackImg , (0 , 0))
    screen.blit(potatoImg_Player , (player_x , player_y))
    screen.blit(enimyPotatoImg , (enimy_x,enimy_y))
    
    pygame.display.flip()



    print(player_y)
    clock.tick(60) #FPS



pygame.quit()






    



