from global_def import Global
import pygame

class Info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.info_running = True

        
    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()

    def capumain(self):
        background = pygame.image.load('images\images-pokedex\pokedex2b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()
        
    def evoli(self):
        background = pygame.image.load('images\images-pokedex\pokedex3b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def marcacrin(self):
        background = pygame.image.load('images\images-pokedex\pokedex4b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def salameche(self):
        background = pygame.image.load('images\images-pokedex\pokedex5b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def medhyena(self):
        background = pygame.image.load('images\images-pokedex\pokedex6b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def tiplouf(self):
        background = pygame.image.load('images\images-pokedex\pokedex7b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def caninos(self):
        background = pygame.image.load('images\images-pokedex\pokedex8b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()

    def etourvol(self):
        background = pygame.image.load('images\images-pokedex\pokedex208.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.addd_name("etourvol")

    def lainergie(self):
        background = pygame.image.load('images\images-pokedex\pokedex212.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()

    def floravol(self):
        background = pygame.image.load('images\images-pokedex\pokedex209.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()

    def luxio(self):
        background = pygame.image.load('images\images-pokedex\pokedex214.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
        
    def magicarpe(self):
        background = pygame.image.load('images\images-pokedex\pokedex213.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def phanpy(self):
        background = pygame.image.load('images\images-pokedex\pokedex215.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def psykokwak(self):
        background = pygame.image.load('images\images-pokedex\pokedex210.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
        
    def rondoudou(self):
        background = pygame.image.load('images\images-pokedex\pokedex211.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()        

    def button_quit(self):
        # Affiche le bouton QUIT
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    def button_back(self):
        # Affiche le bouton BACK
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        
        
    def button_add(self):
        # Affiche le bouton BACK
        self.rect_radius(5, self.white, 540, 10, 70, 25)
        self.text_c1("ADD", self.black, 550, 13)
           
           
    def is_mouse_over_button(self, button_rect):
        # Vérifie si la souris est au-dessus du bouton
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)
    

        
    def info_pokemon_run(self):
        self.button_add()
        self.button_quit()

        while self.info_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.info_running = False
                elif self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                    # # Vérifie si le bouton gauche de la souris est cliqué
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                    #     # Quitte le jeu lors du clic sur le bouton QUIT
                        pass
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        
                        self.info_running = False
                    # if self.is_mouse_over_button(pygame.Rect(540, 10, 70, 25)):
                    # # self.add_name("etourvol")
                    #     print("etourvol")
                        
            pygame.display.flip()