# Importer les modules
from global_def import Global
from play_pokemon import Play_Pokemon
from add_pokemon import Add_Pokemon
from pokedex import Pokedex
import pygame, time, sys

class Menu(Global): 
    
    def __init__(self): 
        Global.__init__(self)
        self.play_p = Play_Pokemon()
        # self.play_f = Play_Fight()
        self.add_pokemon = Add_Pokemon()
        self.pokedex = Pokedex()
        self.running = True

    def menu_run(self):        
        self.display_name_background() 
        self.options_menu()       

    def display_name_background (self):
        start_time = time.time()
        while True:
            self.screen.fill(self.white)
            current_time = time.time()
            elapsed_time = current_time - start_time
            # Afficher prenoms
            if elapsed_time < 2:
                self.text_c1("By  Ines Lorquet - Lucy Madec - Vanny Lamorte", self.black, 220, 410)
                self.img_back("img_forest", "images/images-menu/menu1.png")
            else:
                break
            pygame.display.flip()
            self.clock.tick(60)

    # Afficher des rectangles blancs pour les options du menu            

    def  draw_menu_option(self, rect, text, pos):
        menu_text = self.police_p1.render(text, True, self.grey)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.white, rect.inflate(10, 10), border_radius=10)
        else:
            pygame.draw.rect(self.screen, self.white, rect, border_radius=10)
        self.screen.blit(menu_text, pos)     

    def options_menu(self): 
        # Définir choix du menu
        self.running = True
        img_back = pygame.image.load("images/images-menu/menu2.png").convert()
        option_rects = [
            pygame.Rect(50, 100 + i * 100, 200, 50) for i in range(4)
        ]
        option_texts = ["PLAY", "ADD POKEMON", "POKEDEX", "QUIT"]

        while self.running:
            self.screen.blit(img_back, (0, 0))           

            for i, (rect, text) in enumerate(zip(option_rects, option_texts)):
                if text == "ADD POKEMON":
                    position = (70, 100 + i * 100)
                elif text == "POKEDEX":
                    position = (100, 100 + i * 100)
                else:
                    position = (125, 100 + i * 100)

                self.draw_menu_option(rect, text, position)
            self.rect_radius(10, self.white, 310, 100, 440, 350)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Lier les options du menu à d'autres pages
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, item in enumerate(option_texts):
                        rect = option_rects[i]
                        if rect.collidepoint(mouse_pos):
                            if item == "PLAY":
                                self.play_p.play_pokemon_run()
                            elif item == "ADD POKEMON":
                                self.add_pokemon.add_pokemon_run()
                            elif item == "POKEDEX":
                                print("pokedex")
                                self.pok_running =  True
                                self.pokedex.pokedex_run()
                            elif item == "QUIT":
                                pygame.quit()
                                sys.exit()

            pygame.display.update()
            self.clock.tick(60)

test_menu = Menu()
test_menu.menu_run()
