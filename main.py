#Importation de random
import random
#Importation de pygame
import pygame
#Initialisation de pygame(PG)
from pygame import mixer
pygame.init()

#Créer une fenêtre pour afficher le jeu
window = pygame.display.set_mode((800, 600))

# Modifier le titre et l'icône
pygame.display.set_caption("Thanos PyGame")
windowIcon =pygame.image.load("alien.png")
pygame.display.set_icon(windowIcon)

# On charge l'image du joueur
player = pygame.image.load("player.png")
playerRect = player.get_rect()

# Position du joueur à l'écran
posX = 350
posY = 480
# Image Background
bg = pygame.image.load("bg.png")
playerSpeed = 5

# Le laser
laser = pygame.image.load("laser.png")
laserRect = laser.get_rect()
laserSpeed = 4
posLaserX = 0
posLaserY = -100
canShoot = True

# L'Ovni
# ovni = pygame.image.load("ufo.png")
# ovniRect = ovni.get_rect()
# ovniSpeed = 3
# posOvniX = random.randint(1, 750)
# posOvniY = 50

ovni =[] # Images
ovniRect = [] # Rect
posOvniX =[] # pos X
posOvniY = [] # pos Y
ovniSpeed = [] # tableau des vitesses
nbOvni = 4

# Texte
score = 0
font = pygame.font.Font("future.ttf", 36)
txtPos = 10

# Musique
# mixer.music.load("maMusique.wav")
# mixer.music.play(-1)

# Boucle de génération des monstres
for i in range(nbOvni):
    ovni.append(pygame.image.load("ufo.png"))
    ovniRect.append(ovni[i].get_rect())
    posOvniX.append(random.randint(1, 750))
    posOvniY.append(random.randint(10, 300))
    ovniSpeed.append(3)


# Fonction de détection de collision
def collision(rectA, rectB):
    if rectB.right < rectA.left:
        # rectB est à gauche
        return False
    if rectB.bottom < rectA.top:
        # rectB est au-dessus
        return False
    if rectB.left > rectA.right:
        # rectB est à droite
        return False
    if rectB.top > rectA.bottom:
        # rectB est en-dessous
        return False
    # Dans tous les autres cas il y a collision
    return True

# Pour définir le FPS
clock = pygame.time.Clock()

# La boucle de jeu
running = True
while running:
    # Couleur de l'écran
    window.fill((0,0,0))
    #Background
    window.blit(bg,(0, 0))
    # Je check tous les événements (clavier/souris)
    for event in pygame.event.get():
        # Est-ce que l'utilisateur clique sur la crois de la fenetre
        pressed = pygame.key.get_pressed()
        # On teste si l'utilisateur clique sur la croix
        if event.type ==pygame.QUIT:
            # On quitte le jeu
            running = False
        # Détection barre espace pour tirer le laser
        if event.type == pygame.KEYDOWN:
            # De quelle touche sa'git-il
            if event.key == pygame.K_SPACE and canShoot:
                laserSfx = mixer.Sound("sfx_laser.ogg")
                laserSfx.play()
                canShoot = False
                posLaserX = posX + 45
                posLaserY = posY - 50

    # Gestion du déplacement du joueur à l'écran
    if pressed[pygame.K_LEFT] and posX > 0:
        posX -= playerSpeed
    if pressed[pygame.K_RIGHT] and posX < 700:
        posX += playerSpeed

    # Affichage joueur
    # On applque cette position au rectangle
    playerRect.topleft = (posX, posY)
    # On a affiche l'image du joueur dans la fenêtre du jeu
    window.blit(player, playerRect)

    # Gestion du laser
    posLaserY -= laserSpeed
    laserRect.topleft = (posLaserX, posLaserY)
    window.blit(laser, laserRect)
    if posLaserY < -40:
        canShoot = True

    # Gestion des Ovnis
    for i in range(nbOvni):
        posOvniX[i] -= ovniSpeed[i]
        ovniRect[i].topleft = (posOvniX[i], posOvniY[i])
        window.blit(ovni[i], ovniRect[i])
        if posOvniX[i] < 0 or posOvniX[i] > 750:
            ovniSpeed[i] = -ovniSpeed[i]
            posOvniY[i] += 50

        # Y a t-il collision entre le laser et l'ovni
        if collision(laserRect, ovniRect[i]):
            posOvniY[i] = 10000
            posLaserY = -500
            score += 1

        # Y a t-il collision entre l'ovni et le joueur
        if collision(playerRect, ovniRect[i]):
            posX = -500

    # Affichage du score
    scoreTxt = font.render("score : " + str(score), True, (255, 255, 255))
    window.blit(scoreTxt, (txtPos, txtPos))

    # On dessine/ mettre à jour le contenu de l'écran
    pygame.display.flip()
    clock.tick(60)
# Quitter pygame
pygame.quit()