from global_def import Global
import pygame, json

class Play_Fight(Global):

    # Appelle le constructeur de la classe parent Global
    def __init__(self):
        
        Global.__init__(self)
        self.play_fight_running = True
     
    # Afficher l'image de fond
    def background(self):
        self.img_back("Background", r"images/images-play/play1.jpg")

    def message_start(self): 
        self.text_c2("What will you do ? ", self.black, 70, 475)  

    # Afficher message si le joueur choisit l'option "RUN"
    def message_run(self): 
        self.text_c1("C'est trop dangereux ici,", self.black, 70, 455)
        self.text_c1("vous décidez de fuir ", self.black, 70, 475)
        self.text_c1(" le combat.", self.black, 70, 495)

    # Afficher message si le joueur choisit l'option "FIGHT"
    def message_fight(self):
        self.text_c1("Vous avez choisi de ", self.black, 85, 455)
        self.text_c1("rester et de défier", self.black, 85, 475) 
        self.text_c1("le Pokémon sauvage.", self.black, 85, 495)   

    # Afficher message si le joueur choisit l'option "BAG"
    def message_bag(self): 
        self.text_c1("Le joueur fouille dans ", self.black, 80, 455)
        self.text_c1("son sac à la recherche", self.black, 80, 475)
        self.text_c1("d'objets utiles.", self.black, 80, 495) 
 
    # Afficher message si le joueur choisit l'option "POKEMON"
    def message_pokemon(self): 
        self.text_c1("Vous envoyez un autre", self.black, 80, 465) 
        self.text_c1("Pokémon au combat.", self.black, 80, 495)   
     
    # Afficher message si le joueur gagne
    def message_end_win(self): 
        self.text_c2("Félicitations !", self.black, 85, 445)  
        self.text_c1("Vous avez remporté ", self.black, 85, 475)
        self.text_c1("la victoire.", self.black, 85, 495)    

    # Afficher message si le joueur perd
    def message_end_lose(self): 
        self.text_c6("Vous avez été ", self.black, 105, 465)  
        self.text_c2("vaincu ! ", self.black, 130, 485)      

    def rectangle(self): 

        # Rectangle blanc texte
        self.rect_radius(10,self.white,55,430,235,115) 

        # Rectangle texte
        self.img_pokemon("rectangle_texte",r'images/images-play/play7.png', 250,129,50,420)    

        # Rectangle 4 actions
        self.rect_radius(10,self.white,335,430,430,115)          
        self.img_pokemon("rectangle_option",r'images/images-play/play5.png',445,129,325,422)        

    # Affiche le bouton QUIT
    def button_quit(self):
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)

    # Affiche le bouton BACK
    def button_menu(self):
      
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)

    # Vérifie si la souris est au-dessus du bouton
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)    
    
    # Affiche le bouton d'attaque
    def fight_button(self):
        self.rect_radius(5, self.pink, 350, 450, 95, 75)
        self.text_c1("FIGHT", self.black, 370, 475)
    
    def bag_button(self):
        self.rect_radius(5, self.brown, 450, 450, 95, 75)
        self.text_c1("BAG", self.black, 480, 475)     

    # Affiche le bouton de défense
    def pokemon_button(self):
        self.rect_radius(5, self.green, 550, 450, 95, 75)
        self.text_c1("POKEMON", self.black, 555, 475)

    def run_button(self):
        self.rect_radius(5, self.blue, 650, 450, 95, 75)
        self.text_c1("RUN", self.black, 680, 475)      

    def draw_hover_rectangle(self, btn_rect,  image_rect, image_path): 
        # Afficher le rectangle noir au survol de la souris
        if self.is_mouse_over_button(btn_rect):
            pygame.draw.rect(self.screen, self.black, btn_rect, 4, 5)   
             # Pokeball pixeled
            self.img_pokemon("pokeball", image_path, image_rect[2], image_rect[3], image_rect[0], image_rect[1])
    
    def rect_hover(self):   

        self.draw_hover_rectangle(pygame.Rect(350, 450, 95, 75), (430, 445, 20, 20), r'images/images-play/play6.png')  # Fight
        self.draw_hover_rectangle(pygame.Rect(450, 450, 95, 75),(530, 445, 20, 20),r'images/images-play/play6.png' )  # Bag   
        self.draw_hover_rectangle(pygame.Rect(550, 450, 95, 75), (630, 445, 20, 20), r'images/images-play/play6.png')  # Pokemon
        self.draw_hover_rectangle(pygame.Rect(650, 450, 95, 75),(730, 445, 20, 20), r'images/images-play/play6.png')  # Run

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
                
    def pokemon(self): 
              # Afficher pokemon pikachu
        self.img_pokemon("pikachu",r'images\images-pokedex\pokedex1.png',100,109,65,250)
        self.text_c2("pikachu",self.black,60,342)
   
    def play_fight_run(self):
        self.play_fight_running = True 
        self.run()
    
    def run(self):
        # La boucle principale du jeu
        self.play_fight_running = True
        while self.play_fight_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    # Quitte le programme lorsque la fenêtre est fermée
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        pygame.quit() 
                        
                    elif self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        self.play_fight_running = False 
           
            # Affiche les éléments à l'écran
            self.background()
            self.rectangle()
            self.button_quit()
            self.button_menu()
            self.fight_button()
            self.pokemon_button()
            self.bag_button()
            self.run_button()
            self.rect_hover()
            self.hp()

            # Afficher les messages 
            self.message_start()
            # # self.message_fight()
            # # self.message_run()
            # self.message_pokemon()
            # self.message_bag()
            # self.message_end_win()
            # self.message_end_lose()
               
            pygame.display.flip()
            
     

# Créer une instance de la classe Play_Fight et exécute le jeu
        
# game = Play_Fight()
# game.play_fight_run()
