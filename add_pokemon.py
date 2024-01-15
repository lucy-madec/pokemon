from global_def import Global
from info_pokemon import Info_pokemon
import pygame
from menu import Menu

class Add_Pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.info_pokemon = Info_pokemon()
        self.M = Menu()
        self.show_menu = False
        self.hover_menu = False 
        self.quit = False

    # Affiche le background
    def background(self):
        background = pygame.image.load('images/images-add/add_pokemon10.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))

    # Affiche le logo "Catch Them All"
    def logo(self):
        self.img_pokemon("tagline",'images/images-add/add_pokemon9.png',175,100,340,110) 
    
    # Affiche le bouton QUIT
    def button_quit(self):        
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    def button_menu(self):
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)
    
    # Vérifie si le bouton gauche de la souris est cliqué
    def is_quit_button_clicked(self):  
        mouse_pos = pygame.mouse.get_pos()
        quit_button_rect = pygame.Rect(720, 10, 70, 25)
        return quit_button_rect.collidepoint(mouse_pos)
    
    def is_menu_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        back_menu_rect = pygame.Rect(640, 10, 70, 25)
        return back_menu_rect.collidepoint(mouse_pos)
    
    def logo(self):
        self.img_pokemon("tagline",'images/images-add/add_pokemon9.png',175,100,340,110)     

    #  Affiche liste des 8 Pokémons
    def pokemon(self):
        
        # Affiche titre "Add Pokémon"
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c5("ADD POKEMON",self.black,350,65)
        
        # Crée rectangles haut
        self.rect_radius(10,self.white,20, 250, 170, 120)
        self.rect_radius(10,self.white,220, 250, 170, 120)
        self.rect_radius(10,self.white,420, 250, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)
    
        # Crée rectangles bas
        self.rect_radius(10,self.white,20, 450, 170, 120)
        self.rect_radius(10,self.white,220, 450, 170, 120)
        self.rect_radius(10,self.white,420, 450, 170, 120)
        self.rect_radius(10,self.white,620, 450, 170, 120)
        
        # Affiche pokemon Etourvol
        self.img_pokemon("Etourvol",'images/images-add/add_pokemon1.png',70,89,75,255)
        self.text_c2("Etourvol",self.black,60,342)

        # Affiche pokemon Lainergie
        self.img_pokemon("Lainergie",'images/images-add/add_pokemon3.png',85,89,65,455)
        self.text_c2("Lainergie",self.black,50,542)

        # Affiche pokemon Floravol
        self.img_pokemon("Floravol",'images/images-add/add_pokemon2.png',100,119,265,242)
        self.text_c2("Floravol",self.black,265,342)

        # Affiche pokemon Luxio
        self.img_pokemon("Luxio",'images/images-add/add_pokemon4.png',90,109,450,445)
        self.text_c2("Luxio",self.black,470,542)

        # Affiche pokemon Magicarpe
        self.img_pokemon("Magicarpe",'images/images-add/add_pokemon5.png',90,99,255,452)
        self.text_c2("Magicarpe",self.black,245,542)
        
        # Affiche pokemon Phanpy
        self.img_pokemon("Phanpy",'images/images-add/add_pokemon6.png',80,99,655,450)
        self.text_c2("Phanpy",self.black,670,542)
        
        # Affiche pokemon Psykokwak
        self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',70,89,465,253)
        self.text_c2("Psykokwak",self.black,440,342)
        
        # Affiche pokemon Rondoudou
        self.img_pokemon("Rondoudou",'images/images-add/add_pokemon8.png',70,79,670,258)
        self.text_c2("Rondoudou",self.black,642,342) 

    def setup_screen(self):
        self.background()
        self.logo()
        self.pokemon()
        self.button_quit()

    def show_pokemon_list(self):
        self.setup_screen()       
        pygame.display.update()
        pygame.display.flip()

    def add_pokemon_run(self):
        self.run()

    def run(self):
        self.setup_screen()
        running = True
        while not self.show_menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.show_menu = True  # Close the Pokemon list and show the menu
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.is_quit_button_clicked():
                        self.show_menu = True  # Close the Pokemon list and show the menu
                    elif self.is_menu_button_clicked():
                        self.M.menu_run()
                        self.show_menu = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Quitte le jeu lors du clic sur le bouton QUIT
                    if self.is_quit_button_clicked():    
                        running = False
                    elif self.is_menu_button_clicked():
                        self.pokemon()

            #Test cliques sur les rect                    
        
                #Rectangle du haut        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.etourvol()
             
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.floravol()                      

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.floravol()
                       
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.luxio()
                       
                #Rectangle du bas        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.lainergie()                

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.magicarpe()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.psykokwak()
                       
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.rondoudou()
                                                       
            self.button_quit()
            self.button_menu()
            
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

ajout = Add_Pokemon()
ajout.add_pokemon_run()

