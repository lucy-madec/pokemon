from global_def import Global
import pygame

class Info_pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        
    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1b.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.button_back1()

    def capumain(self):
        background = pygame.image.load('images\images-pokedex\pokedex2b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back1()
        
    def evoli(self):
        background = pygame.image.load('images\images-pokedex\pokedex3b.png')
        background = background.convert()
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
    def marcacrin(self):
        background = pygame.image.load('images\images-pokedex\pokedex4b.png')
        background = background.convert()
        self.button_back()
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
        self.button_back()
        self.screen.blit(background, (0,0))
        self.button_back()
                
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

    # def button_back(self):
    #     self.rect_radius(5, self.white, 720, 10, 70, 25)
    #     self.text_c1("BACK", self.black, 733, 13)
    #     pygame.display.update()
    #     pygame.display.flip()

    def button_back1(self):
        self.rect_radius(5, self.yellow, 620, 10, 70, 25)
        self.text_c1("BACK", self.black, 633, 13)
        pygame.display.update()
        pygame.display.flip()
        
    def button_back(self):
        self.rect_radius(10, self.white, 720, 10, 70, 25)
        self.text_c1("BACK", self.black, 733, 13)


    def info_pokemon_run(self):
        info_run = True
        while info_run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    info_run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 10, 70, 25)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.pokedex.pokedex_run()
                        info_run = False
            pygame.display.flip()
        pygame.quit()