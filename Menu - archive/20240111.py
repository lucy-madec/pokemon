# Importer les modules
from global_def import Global
from test1 import Test1
from test2 import Test2
from test3 import Test3

import pygame, time, sys

class Menu(Global): 

    def __init__(self): 
        Global.__init__(self)
        self.T1 = Test1()
        self.T2 = Test2()
        self.T3 = Test3() 

    def run(self):        
        self.display_name_background() 
        self.options_menu()       
    
    def display_name_background (self):
        start_time = time.time()
        while True:
            self.screen.fill(self.orange)
            current_time = time.time()
            elapsed_time = current_time - start_time
            if elapsed_time < 2:
                self.text_c1("By  Ines Lorquet - Lucy Madec - Vanny Lamorte", self.black, 220, 410)
                self.img_back("img_forest", "images/images-menu/menu1.png")
            else:
                break
            pygame.display.flip()
            self.clock.tick(60)            

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
                                self.T1.affichage1()
                                print("T1")
                            elif item == "ADD POKEMON":
                                self.T2.affichage2()
                                print("T2")
                            elif item == "POKEDEX":
                                self.T3.affichage3()
                                print("T3")
                            elif item == "QUIT":
                                pygame.quit()
                                sys.exit()
                            running = False 
                               
      
                pygame.display.update()
            
            self.clock.tick(60)

    

menu = Menu()
menu.run()