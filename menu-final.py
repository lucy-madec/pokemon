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

    def display_texte(self, texte, couleur, x, y):
        police_menu = pygame.font.Font("Arial", 30)
        texte_surface = police_menu.render(texte, True, couleur)
        self.screen.blit(texte_surface, (x, y))
    
    def display_menu(self):
        
        running = True
        start_time = time.time()
        police = pygame.font.Font(None, 36)
        
        while running:
            black = (255, 255, 255)
            font_options = pygame.font.Font(None, 30)
            white = "#ffffff"
            self.screen.fill(white)
            current_time = time.time()
            elapsed_time = current_time - start_time
            
            if elapsed_time < 2 :
                img_logo =  pygame.image.load("images/images-menu/menu1.png").convert_alpha()
                L_img_logo, H_img_logo = img_logo.get_size()
                img_logo = pygame.transform.scale(img_logo, (L_img_logo,H_img_logo))
                x =(self.screen_width - L_img_logo)//2
                y = (self.screen_height - H_img_logo)//2
                self.screen.blit(img_logo, (x, y))

                name1 = font_options.render("Pikachu", True, black)
                name2 = font_options.render("Charmander", True, black)
                name3 = font_options.render("Bulbasaur", True, black)

                

                display_texte(self, "Ines Lorquet, Lucy Madec, Vanny Lamorte", black, 300, 150)

                self.screen.blit(name1, (x, y))
                self.screen.blit(name2, (x, y))
                self.screen.blit(name3, (x, y))

            else:
                break

            pygame.display.flip()
            self.clock.tick(60)
            
    def options_menu(self): 
        running = True
        img_back = pygame.image.load("images/images-menu/menu2.jpg").convert()
                
        while running:  
            white = "#ffffff"
            grey = "#3c3c3c"
            option_radius = 10
            self.screen.blit(img_back, (0,0)) 
            font = pygame.font.Font(None, 30)
            menu_play = font.render("PLAY", True, grey)
            menu_add = font.render("ADD POKEMON", True, grey)
            menu_pokedex = font.render("POKEDEX", True, grey)
            menu_quit = font.render("QUIT", True, grey)
            pygame.draw.rect(self.screen, white, (50, 100, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_play, (60, 110))

            pygame.draw.rect(self.screen, white, (50, 200, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_add, (60, 210))

            pygame.draw.rect(self.screen, white, (50, 300, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_pokedex, (60, 310))

            pygame.draw.rect(self.screen, white, (50, 400, 200, 50), border_radius=option_radius)
            self.screen.blit(menu_quit, (60, 410))


        # Quittez avec la touche "Escape"
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
        
            pygame.display.update()
            self.clock.tick(60)

    def run(self):
        self.display_menu()
        self.options_menu()
        pygame.quit()    

menu = Menu()
menu.run()