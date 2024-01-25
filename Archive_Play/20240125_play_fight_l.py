from global_def import Global
from cloud import Cloud
from pokedex import Pokedex
import random
import pygame
import json

class Play_Fight(Global):

    def __init__(self):
        Global.__init__(self)
        self.play_fight_running = True
        self.c = Cloud ()
        self.run_clicked = False
        self.enemy_chosen = False
        self.poke = Pokedex()
        
    # Afficher background
    def background(self):
        self.img_back("Background", r"images/images-play/play1.jpg")
    
    # Afficher message début
    def message_start(self): 
        self.text_c2("What will you do ? ", self.black, 70, 475)  

    # Afficher message joueur choisit option "RUN"
    def message_run(self): 
        self.text_c1("C'est trop dangereux ici,", self.black, 70, 455)
        self.text_c1("vous décidez de fuir ", self.black, 70, 475)
        self.text_c1(" le combat.", self.black, 70, 495)

    # Afficher message joueur choisit option "FIGHT"
    def message_fight(self):
        self.text_c1("Vous avez choisi de ", self.black, 85, 455)
        self.text_c1("rester et de défier", self.black, 85, 475) 
        self.text_c1("le Pokémon sauvage.", self.black, 85, 495)   

    # Afficher message joueur choisit option "BAG"
    def message_bag(self): 
        self.text_c1("Le joueur fouille dans ", self.black, 80, 455)
        self.text_c1("son sac à la recherche", self.black, 80, 475)
        self.text_c1("d'objets utiles.", self.black, 80, 495) 
 
    # Afficher message joueur choisit option "POKEMON"
    def message_pokemon(self): 
        self.text_c1("Vous envoyez un autre", self.black, 80, 465) 
        self.text_c1("Pokémon au combat.", self.black, 80, 495)   
     
    # Afficher message joueur gagne
    def message_end_win(self): 
        self.text_c2("Félicitations !", self.black, 85, 445)  
        self.text_c1("Vous avez remporté ", self.black, 85, 475)
        self.text_c1("la victoire.", self.black, 85, 495)    

    # Afficher message joueur perd
    def message_end_lose(self): 
        self.text_c6("Vous avez été ", self.black, 105, 465)  
        self.text_c2("vaincu ! ", self.black, 130, 485)   

    # Afficher pokemon choisit pour fight
    def choose(self):
        with open('choix.json', 'r') as json_file:
            data = json.load(json_file)
        name_pokemons = [pokemon["nom"] for pokemon in data]
        
        for name in name_pokemons:
            if name == "Pikachu" and not self.run_clicked:
                self.img_pokemon("Pikachu",r'images/images-fight/fight1.png',200,209,120,225)
                
            if name == "Capumain" and not self.run_clicked:
                self.img_pokemon("Capumain",r'images/images-fight/fight2.png',190,209,120,225)

            if name == "Evoli" and not self.run_clicked:
                self.img_pokemon("Evoli",r'images/images-fight/fight3.png',205,209,100,205)
                                
            if name == "Marcacrin" and not self.run_clicked:
                self.img_pokemon("Marcacrin",r'images/images-fight/fight4.png',150,169,139,245)

            if name == "Salameche" and not self.run_clicked:
                self.img_pokemon("Salameche",r'images/images-fight/fight5.png',190,199,120,225)

            if name == "Medhyena" and not self.run_clicked:
                self.img_pokemon("Medhyena",r'images/images-fight/fight6.png',180,199,109,225)
                
            if name == "Tiplouf" and not self.run_clicked:
                self.img_pokemon("Tiplouf",r'images/images-fight/fight7.png',230,219,100,200)
                
            if name == "Caninos" and not self.run_clicked:
                self.img_pokemon("Caninos",r'images/images-fight/fight8.png',190,209,100,205)
                
            if name == "Etourvol" and not self.run_clicked:
                self.img_pokemon("Etourvol",r'images/images-fight/fight9.png',170,189,109,225)
                
            if name == "Floravol" and not self.run_clicked:
                self.img_pokemon("Floravol",r'images/images-fight/fight10.png',180,199,109,225)

            if name == "Lainergie" and not self.run_clicked:
                self.img_pokemon("Lainergie",r'images/images-fight/fight11.png',185,189,109,225)
                
            if name == "Luxio" and not self.run_clicked:
                self.img_pokemon("Luxio",r'images/images-fight/fight12.png',190,209,110,215)

            if name == "Magicarpe"and not self.run_clicked:
                self.img_pokemon("Magicarpe",r'images/images-fight/fight13.png',190,199,109,225)

            if name == "Phanpy" and not self.run_clicked:
                self.img_pokemon("Phanpy",r'images/images-fight/fight14.png',140,159,149,260)
                
            if name == "Psykokwak" and not self.run_clicked:
                self.img_pokemon("Psykokwak",r'images/images-fight/fight15.png',170,189,120,225)
                
            if name == "Roudoudou" and not self.run_clicked:
                self.img_pokemon("Roudoudou",r'images/images-fight/fight16.png',180,189,109,225)

    def rectangle(self): 

        # Rectangle blanc texte
        self.rect_radius(10,self.white,55,430,235,115) 
        self.img_pokemon("rectangle_texte",r'images/images-play/play7.png', 250,129,50,420)    

        # Rectangle droite: 4 choix d'actions
        self.rect_radius(10,self.white,335,430,430,115)          
        self.img_pokemon("rectangle_option",r'images/images-play/play5.png',445,129,325,422)        

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
    
    # Afficher bouton fight
    def fight_button(self):
        self.rect_radius(5, self.pink, 350, 450, 95, 75)
        self.text_c1("FIGHT", self.black, 370, 475)

    # Afficher bouton bag
    def bag_button(self):
        self.rect_radius(5, self.brown, 450, 450, 95, 75)
        self.text_c1("BAG", self.black, 480, 475)     

    # Afficher le bouton pokémon
    def pokemon_button(self):
        self.rect_radius(5, self.green, 550, 450, 95, 75)
        self.text_c1("POKEMON", self.black, 555, 475)

    # Afficher bouton run
    def run_button(self):
        self.rect_radius(5, self.blue, 650, 450, 95, 75)
        self.text_c1("RUN", self.black, 680, 475)      

    # Afficher rectangle noir
    def draw_hover_rectangle(self, btn_rect,  image_rect, image_path): 
        if self.is_mouse_over_button(btn_rect):
            pygame.draw.rect(self.screen, self.black, btn_rect, 4, 5) 

            # Pokeball pixeled
            self.img_pokemon("pokeball", image_path, image_rect[2], image_rect[3], image_rect[0], image_rect[1])

    # Affichage du hoover
    def rect_hover(self):
        self.draw_hover_rectangle(pygame.Rect(350, 450, 95, 75), (430, 445, 20, 20), r'images/images-play/play6.png')   # Fight
        self.draw_hover_rectangle(pygame.Rect(450, 450, 95, 75),(530, 445, 20, 20),r'images/images-play/play6.png' )    # Bag   
        self.draw_hover_rectangle(pygame.Rect(550, 450, 95, 75), (630, 445, 20, 20), r'images/images-play/play6.png')   # Pokemon
        self.draw_hover_rectangle(pygame.Rect(650, 450, 95, 75),(730, 445, 20, 20), r'images/images-play/play6.png')    # Run

    # Afficher barre vie ennemi
    def life1(self): 
        self.rect_radius(0,self.orange,112,102,110,10)

    # Affichere barre vie joueur
    def life2(self): 
        self.rect_radius(0,self.orange,650,400,110,10)

    def hp(self):
        # Rectangle noir côté gauche
        self.rect_radius(0,self.black,112,62,110,10)

        # PV coté gauche
        self.img_pokemon("rectangle_option",r'images/images-play/play8.png', 220,70,25,22)   

        # Rectangle noir HP côté droit
        self.rect_radius(0,self.black,650,350,110,10)

        # Rectangle noir EXP côté droit
        self.rect_radius(0,self.black,618,380,135,8)

        # PV coté droit
        self.img_pokemon("rectangle_option",r'images/images-play/play9.png',220,70,550,320)

        # Afficher nom du Pokémon au-dessus du rectangle HP
        with open('choix.json', 'r') as choix_file:
            choix_data = json.load(choix_file)

        name_pokemons = [pokemon["nom"] for pokemon in choix_data]

        if name_pokemons:
            current_pokemon_name = name_pokemons[0]
            self.text_c2(current_pokemon_name, self.black, 40, 30)
    
    # Lien au fichier JSON
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

    # Choisir aléatoirement pokemon ennemi  
    def enemy(self):
        with open('ennemi.json', 'r') as json_file:
            data = json.load(json_file)

        self.name_pokemons = [pokemon["nom"] for pokemon in data]
        self.random_pokemon = random.choice(self.name_pokemons)

        for pokemon in data:
            if pokemon["nom"] == self.random_pokemon:
                self.name_rival = pokemon["nom"]
                self.type_rival = pokemon["type"]
                self.level_rival = pokemon["niveau"]
                self.puissance_rivel = pokemon["puissance"]
                self.pv_rival = pokemon["pv"]
                self.defense_rival = pokemon["defense"]
        
        self.nouveau_pokemon = {
            "nom": self.name_rival,
            "type": self.type_rival,
            "niveau": self.level_rival,
            "puissance": self.puissance_rivel,
            "pv": self.pv_rival,
            "defense": self.defense_rival
        }
        try:
            with open('choix.json', 'r') as choix_file:
                choix_data = json.load(choix_file)
        except FileNotFoundError:
            choix_data = []

        choix_data.append(self.nouveau_pokemon)

        with open('choix.json', 'w') as choix_file:
            json.dump(choix_data, choix_file, indent=2)
    
    # Afficher pokemon ennemi   
    def rival(self):
        with open('choix.json', 'r') as choix_file:
            choix_data = json.load(choix_file)
        name_pokemons = [pokemon["nom"] for pokemon in choix_data]
        for name in name_pokemons:
            if name == "Spectrum":
                self.img_pokemon("Spectrum",r'images/images-enemy/enemy1.png', 200,209,400,105)
                self.text_c2(name, self.black, 590, 323)
    
            elif name == "Soporifix":
                self.img_pokemon("Soporifix",r'images/images-enemy/enemy2.png', 180,189,400,90)
                self.text_c2(name, self.black, 580, 322)

            elif name == "Manzai":
                self.img_pokemon("Manzai",r'images/images-enemy/enemy3.png', 200,209,430,80)
                self.text_c2(name, self.black, 620, 323)
                                
            elif name == "Magireve":
                self.img_pokemon("Magireve",r'images/images-enemy/enemy4.png', 200,209,430,80)
                self.text_c2(name, self.black, 590, 322)

            elif name == "Coupenotte":
                self.img_pokemon("Coupenotte",r'images/images-enemy/enemy5.png', 200,209,430,80)
                self.text_c1(name, self.black, 595, 328)

            elif name == "Charibari":
                self.img_pokemon("Charibari",r'images/images-enemy/enemy6.png',200,209,430,80)
                self.text_c2(name, self.black, 590, 322)
                
            elif name == "Carapuce":
                self.img_pokemon("Carapuce",r'images/images-enemy/enemy7.png',200,209,430,80)
                self.text_c2(name, self.black, 585, 323)

            elif name == "Poussacha":
                self.img_pokemon("Poussacha",r'images/images-enemy/enemy8.png',250,259,400,70)
                self.text_c2(name, self.black, 580, 323)

            elif name == "Chochodile":
                self.img_pokemon("Chochodile",r'images/images-enemy/enemy9.png', 250,259,400,70)
                self.text_c2(name, self.black, 580, 323)
   
    def play_fight_run(self):
        self.play_fight_running = True 
        self.run()

    def run(self):

        # Boucle principale du jeu
        self.play_fight_running = True
        self.enemy_chosen = False
        
        while self.play_fight_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    # Quit
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        pygame.quit() 

                    # Menu
                    elif self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                            self.play_fight_running = False                         

                    #  # Fight                      
                    # elif self.is_mouse_over_button (pygame.Rect(650, 450, 95, 75)): 

                    # # Bag                        
                    # elif self.is_mouse_over_button (pygame.Rect(650, 450, 95, 75)): 

                    # Pokemon
                    elif self.is_mouse_over_button (pygame.Rect(550, 450, 95, 75)): 
                            self.play_fight_running = False 
                            self.poke.pokedex_run()                      
                        
                    # Run                        
                    elif self.is_mouse_over_button (pygame.Rect(650, 450, 95, 75)):   
                        self.run_clicked = True
                        self.message_run()
                        self.c.cloud()
                        self.play_fight_running = False 

            if not self.run_clicked:
                self.message_start()
            else:
                self.message_run()

            # Afficher les éléments à l'écran
            self.background()
            self.rectangle()
            self.button_quit()
            self.button_menu()
            self.fight_button()
            self.pokemon_button()
            self.bag_button()
            self.run_button()
            self.rect_hover()
            self.choose()
            self.life1()
            self.life2()
            self.hp()
            
            if not self.enemy_chosen:
                self.enemy()
                self.enemy_chosen = True 

            self.rival()
            # Afficher les messages 
            # self.message_start()
            # self.message_fight()
            # self.message_run()
            # self.message_pokemon()
            # self.message_bag()
            # self.message_end_win()
            # self.message_end_lose()
               
            pygame.display.flip()
        
# game = Play_Fight()
# game.play_fight_run()
