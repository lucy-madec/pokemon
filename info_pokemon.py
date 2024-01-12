from Archive_Pokedex.global_def import Global
import pygame

class info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)

    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
    
    def button_back(self):
        self.rect_radius(10, self.white, 640, 10, 70, 25)
        self.text_c1("BACK", self.black, 650, 13)

    def pikachu_run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.pikachu()
            pygame.display.flip()
        pygame.quit()

