#Importation de pygame
import pygame
#Initialisation de pygame(PG)
pygame.init()

#Créer une fenêtre pour afficher le jeu
window = pygame.display.set_mode((800, 600))
# Modifier le titre et l'icône
pygame.display.set_caption("Thanos PyGame")
windowIcon =pygame.image.load("alien.png")
pygame.display.set_icon(windowIcon)

# Ob charge k'image du joueur
player = pygame.image.load("player.png")
playerRect = player.get_rect()
# Position du joueur à l'écran
posX = 350
posY = 480
# Image Background
bg = pygame.image.load("bg.png")


# La boucle de jeu
running = True
while running:
    # Couleur de l'écran
    window.fill((0,0,0))
    #BG
    window.blit(bg, (0, 0))
    # Je check tous les événements (clavier/souris)
    for event in pygame.event.get():
        # Est-ce que l'utilisateur clique sur la crois de la fenetre
        pressed = pygame.key.get_pressed()
        # On teste si l'utilisateur clique sur la croix
        if event.type ==pygame.QUIT:
            # On quitte le jeu
            running = False
        #On teste les flèches du clavier
        # if event.type == pygame.KEYDOWN:
        #     # De quelle touche sa'git-il
        #     if event.key ==pygame.K_LEFT:
        #         posX -= 50
        #     if event.key == pygame.K_RIGHT:
        #         #le joueur a appuyé sur la touche flèche gauche
        #         posX += 50
    # Gestion du déplacement du joueur à l'écran
    if pressed[pygame.K_LEFT]: posX -= 2
    if pressed[pygame.K_RIGHT]: posX += 2

    # Affichage joueurgit
    # On applque cette position au rectangle
    playerRect.topleft = (posX, posY)
    # On a affiche l'image du joueur dans la fenêtre du jeu
    window.blit(player, playerRect)
    # On dessine/ mettre à jour le contenu de l'écran
    pygame.display.flip()
# Quitter pygame
pygame.quit()