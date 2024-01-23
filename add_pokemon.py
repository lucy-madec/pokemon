from global_def import Global
from info_pokemon import Info_pokemon
import pygame
import json

class Add_Pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.add_running = True
        self.info_pokemon = Info_pokemon()
        self.page = 1
        self.poke2 = False
        
    def background(self):
        background = pygame.image.load(r'images/images-add/add_pokemon10.jpg')
        background = background.convert()
        self.screen.blit(background, (0, 0))

    def read_json(self, name):
        with open('add_json.json', 'r') as json_file:
            data = json.load(json_file)

        if pokemon_data := next(
            (pokemon for pokemon in data if pokemon["nom"] == name), None
        ):
            try:
                with open('pokemon.json', 'r') as dest_json_file:
                    destination_data = json.load(dest_json_file)
            except FileNotFoundError:
                destination_data = []

            destination_data.append(pokemon_data)

            with open('pokemon.json', 'w') as new_json_file:
                json.dump(destination_data, new_json_file, indent=2) 


             

    def page1(self): 
        self.background()
        self.background()
        # Afficher titre "CLICK TO ADD POKEMON"
        self.rect_radius(10,self.white,200, 40, 400, 80)
        self.text_c5("CLICK TO ADD A POKEMON",self.black,220,65)

        # Créer rectangles haut
        self.rect_radius(10,self.white,100, 130, 600, 100) # Etourvol
        self.rect_radius(10,self.white,100, 250, 600, 100) # Floravol
        self.rect_radius(10,self.white,100, 370, 600, 100) # Lainergie
        self.rect_radius(10,self.white,100, 490, 600, 100) # Luxio

        # Afficher pokemon Etourvol
        self.img_pokemon("Etourvol",r'images/images-add/add_pokemon1.png',70,89,150,135)
        self.information("Etourvol",250,150)        
        # Afficher pokemon Floravol
        self.img_pokemon("Floravol",r'images/images-add/add_pokemon2.png',100,119,150,240)
        self.information("Floravol",250,270)
        
        # Afficher pokemon Lainergie
        self.img_pokemon("Lainergie",r'images/images-add/add_pokemon3.png',85,89,150,373)
        self.information("Lainergie",250,390)
        
        # Afficher pokemon Luxio
        self.img_pokemon("Luxio",r'images/images-add/add_pokemon4.png',90,109,150,483)
        self.information("Luxio",250,510)
        
        #boutton changer de page
        self.rect_radius(10,self.yellow,740, 380, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((770,410),(750,390),(750,430)), 7)


        pygame.display.update()
        pygame.display.flip()

    def page2(self):
        # Créer rectangles haut
        self.rect_radius(10,self.white,100, 130, 600, 100) # Magicarpe
        self.rect_radius(10,self.white,100, 250, 600, 100) # Phanpy
        self.rect_radius(10,self.white,100, 370, 600, 100) # Psykokwak
        self.rect_radius(10,self.white,100, 490, 600, 100) # Roudoudou
        
        # Afficher pokemon Magicarpe
        self.img_pokemon("Magicarpe",r'images/images-add/add_pokemon5.png',70,89,150,135)
        self.information("Magicarpe",250,150)
                
        # Afficher pokemon Phanpy
        self.img_pokemon("Phanpy",r'images/images-add/add_pokemon6.png',70,89,150,255)
        self.information("Phanpy",250,270)
                
        # Afficher pokemon Psykokwak
        self.img_pokemon("Psykokwak",r'images/images-add/add_pokemon7.png',85,89,150,373)
        self.information("Psykokwak",250,390)
        
        # Afficher pokemon Roudoudou
        self.img_pokemon("Roudoudou",r'images/images-add/add_pokemon8.png',60,89,150,493)
        self.information("Roudoudou",250,510)

        #boutton de gauche
        self.rect_radius(10,self.yellow,20, 380, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((30,410),(50,390),(50,430)), 7)

        pygame.display.update()
        pygame.display.flip()

    def information(self,name_pokemon,x,y):
        with open('add_json.json', 'r') as fichier:
            donnees_pokemons = json.load(fichier)

        for pokemon in donnees_pokemons:
            if pokemon["nom"] == name_pokemon:
                name = pokemon["nom"]
                type_pokemon = pokemon["type"]
                level = pokemon["niveau"]
                puissance = pokemon["puissance"]
                pv = pokemon["pv"]
                defense = pokemon["defense"]

        self.text_c2("NAME",self.black,x,y)
        self.text_c2("TYPE",self.black,x,y+20)
        self.text_c2("LEVEL",self.black,x,y+40)
        
        self.text_c2(name,self.black,x+90,y)
        self.text_c2(type_pokemon,self.black,x+90,y+20)
        self.text_c2(str(level),self.black,x+90,y+40)
            
        self.text_c2("POWER",self.black,x+250,y)
        self.text_c2("PV",self.black,x+250,y+20)
        self.text_c2("DEFENSE",self.black,x+250,y+40)
        
        self.text_c2(str(puissance),self.black,x+375,y)
        self.text_c2(str(pv),self.black,x+375,y+20)
        self.text_c2(str(defense),self.black,x+375,y+40)


    def button_quit(self):
        # Affiche le bouton QUIT
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)

    def button_menu(self):
        # Affiche le bouton BACK
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)

    def is_mouse_over_button(self, button_rect):
        # Vérifie si la souris est au-dessus du bouton
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)

    def add_pokemon_run(self):
        self.add_running = True
        self.run()

    def run(self):
        self.background()
        self.page1()
        self.button_menu()
      

        while self.add_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.add_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        pygame.quit()
                    if self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        self.add_running = False  

                    # Logique de clic sur les flèches gauche et droite
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Flèche droite
                    if pygame.Rect(740, 375, 50, 70).collidepoint(mouse_x, mouse_y):
                        self.poke2 = True
                        self.page2() if self.poke2 else self.page1()

                    # Flèche gauche
                    if pygame.Rect(20, 380, 50, 60).collidepoint(mouse_x, mouse_y):
                        self.poke2 = False
                        self.page2() if self.poke2 else self.page1()

                    if not self.poke2:
                        self.button_menu() 
                        self.button_menu() 
                        #Rectangle Page 1       
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 130, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Etourvol") 
   
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 250, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Floravol")
                                            
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 370, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Lainergie")           
                                                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 490, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Luxio")

                    if self.poke2:
                        self.button_menu()
                        self.button_quit() 
                        #Rectangles Page 2
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 130, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Magicarpe") 
                                    
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(70, 230, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Phanpy")
                                            
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 370, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Psykokwak")           
                                                        
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouse_x, mouse_y = pygame.mouse.get_pos()
                            button_rect = pygame.Rect(100, 490, 600, 100)
                            if button_rect.collidepoint(mouse_x, mouse_y):
                                self.read_json("Roudoudou")

            self.button_menu()
            self.button_quit()
            # self.draw_hover_rectangle()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(30)

# test_add_pokemon = Add_Pokemon()
# test_add_pokemon.add_pokemon_run()
