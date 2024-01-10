# Importer les modules
from global_def import Global

import pygame, time

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)

    
    def display_menu(self):
        running = True
        start_time = time.time()
        police_menu = pygame.font.Font("Pokemon Classic.ttf",10)              

        while running:

            self.screen.fill(self.orange)
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            if elapsed_time < 2:

                # Afficher prénoms
                self.text_c1("By  Ines Lorquet - Lucy Madec - Vanny Lamorte", self.black, 220, 410)

                # Afficher background
                self.img_back("img","images/images-menu/menu1.png")

            else:
                break

            pygame.display.flip()
            self.clock.tick(60)
            
    def options_menu(self): 
        running = True
        img_back = pygame.image.load("images/images-menu/menu2.png").convert()

        # white = "#ffffff"
        # grey = "#3c3c3c"            

        option_radius = 10

        # Créer le hoover
        rect_play = pygame.Rect(50, 100, 200, 50)
        rect_add = pygame.Rect(50, 200, 200, 50)
        rect_pokedex = pygame.Rect(50, 300, 200, 50)
        rect_quit = pygame.Rect(50, 400, 200, 50)       
        
        while running:  

            self.screen.blit(img_back, (0,0)) 
            font = pygame.font.Font("Pixeled.ttf", 16)

            menu_play = font.render("PLAY", True, self.grey)
            menu_add = font.render("ADD POKEMON", True, self.grey)
            menu_pokedex = font.render("POKEDEX", True, self.grey)
            menu_quit = font.render("QUIT", True, self.grey)
                       
            pygame.draw.rect(self.screen, self.white, (50, 100, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_play,(125, 100))

            pygame.draw.rect(self.screen, self.white, (50, 200, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_add,(70, 200))

            pygame.draw.rect(self.screen, self.white, (50, 300, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_pokedex,(95, 300))

            pygame.draw.rect(self.screen, self.white, (50, 400, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_quit,(120, 400)) 

            pygame.draw.rect(self.screen, self.white,(310, 100, 440, 350), border_radius=option_radius)
                              
            # Effet hoover au passage de la souris
            if rect_play.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, rect_play.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_play,(125, 100))
            else:
                pygame.draw.rect(self.screen, self.white, rect_play, border_radius=option_radius)
                self.screen.blit(menu_play,(125, 100))

            if rect_add.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, rect_add.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_add,(70, 200))
            else:
                pygame.draw.rect(self.screen, self.white, rect_add, border_radius=option_radius)
                self.screen.blit(menu_add, (70, 200))

            if rect_pokedex.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, rect_pokedex.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_pokedex, (95, 300))
            else:
                pygame.draw.rect(self.screen, self.white, rect_pokedex, border_radius=option_radius)
                self.screen.blit(menu_pokedex, (95, 300))

            if rect_quit.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.white, rect_quit.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_quit, (120, 400))
            else:
                pygame.draw.rect(self.screen, self.white, rect_quit, border_radius=option_radius)
                self.screen.blit(menu_quit, (120, 400))


        # Quittez avec "Escape"
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
        pygame.quit()

menu = Menu()
menu.run()