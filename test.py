import pygame

# Initialisation de Pygame
pygame.init()

# Définition de la taille de la fenêtre
largeur, hauteur = 800, 600
taille_fenetre = (largeur, hauteur)

# Création de la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Fenêtre Pygame")

# Couleur blanche en RGB
blanc = (255, 255, 255)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplir la fenêtre avec la couleur blanche
    fenetre.fill(blanc)

    # Rafraîchir l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()