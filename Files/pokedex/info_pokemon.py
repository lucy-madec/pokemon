from Files.pygame.global_def import Global
import pygame

class Info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.info_running = True
        
    def pikachu(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex1b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def capumain(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex2b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def evoli(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex3b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def marcacrin(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex4b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def salameche(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex5b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def medhyena(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex6b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def tiplouf(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex7b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def caninos(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex8b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    #Information pokémon ADD
    def etourvol(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex208.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def lainergie(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex212.png')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def floravol(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex209.png')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def luxio(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex214.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def magicarpe(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex213.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def phanpy(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex215.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
                
    def psykokwak(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex210.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        
    def roudoudou(self):
        background = pygame.image.load(r'images\images-pokedex\pokedex211.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()                        

    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
    
    def info_pokemon_run(self):
        self.button_add()
        while self.info_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.info_running = False
                elif self.is_mouse_over_button(pygame.Rect(540, 10, 70, 25)):
                    # Vérifie si le bouton gauche de la souris est cliqué
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        print("but add")
                        # self.add_pokemon()
                    if self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):                      
                        # self.info_running = False
                        self.read_json("etourvol")
            pygame.display.flip()


