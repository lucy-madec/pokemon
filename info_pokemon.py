from Archive_Pokedex.global_def import Global
# from pokedex import Pokedex
import pygame

class Info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        # self.pokedex = Pokedex()
    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def posipi(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def evoli(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def marcacrin(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def salameche(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def medhyena(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def tiplouf(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def caninos(self):
        background = pygame.image.load('images\images-pokedex\pokedex1070.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()

    def button_back(self):
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("BACK", self.black, 733, 13)
        pygame.display.update()
        pygame.display.flip()
        
    def button_back(self):
        self.rect_radius(10, self.white, 640, 10, 70, 25)
        self.text_c1("BACK", self.black, 650, 13)

    def info_pokemon_run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(720, 10, 70, 25)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.pokedex.pokedex_run()
                        running = False

            pygame.display.flip()
        pygame.quit()

