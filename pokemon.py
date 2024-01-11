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
        self.rect_radius(10, self.white, 10, 10, 70, 25)
        self.text_c1("BACK", self.black, 733, 13)

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Check if the left mouse button is clicked
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        self.running = False

            self.background()
            self.button_quit()
            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()

game = Pokemon()
game.run()