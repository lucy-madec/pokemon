import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
blanc = (255, 255, 255)
gris = (192, 192, 192)

# Paramètres du tableau
largeur_cellule = 100
hauteur_cellule = 50
nb_lignes = 7
largeur_tableau = largeur_cellule
hauteur_tableau = hauteur_cellule * nb_lignes

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur_tableau, hauteur_tableau))
pygame.display.set_caption("Tableau Pygame")

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Effacer l'écran
    fenetre.fill(blanc)

    # Dessiner les bordures du tableau
    pygame.draw.rect(fenetre, gris, (0, 0, largeur_tableau, hauteur_tableau), 1)

    # Dessiner les cellules fusionnées
    for i in range(nb_lignes):
        pygame.draw.rect(fenetre, gris, (0, i * hauteur_cellule, largeur_tableau, hauteur_cellule), 1)

    # Mettre à jour l'affichage
    pygame.display.flip()
