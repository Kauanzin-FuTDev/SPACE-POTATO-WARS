import pygame
from random import randint

# Inicialização do pygame
pygame.init()
pygame.mixer.init()

# Configurações da tela
WIDTH, HEIGHT = 600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE POTATO WARS")

# Variáveis de controle
shot_Scoop = False
enimy_x = randint(50, 500)
enimy_y = 100
speed_enimy = 2
speed_y_shoot = 20
shoot = []
score = 0

# Configuração do tempo limite
TEMPO_LIMITE = 2000  # 2 segundos
EVENTO_PARAR_SOM = pygame.USEREVENT + 1  # Criar evento personalizado para parar o som

# Posições iniciais do jogador
player_x = 230
player_y = 700
speed_player = 10

# Carregamento de imagens e sons
potatoImg_Player = pygame.image.load("D:/progaming/space-potato-wars/Baked_Potato_JE4_BE2.webp")
BackImg = pygame.image.load("D:/progaming/space-potato-wars/quadrodecorativoretangularplanetaterraspaceazul.webp")
enimyPotatoImg = pygame.image.load("D:/progaming/space-potato-wars/Poisonous_Potato_JE3_BE2.webp")
shootImg = pygame.image.load("D:/progaming/space-potato-wars/pngtree-golden-yellow-fast-food-potato-fries-png-image_2707911.jpg")
shootImg = pygame.transform.scale(shootImg, (60, 60))

sondOfShoot = pygame.mixer.Sound("D:/progaming/space-potato-wars/depositphotos_430790386-track-sound-food-sizzle-oil-french.mp3")
background_music = pygame.mixer.Sound("D:/progaming/space-potato-wars/pad-space-travel-hyperdrive-engine-humming-235901.mp3")

# Iniciar música de fundo (repetindo infinitamente)
background_music.play(-1)

# Relógio do jogo
clock = pygame.time.Clock()

# Loop principal
running = True
while running:
    screen.blit(BackImg, (0, 0))  # Atualiza o fundo

    # Captura eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Parar o som após 2 segundos
        elif event.type == EVENTO_PARAR_SOM:
            sondOfShoot.stop()
            pygame.time.set_timer(EVENTO_PARAR_SOM, 0)  # Cancela o timer para evitar repetições

    # Movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]: player_y -= speed_player
    if keys[pygame.K_DOWN]: player_y += speed_player
    if keys[pygame.K_LEFT]: player_x -= speed_player
    if keys[pygame.K_RIGHT]: player_x += speed_player

    # Limitar o jogador à tela
    player_x = max(-22, min(player_x, 450))
    player_y = max(-30, min(player_y, 751))

    # Movimento do inimigo
    enimy_y += speed_enimy
    if enimy_y > HEIGHT:
        enimy_x = randint(50, 500)
        enimy_y = randint(-100, -30)

    # Disparo do jogador
    if keys[pygame.K_SPACE] and not shot_Scoop:
        shot_Scoop = True
        sondOfShoot.play()
        pygame.time.set_timer(EVENTO_PARAR_SOM, TEMPO_LIMITE)  # Iniciar timer para parar o som
        shoot.append([player_x + 20, player_y])

    # Atualizar posição dos tiros
    for missile in shoot[:]:  # Criar uma cópia para evitar erros de remoção
        missile[1] -= speed_y_shoot
        if missile[1] < -30:
            shoot.remove(missile)  # Remove tiros que saíram da tela

    # Redefinir a possibilidade de atirar após um intervalo
    if not keys[pygame.K_SPACE]:
        shot_Scoop = False

    # Desenhar jogador, inimigo e tiros
    screen.blit(potatoImg_Player, (player_x, player_y))
    screen.blit(enimyPotatoImg, (enimy_x, enimy_y))
    for missile in shoot:
        screen.blit(shootImg, (missile[0], missile[1]))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

    



