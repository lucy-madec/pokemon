# Importer les modules
import pygame, time

class Menu: 

    def __init__(self): 
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
    
    def display_menu(self):
        running = True
        start_time = time.time()
        police_menu = pygame.font.Font("Pokemon Classic.ttf",10)
        orange = (255,103, 2)        
        black =  (0, 0, 0)

        while running:

            self.screen.fill(orange)
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            if elapsed_time < 2 :

                # Afficher prénoms
                prenom = "By  Ines Lorquet - Lucy Madec - Vanny Lamorte"
                texte_prenom = police_menu.render(prenom, True, black)
                self.screen.blit(texte_prenom,(220,410))             

                # Afficher background
                img_logo =  pygame.image.load("images/images-menu/menu1.png").convert_alpha()
                L_img_logo, H_img_logo = img_logo.get_size()
                img_logo = pygame.transform.scale(img_logo, (L_img_logo,H_img_logo))
                x =(self.screen_width - L_img_logo)//2
                y = (self.screen_height - H_img_logo)//2
                self.screen.blit(img_logo, (x, y))
                
            else:
                break

            pygame.display.flip()
            self.clock.tick(60)
            
    def options_menu(self): 
        running = True
        img_back = pygame.image.load("images/images-menu/menu2.png").convert()

        white = "#ffffff"
        grey = "#3c3c3c"            

        option_radius = 10

        # Créer le hoover
        rect_play = pygame.Rect(50, 100, 200, 50)
        rect_add = pygame.Rect(50, 200, 200, 50)
        rect_pokedex = pygame.Rect(50, 300, 200, 50)
        rect_quit = pygame.Rect(50, 400, 200, 50)       
        
        while running:  

            self.screen.blit(img_back, (0,0)) 
            font = pygame.font.Font("Pixeled.ttf", 16)

            menu_play = font.render("PLAY", True, grey)
            menu_add = font.render("ADD POKEMON", True, grey)
            menu_pokedex = font.render("POKEDEX", True, grey)
            menu_quit = font.render("QUIT", True, grey)
                       
            pygame.draw.rect(self.screen, white, (50, 100, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_play,(125, 100))

            pygame.draw.rect(self.screen, white, (50, 200, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_add,(70, 200))

            pygame.draw.rect(self.screen, white, (50, 300, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_pokedex,(95, 300))

            pygame.draw.rect(self.screen, white, (50, 400, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_quit,(120, 400)) 

            pygame.draw.rect(self.screen, white,(310, 100, 440, 350), border_radius=option_radius)
                              
            # Effet hoover au passage de la souris
            if rect_play.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, white, rect_play.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_play, (125, 100))
            else:
                pygame.draw.rect(self.screen, white, rect_play, border_radius=option_radius)
                self.screen.blit(menu_play, (125, 100))

            if rect_add.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, white, rect_add.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_add, (70, 200))
            else:
                pygame.draw.rect(self.screen, white, rect_add, border_radius=option_radius)
                self.screen.blit(menu_add, (70, 200))

            if rect_pokedex.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, white, rect_pokedex.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_pokedex, (95, 300))
            else:
                pygame.draw.rect(self.screen, white, rect_pokedex, border_radius=option_radius)
                self.screen.blit(menu_pokedex, (95, 300))

            if rect_quit.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, white, rect_quit.inflate(10, 10), border_radius=option_radius)
                self.screen.blit(menu_quit, (120, 400))
            else:
                pygame.draw.rect(self.screen, white, rect_quit, border_radius=option_radius)
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