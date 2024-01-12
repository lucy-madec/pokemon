from Archive_Pokedex.global_def import Global
import pygame
class Play1(Global):
    def __init__(self): 
            Global.__init__(self)
    # Initialisation de Pygame
    pygame.init()
    def affichage(self):
    # Définition de la taille de la fenêtre
        largeur, hauteur = 800, 600
        taille_fenetre = (largeur, hauteur)
        fenetre = pygame.display.set_mode(taille_fenetre)

        # Définition de la couleur gris


        # Boucle principale
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            # Remplir la fenêtre avec la couleur gris

            # Mettre à jour l'affichage
            pygame.display.flip()

    # Quand la boucle est terminée, quitter Pygame
    pygame.quit()

test1 = Play1()
test1.affichage()