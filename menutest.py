# Importer les modules
from global_def import Global
import pygame
import time
import sys

class Menu(Global): 
    def __init__(self): 
        super().__init__()
        # Définir les rectangles comme des attributs de la classe
        self.rect_play = pygame.Rect(50, 100, 200, 50)
        self.rect_add = pygame.Rect(50, 200, 200, 50)
        self.rect_pokedex = pygame.Rect(50, 300, 200, 50)
        self.rect_quit = pygame.Rect(50, 400, 200, 50)

    def play(self):
        pass

    def add_pokemon(self):
        pass

    def pokedex(self):
        pass

    def display_menu(self):
        running = True
        start_time = time.time()

        while running:
            self.screen.fill(self.orange)
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Afficher prénoms
            self.text_c1("By Ines Lorquet - Lucy Madec - Vanny Lamorte", self.black, 220, 410)

            # Afficher background forêt
            self.img_back("img_forest", "images/images-menu/menu1.png")

            if elapsed_time < 2:
                # Affiche la première partie du menu pendant les 2 premières secondes
                pass
            else:
                # Affiche la deuxième partie du menu après les 2 secondes
                self.options_menu()

            pygame.display.flip()
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()

        pygame.quit()

    def options_menu(self): 
        running = True           
        # Afficher logo Pokemon
        img_back = pygame.image.load("images/images-menu/menu2.png").convert()

        while running:
            option_radius = 10

            self.screen.blit(img_back, (0, 0)) 
            font = pygame.font.Font("Pixeled.ttf", 16)
            menu_play = font.render("PLAY", True, self.grey)
            menu_add = font.render("ADD POKEMON", True, self.grey)
            menu_pokedex = font.render("POKEDEX", True, self.grey)
            menu_quit = font.render("QUIT", True, self.grey)

            # Utiliser les attributs de la classe pour accéder aux rectangles
            self.rect_radius(10, self.white, self.rect_play.x, self.rect_play.y, self.rect_play.width, self.rect_play.height)  
            self.screen.blit(menu_play, (self.rect_play.x + 75, self.rect_play.y))

            self.rect_radius(10, self.white, self.rect_add.x, self.rect_add.y, self.rect_add.width, self.rect_add.height) 
            self.screen.blit(menu_add, (self.rect_add.x + 30, self.rect_add.y))

            self.rect_radius(10, self.white, self.rect_pokedex.x, self.rect_pokedex.y, self.rect_pokedex.width, self.rect_pokedex.height)   
            self.screen.blit(menu_pokedex, (self.rect_pokedex.x + 45, self.rect_pokedex.y))

            self.rect_radius(10, self.white, self.rect_quit.x, self.rect_quit.y, self.rect_quit.width, self.rect_quit.height) 
            self.screen.blit(menu_quit, (self.rect_quit.x + 70, self.rect_quit.y))

            self.rect_radius(10, self.white, 310, 100, 440, 350) 

            # Effet hoover au passage de la souris
            if self.rect_play.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, self.rect_play.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_play, (self.rect_play.x + 75, self.rect_play.y))
                
            else:
                pygame.draw.rect(self.screen, self.white, self.rect_play, border_radius=option_radius)
                self.screen.blit(menu_play, (self.rect_play.x + 75, self.rect_play.y))

            if self.rect_add.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, self.rect_add.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_add, (self.rect_add.x + 30, self.rect_add.y))
            else:
                pygame.draw.rect(self.screen, self.white, self.rect_add, border_radius=option_radius)
                self.screen.blit(menu_add, (self.rect_add.x + 30, self.rect_add.y))

            if self.rect_pokedex.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, self.rect_pokedex.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_pokedex, (self.rect_pokedex.x + 45, self.rect_pokedex.y))
            else:
                pygame.draw.rect(self.screen, self.white, self.rect_pokedex, border_radius=option_radius)
                self.screen.blit(menu_pokedex, (self.rect_pokedex.x + 45, self.rect_pokedex.y))

            if self.rect_quit.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, self.rect_quit.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_quit, (self.rect_quit.x + 70, self.rect_quit.y))
            else:
                pygame.draw.rect(self.screen, self.white, self.rect_quit, border_radius=option_radius)
                self.screen.blit(menu_quit, (self.rect_quit.x + 70, self.rect_quit.y))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(60)

    def run(self):
        self.display_menu()
        self.options_menu()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    sys.exit()
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Utiliser les attributs de la classe pour accéder aux rectangles
                    if self.rect_play.collidepoint(mouse_pos):
                        print("ok")
                    elif self.rect_add.collidepoint(mouse_pos): 
                        print("okay")
                        # self.Add_pokemon1()                    
                    elif self.rect_pokedex.collidepoint(mouse_pos):
                        print("oki")
                        # self.Pokedex1()
                            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False 

            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()

menu = Menu()
menu.run()
