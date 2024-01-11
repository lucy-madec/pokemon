from global_def import Global
import pygame
class Add_pokemon1(Global):
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
        couleur_gris = (150, 150, 150)  # RGB

        # Boucle principale
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            # Remplir la fenêtre avec la couleur gris
            fenetre.fill(couleur_gris)

            # Mettre à jour l'affichage
            pygame.display.flip()

        # Quand la boucle est terminée, quitter Pygame
    pygame.quit()
    
test1 = Add_pokemon1()
test1.affichage()