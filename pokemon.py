from global_def import Global
import pygame
import sys

class Pokemon(Global):

    def __init__(self):
        Global.__init__(self)

    def background(self):
        self.img_back("Background", "images/images-partie/pokedex105.jpg")

    def button_quit(self):
        self.rect_radius(10, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    def button_back(self):
        self.rect_radius(10, self.white, 700, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)

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