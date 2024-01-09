import pygame

class Pokedex:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.police = pygame.font.Font("Pokemon Classic.ttf", 50)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()

    def texte(self,texte, couleur, x, y):
        texte_surface = self.police.render(texte, True, couleur)
        self.screen.blit(texte_surface, (x, y))
        
    def background(self):
        black = (0,0,0)
        background = pygame.image.load('images\images-pokedex\pokedex1020.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.texte("POKEDEX",black,250,30)

    def pokemon(self):
        radius = 10
        white = "#3c3c3c"
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
        
        pikachu = pygame.image.load('images\images-pokedex\pokedex1.png')
        pikachu = pikachu.convert_alpha()
        pikachu = pygame.transform.scale(pikachu,(100,106))        
        self.screen.blit(pikachu, (50,250))

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
