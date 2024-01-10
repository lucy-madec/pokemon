from global_def import Global
import pygame
import sys

class Pokemon(Global):

    def __init__(self):
        Global.__init__(self)

    def background(self):
        self.img_back("Background", "images/images-partie/pokedex105.jpg")

    def button_quit(self):
        # Récupérer la largeur de l'écran
        screen_width = self.screen.get_width()

        # Dimensions du rectangle (plus petit et allongé en largeur)
        rect_width = 40
        rect_height = 20

        # Coordonnées du rectangle
        rect_x = screen_width - rect_width - 10
        rect_y = 10

        # Récupérer les coordonnées de la souris
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Vérifier si la souris est sur le rectangle
        if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
            # Agrandir le rectangle symétriquement en fonction de la position de la souris
            enlargement_factor = 1.5  # Facteur d'agrandissement
            rect_width = int(rect_width * enlargement_factor)
            rect_height = int(rect_height / enlargement_factor)

            # Ajuster les coordonnées pour rester dans le cadre du programme
            rect_x = screen_width - rect_width - 10
            rect_y = 10

        # Afficher le rectangle
        self.rect_radius(10, self.white, rect_x, rect_y, rect_width, rect_height)

        # Afficher le texte "QUIT" au centre du rectangle
        text_x = rect_x + (rect_width - self.police_c1.size("QUIT")[0]) // 2
        text_y = rect_y + (rect_height - self.police_c1.size("QUIT")[1]) // 2
        self.text_c1("QUIT", self.black, text_x, text_y)

        # Vérifier si un bouton de la souris est enfoncé
        mouse_click = pygame.mouse.get_pressed()
        if mouse_click[0] == 1:  # Clic gauche
            pygame.quit()
            sys.exit()

    

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.background()
            self.button_quit()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

game = Pokemon()
game.run()