# Importer les modules
from global_def import Global
from cloud import Test1
from test2 import Test2
<<<<<<< HEAD:Archive_Pokedex/menu_am.py
<<<<<<< HEAD:menu.py
from info_pokemon import Info_pokemon
=======
from pokedex_ancien import Pokedex
>>>>>>> pokedex:Archive_Pokedex/menu_am.py
=======
from pokedex_ancien import Pokedex
>>>>>>> main_bis:Archive_Add_Pokemon/20240111asupprimer.py
import pygame, time, sys

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)
        self.play = Test1()
        self.add_pokemon = Test2()
        self.pokedex = Info_pokemon() 

    def run(self):        
        self.display_name_background() 
        self.options_menu()       
    
    def display_name_background (self):
        start_time = time.time()
        while True:
            self.screen.fill(self.white)
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time < 2:
                self.text_c1("By  Ines Lorquet - Lucy Madec - Vanny Lamorte", self.black, 220, 410)
                self.img_back("img_forest", "images/images-menu/menu1.png")
            else:
                break
            pygame.display.flip()
<<<<<<< HEAD:menu.py
            self.clock.tick(60)

    # Afficher rectangles blancs pour les options du menu            
=======
            self.clock.tick(60)            
>>>>>>> pokedex:Archive_Pokedex/menu_am.py

    def  draw_menu_option(self, rect, text, pos):
        menu_text = self.police_p1.render(text, True, self.grey)
        if rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.screen, self.white, rect.inflate(10, 10), border_radius=10)
        else:
            pygame.draw.rect(self.screen, self.white, rect, border_radius=10)
        self.screen.blit(menu_text, pos)     
    
    def options_menu(self): 
        running = True
        img_back = pygame.image.load("images/images-menu/menu2.png").convert()
        option_rects = [
            pygame.Rect(50, 100 + i * 100, 200, 50) for i in range(4)
        ]

        option_texts = ["PLAY", "ADD POKEMON", "POKEDEX", "QUIT"]

        while running:
            self.screen.blit(img_back, (0, 0))

            for i, (rect, text) in enumerate(zip(option_rects, option_texts)):
                self.draw_menu_option(rect, text, (125 if i != 1 else 70, 100 + i * 100))

            self.rect_radius(10, self.white, 310, 100, 440, 350)
       
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, item in enumerate(option_texts):
                        rect = option_rects[i]
                        if rect.collidepoint(mouse_pos):
                            if item == "PLAY":
                                self.play.affichage1()
                            elif item == "ADD POKEMON":
                                self.add_pokemon.affichage2()
                            elif item == "POKEDEX":
                                self.pokedex.pokedex_run()
                            elif item == "QUIT":
                                pygame.quit()
                                sys.exit()
                            running = False 


                pygame.display.update()
                pygame.display.flip()
            
            self.clock.tick(60)

    

menu = Menu()
menu.run()