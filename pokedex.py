import pygame
import sys

pygame.init()

# Paramètres
largeur_fenetre = 800
hauteur_fenetre = 600
taille_image = 100

# Initialisation de la fenêtre
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Défilement d'images")

# Chargement des images
images = [
    pygame.image.load("images\images-pokedex\pokedex107.png"),
    pygame.image.load("images\images-pokedex\pokedex106.png"),
    pygame.image.load("images\images-pokedex\pokedex108.png"),
    # Ajoutez autant d'images que nécessaire
]

# Position initiale
position_x = 0

# Boucle principale
clock = pygame.time.Clock()  # Ajout d'une horloge pour réguler la vitesse
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Défilement vers la droite
                position_x += taille_image

    # Affichage des images
    fenetre.fill((255, 255, 255))  # Fond blanc
    for image in images:
        fenetre.blit(image, (position_x, hauteur_fenetre // 2 - taille_image // 2))
        position_x += taille_image

    position_x = 0  # Réinitialise la position_x après avoir affiché toutes les images

    pygame.display.flip()
    clock.tick(30)  # Limite la vitesse à 30 images par seconde
