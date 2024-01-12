from global_def import Global
# from pokedex import Pokedex Voir RYMA
import pygame

class Info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        # self.pokedex = Pokedex()
    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()
    def capumain(self):
        background = pygame.image.load('images\images-pokedex\pokedex2b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def evoli(self):
        background = pygame.image.load('images\images-pokedex\pokedex3b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def marcacrin(self):
        background = pygame.image.load('images\images-pokedex\pokedex4b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def salameche(self):
        background = pygame.image.load('images\images-pokedex\pokedex5b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def medhyena(self):
        background = pygame.image.load('images\images-pokedex\pokedex6b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def tiplouf(self):
        background = pygame.image.load('images\images-pokedex\pokedex7b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def caninos(self):
        background = pygame.image.load('images\images-pokedex\pokedex8b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))





    def etourvol(self):
        background = pygame.image.load('images\images-pokedex\pokedex208.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def lainergie(self):
        background = pygame.image.load('images\images-pokedex\pokedex212.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))

    def floravol(self):
        background = pygame.image.load('images\images-pokedex\pokedex209.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))

    def luxio(self):
        background = pygame.image.load('images\images-pokedex\pokedex214.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))

    def magicarpe(self):
        background = pygame.image.load('images\images-pokedex\pokedex213.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def phanpy(self):
        background = pygame.image.load('images\images-pokedex\pokedex215.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
    def psykokwak(self):
        background = pygame.image.load('images\images-pokedex\pokedex210.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))

    def rondoudou(self):
        background = pygame.image.load('images\images-pokedex\pokedex211.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        
        
    def button_back(self):
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("BACK", self.black, 733, 13)
        pygame.display.update()
        pygame.display.flip()
    

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

