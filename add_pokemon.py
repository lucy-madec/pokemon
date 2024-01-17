from global_def import Global
from info_pokemon import Info_pokemon
import pygame
import json
class Add_Pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.info_pokemon = Info_pokemon()
        self.add_running = True

    def background(self):
        background = pygame.image.load('images/images-add/add_pokemon10.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))

    # Afficher le logo "Catch Them All"
    def logo(self):
        self.img_pokemon("tagline",'images/images-add/add_pokemon9.png',175,100,340,110) 
    
    # Afficher le bouton QUIT
    def button_quit(self):        
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    def button_menu(self):
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)
    
    # Vérifier si le bouton gauche de la souris est cliqué
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

    #  Afficher liste des 8 Pokémons
    def pokemon(self):
        
        # Afficher titre "Add Pokémon"
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c5("ADD POKEMON",self.black,350,65)
        
        # Créer rectangles haut
        self.rect_radius(10,self.white,20, 250, 170, 120)
        self.rect_radius(10,self.white,220, 250, 170, 120)
        self.rect_radius(10,self.white,420, 250, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)
    
        # Créer rectangles bas
        self.rect_radius(10,self.white,20, 450, 170, 120)
        self.rect_radius(10,self.white,220, 450, 170, 120)
        self.rect_radius(10,self.white,420, 450, 170, 120)
        self.rect_radius(10,self.white,620, 450, 170, 120)
        
        # Afficher pokemon Etourvol
        self.img_pokemon("Etourvol",'images/images-add/add_pokemon1.png',70,89,75,255)
        self.text_c2("Etourvol",self.black,60,342)

        # Afficher pokemon Lainergie
        self.img_pokemon("Lainergie",'images/images-add/add_pokemon3.png',85,89,65,455)
        self.text_c2("Lainergie",self.black,50,542)

        # Afficher pokemon Floravol
        self.img_pokemon("Floravol",'images/images-add/add_pokemon2.png',100,119,265,242)
        self.text_c2("Floravol",self.black,265,342)

        # Afficher pokemon Luxio
        self.img_pokemon("Luxio",'images/images-add/add_pokemon4.png',90,109,450,445)
        self.text_c2("Luxio",self.black,470,542)

        # Afficher pokemon Magicarpe
        self.img_pokemon("Magicarpe",'images/images-add/add_pokemon5.png',90,99,255,452)
        self.text_c2("Magicarpe",self.black,245,542)
        
        # Afficher pokemon Phanpy
        self.img_pokemon("Phanpy",'images/images-add/add_pokemon6.png',80,99,655,450)
        self.text_c2("Phanpy",self.black,670,542)
        
        # Afficher pokemon Psykokwak
        self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',70,89,465,253)
        self.text_c2("Psykokwak",self.black,440,342)
        
        # Afficher pokemon Rondoudou
        self.img_pokemon("Rondoudou",'images/images-add/add_pokemon8.png',70,79,670,258)
        self.text_c2("Rondoudou",self.black,642,342) 


    # def read_json(self,name):
    #     with open('add_json.json', 'r') as json_file:
    #         data = json.load(json_file)
    #     if etourvol_data := next(
    #         (pokemon for pokemon in data if pokemon["Nom"] == name), None
    #     ):
    #         try:
    #             with open('pokemon_json.json', 'r') as dest_json_file:
    #                 destination_data = json.load(dest_json_file)
    #         except FileNotFoundError:
    #             destination_data = []
    #         destination_data.append(etourvol_data)

    #         with open('pokemon_json.json', 'w') as new_json_file:
    #             json.dump(destination_data, new_json_file, indent=2)
    #         print("Le dictionnaire Etourvol a été ajouté à pokemon_json.json.")
    #     else:
    #         print("Le Pokémon Etourvol n'a pas été trouvé dans le fichier JSON.")

    def button_add(self):
        self.rect_radius(5, self.white, 540, 10, 70, 25)
        self.text_c1("ADD", self.black, 550, 13)

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
        self.add_running = True
        self.run()

    def run(self):
        self.setup_screen()
        while self.add_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.add_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Quitte le jeu lors du clic sur le bouton QUIT
                    if self.is_quit_button_clicked():    
                        self.add_running = False
                    elif self.is_menu_button_clicked():
                        self.add_running = False

                        

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
                        self.info_pokemon.psykokwak()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.rondoudou()


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
                        self.info_pokemon.luxio()
          
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.phanpy()
                        
            self.button_quit()
            self.button_menu()
            self.button_add()
            pygame.display.flip()
            self.clock.tick(30)

# test_add_pokemon = Add_Pokemon()
# test_add_pokemon.add_pokemon_run()

