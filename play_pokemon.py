from global_def import Global
from play_fight import Play_Fight
import pygame
import json

class Play_Pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.play_pok_running = True
        self.play_f = Play_Fight()
    
    # Afficher background
    def background(self):
        background = pygame.image.load(r'images\images-play\play4.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.rect_radius(10, self.white, 180, 10, 400, 80)
        self.text_c2("Choose your pokemon...", self.black, 230, 35)

    def ajout_pokemon(self): 
        self.background()

        # PAGE 2: Rectangles blancs

        self.rect_radius(10,self.white,20, 150, 170, 120)   # Etourvol 
        self.rect_radius(10,self.white,220, 150, 170, 120)  # Floravol
        self.rect_radius(10,self.white,420, 150, 170, 120)  # Psykokwak
        self.rect_radius(10,self.white,620, 150, 170, 120)  # Roudoudou

        self.rect_radius(10,self.white,20, 300, 170, 120)   # Lainergie
        self.rect_radius(10,self.white,220, 300, 170, 120)  # Magicarpe
        self.rect_radius(10,self.white,420, 300, 170, 120)  # Luxio
        self.rect_radius(10,self.white,620, 300, 170, 120)  # Phanpy

        # Flèche gauche
        self.rect_radius(10,self.yellow, 20, 80, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((50,90),(30,110),(50,130)), 7)

        # Récuperer nom pokemon du pokemon.json
        with open('pokemon.json', 'r') as json_file:
            data = json.load(json_file)
        name_pokemons = [pokemon["nom"] for pokemon in data]

        for name in name_pokemons:

            if name == "Etourvol":
                self.img_pokemon("Etourvol",r'images/images-add/add_pokemon1.png',70,89,75,155)
                self.text_c2("Etourvol",self.black,60,242)
                
            if name == "Floravol":
                self.img_pokemon("Floravol",r'images/images-add/add_pokemon2.png',100,119,265,142)
                self.text_c2("Floravol",self.black,265,242)

            if name == "Psykokwak":
                self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',70,89,465,153)
                self.text_c2("Psykokwak",self.black,440, 242)

            if name == "Roudoudou":
                self.img_pokemon("Roudoudou",r'images/images-add/add_pokemon8.png',70,79,670,158)
                self.text_c2("Roudoudou",self.black,642,242)  

            if name == "Lainergie":
                self.img_pokemon("Lainergie",r'images/images-add/add_pokemon3.png',85,89,65,305)
                self.text_c2("Lainergie",self.black,50,390)
                
            if name == "Luxio":
                self.img_pokemon("Luxio",r'images/images-add/add_pokemon4.png',90,109,450,295)
                self.text_c2("Luxio",self.black,470,390)

            if name == "Magicarpe":
                self.img_pokemon("Magicarpe",r'images/images-add/add_pokemon5.png',90,99,255,302)
                self.text_c2("Magicarpe",self.black,245,390)

            if name == "Phanpy":
                self.img_pokemon("Phanpy",r'images/images-add/add_pokemon6.png',80,99,655,300)
                self.text_c2("Phanpy",self.black,670,390)      
        
            pygame.display.update()
            pygame.display.flip()
            
    def pokemon(self):

        # PAGE 1     
              
        # Afficher pokemon Pikachu
        self.rect_radius(10,self.white,20, 150, 170, 120) 
        self.img_pokemon("pikachu",r'images\images-pokedex\pokedex1.png',100,109,65,150)
        self.text_c2("pikachu",self.black,60,242)

        # Afficher pokemon Evoli
        self.rect_radius(10,self.white,220, 150, 170, 120)
        self.img_pokemon("evoli",r'images\images-pokedex\pokedex3.png',90,99,265,152)
        self.text_c2("evoli",self.black,270,242)

        # Afficher pokemon Tiplouf
        self.rect_radius(10,self.white,420, 150, 170, 120)
        self.img_pokemon("tiplouf",r'images\images-pokedex\pokedex7.png',100,109,455,140)
        self.text_c2("tiplouf",self.black,460,242)

        # Afficher pokemon Caninos
        self.rect_radius(10,self.white,620, 150, 170, 120)
        self.img_pokemon("caninos",r'images\images-pokedex\pokedex8.png',100,109,645,140)
        self.text_c2("caninos",self.black,655,242)     

        # Afficher pokemon Capumain
        self.rect_radius(10,self.white,20, 300, 170, 120)
        self.img_pokemon("capumain",r'images\images-pokedex\pokedex2.png',115,119,45,290)
        self.text_c2("capumain",self.black,60,390)

        # Afficher pokemon Salameche
        self.rect_radius(10,self.white,220, 300, 170, 120)
        self.img_pokemon("salameche",r'images\images-pokedex\pokedex5.png',110,119,255,280)
        self.text_c2("salameche",self.black,245,390)

        # Afficher pokemon Marcacrin
        self.rect_radius(10,self.white,420, 300, 170, 120)
        self.img_pokemon("marcacrin",r'images\images-pokedex\pokedex4.png',130,129,437,270)
        self.text_c2("marcacrin",self.black,440,390)      
        
        # Afficher pokemon Medhyena        
        self.rect_radius(10,self.white,620, 300, 170, 120)
        self.img_pokemon("medhyena",r'images\images-pokedex\pokedex6.png',260,269,585,170)
        self.text_c2("medhyena",self.black,655,390)
        
        # Flèche droite
        self.rect_radius(10,self.yellow,740, 80, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((750,90),(770,110),(750,130)), 7)
        pygame.display.update()
        pygame.display.flip()

    def pokemon_choose(self, name):
        with open('pokemon.json', 'r') as json_file:
            data = json.load(json_file)

        pokemon_data = next((pokemon for pokemon in data if pokemon["nom"] == name), None)

        if pokemon_data:
            with open('choice.json', 'w') as new_json_file:
                json.dump([pokemon_data], new_json_file, indent=2)
        else:
            print(f"Pokemon {name} Non Trouvé")
            
    # Afficher bouton QUIT
    def button_quit(self):
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    # Afficher bouton BACK
    def button_menu(self):
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)

    # Vérifier si souris au-dessus du bouton
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)   

    def play_pokemon_run(self):
        self.play_pok_running = True
        self.run()

    def run(self):
        poke2 = False
        self.background()
        self.pokemon()
        self.button_menu()

        while self.play_pok_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.play_pok_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    # Bouton QUIT
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        pygame.quit()
                                         
                    # Bouton MENU
                    if self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        print("menu")
                        self.play_pok_running = False                      

                # Flèche droite           
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(740, 80, 50, 70)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        poke2 = True
                    if poke2 == True:
                        self.ajout_pokemon()

                # Flèche gauche
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 80, 50, 60)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        poke2 = False
                        self.pokemon()
                
                if poke2 == False:

                    # Rectangle du haut
                    self.button_menu() 

                # PAGE 1 : Rectangles haut 

                    # Accéder à la section combat en choisissant Pikachu         
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Pikachu")
                            self.play_f.play_fight_run()  
                            self.play_pok_running = False 
                            
                    # Accéder à la section combat en choisissant Evoli                            
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Evoli")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Tiplouf 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Tiplouf")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Caninos 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Caninos")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                # PAGE 1 : Rectangle du bas  

                    # Accéder à la section combat en choisissant Capumain                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Capumain")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Salameche 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Salameche")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 
                            
                    # Accéder à la section combat en choisissant Marcacrin 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Marcacrin")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Medhyena        
                    if event.type == pygame.MOUSEBUTTONDOWN : 
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Medhyena")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                if poke2 == True:
                    self.button_menu()
                    self.button_quit() 

                # PAGE 2 : Rectangle du haut                  
                    
                    # Accéder à la section combat en choisissant Etourvol           
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Etourvol")
                            self.play_f.play_fight_run()                           
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Floravol                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Floravol")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                    # Accéder à la section combat en choisissant Psykokwak
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Psykokwak")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 
                            
                    # Accéder à la section combat en choisissant Roudoudou
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 150, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Roudoudou")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

                # PAGE 2 : Rectangle du haut 

                    # Accéder à la section combat en choisissant Lainergie             
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Lainergie")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 
                            
                    # Accéder à la section combat en choisissant Magicarpe
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Magicarpe")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 
                            
                    # Accéder à la section combat en choisissant Luxio
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Luxio")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False                             

                    # Accéder à la section combat en choisissant Phanpy        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 300, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.play_fight_running = True
                            self.pokemon_choose("Phanpy")
                            self.play_f.play_fight_run()
                            self.play_pok_running = False 

            self.button_menu()
            self.button_quit()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(30)

# test = Play_Pokemon()
# test.play_pokemon_run()
