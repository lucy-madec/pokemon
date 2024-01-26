# Test
from global_def import Global
import pygame
class Bag(Global):
    def __init__(self): 
            Global.__init__(self)
        
    # Initialisation de Pygame
    pygame.init()
    # Afficher background
    def background(self):
        self.img_back("background", r"images/images-play/Play12.png")

    def rect(self):
        self.rect_radius(10,self.white,10,400,70,460)
    
    def text(self):
        self.text_c5("Sorry !",self.black, 250, 350)
        self.text_c6("There are no items available in the bag...", self.black, 250, 360)

    def bag_run(self):
    # # Définition de la taille de la fenêtre
    #     largeur, hauteur = 800, 600
    #     taille_fenetre = (largeur, hauteur)
    #     fenetre = pygame.display.set_mode(taille_fenetre)
    
    
        

        # Boucle principale
        en_cours = True
        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            # Remplir la fenêtre avec la couleur gris
            # self.screen(self.orange)
            self.background()
            self.rect()
            self.text()

            # Mettre à jour l'affichage
            pygame.display.flip()

        # Quand la boucle est terminée, quitter Pygame
    pygame.quit()

test = Bag()
test.bag_run()