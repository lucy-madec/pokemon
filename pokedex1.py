import pygame

class Pokedex:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.g_police = pygame.font.Font("Pokemon Classic.ttf", 50)
        self.p_police = pygame.font.Font("Pokemon Classic.ttf", 15)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()

    def b_text(self,text, coulor, x, y):
        text_surface = self.g_police.render(text, True, coulor)
        self.screen.blit(text_surface, (x, y))
        
    def l_text(self,text, coulor, x, y):
        text_surface = self.p_police.render(text, True, coulor)
        self.screen.blit(text_surface, (x, y))
        
    def background(self):
        background = pygame.image.load('images\images-pokedex\pokedex1020.png')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def pokemon(self):
        radius = 10
        white = "#ffffff"
        black = (0,0,0)
        pygame.draw.rect(self.screen,white,(200, 40, 440, 80),border_radius = radius) 
        self.b_text("POKEDEX",black,230,30)
        #Rectangles haut
        pygame.draw.rect(self.screen,white,(20, 250, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(220, 250, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(420, 250, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(620, 250, 170, 120),border_radius = radius)
        #Rectangles bas
        pygame.draw.rect(self.screen,white,(20, 450, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(220, 450, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(420, 450, 170, 120),border_radius = radius)
        pygame.draw.rect(self.screen,white,(620, 450, 170, 120),border_radius = radius) 
        #pokemon pikachu
        pikachu = pygame.image.load('images\images-pokedex\pokedex1.png')
        pikachu = pikachu.convert_alpha()
        pikachu = pygame.transform.scale(pikachu,(110,119))        
        self.screen.blit(pikachu, (45,245))
        self.l_text("pikachu",black,60,345)
        #pokemon posipi
        posipi = pygame.image.load('images\images-pokedex\pokedex3.png')
        posipi = posipi.convert_alpha()
        posipi = pygame.transform.scale(posipi,(115,119))        
        self.screen.blit(posipi, (45,440))
        self.l_text("posipi",black,70,545)
        #pokemon pyroli
        pyroli = pygame.image.load('images\images-pokedex\pokedex4.png')
        pyroli = pyroli.convert_alpha()
        pyroli = pygame.transform.scale(pyroli,(120,129))        
        self.screen.blit(pyroli, (245,242))
        self.l_text("posipi",black,270,345)
        #pokemon salamèche
        salamèche = pygame.image.load('images\images-pokedex\pokedex5.png')
        salamèche = salamèche.convert_alpha()
        salamèche = pygame.transform.scale(salamèche,(120,129))        
        self.screen.blit(salamèche, (245,442))
        self.l_text("salamèche",black,245,535)
         
        pygame.display.update()
        pygame.display.flip()


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.background()
            self.pokemon()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
            
pokedex1 = Pokedex()
pokedex1.run()
