from global_def import Global
import pygame,sys

class Pokemon(Global):

    def __init__(self):
        Global.__init__(self)
    
    def background(self):
        self.img_back("Background", "images/images-partie/pokedex105.jpg")

    def button_quit(self):
        # Récupérer la largeur de l'écran
        screen_width = self.screen.get_width()

        # Dimensions du rectangle
        rect_width = 200
        rect_height = 100

        # Coordonnées du rectangle
        rect_x = screen_width - rect_width - 50
        rect_y = 50

        # Afficher le rectangle
        self.rect_radius(10, self.white, rect_x, rect_y, rect_width, rect_height)

        # Afficher le texte "QUIT" au centre du rectangle
        text_x = rect_x + (rect_width - self.police_c1.size("QUIT")[0]) // 2
        text_y = rect_y + (rect_height - self.police_c1.size("QUIT")[1]) // 2
        self.text_c1("QUIT", self.black, text_x, text_y)
    
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