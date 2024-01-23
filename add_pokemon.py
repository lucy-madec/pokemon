from global_def import Global
import pygame, json

class Add_Pokemon(Global):
    def __init__(self):
        Global.__init__(self)
        self.add_running = True
        self.page = 1
        self.poke2 = False

    def background(self):
        self.img_back("background",r'images/images-add/add_pokemon10.jpg')

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
        # Afficher titre "CLICK TO ADD A POKEMON"
        self.rect_radius(10,self.white,200, 40, 400, 80)
        self.text_c5("CLICK TO ADD A POKEMON",self.black,220,65)

        # Créer rectangles haut
        self.rect_radius(10,self.white,100, 130, 600, 100) # Etourvol
        self.rect_radius(10,self.white,100, 250, 600, 100) # Floravol
        self.rect_radius(10,self.white,100, 370, 600, 100) # Lainergie
        self.rect_radius(10,self.white,100, 490, 600, 100) # Luxio

        # Afficher pokemon Etourvol
        self.img_pokemon("Etourvol",r'images/images-add/add_pokemon1.png',70,89,150,135)
        self.text_c2("Etourvol",self.black,390,142)
        
        # Afficher pokemon Floravol
        self.img_pokemon("Floravol",r'images/images-add/add_pokemon2.png',100,119,150,240)
        self.text_c2("Floravol",self.black,390,255)

        # Afficher pokemon Lainergie
        self.img_pokemon("Lainergie",r'images/images-add/add_pokemon3.png',85,89,150,373)
        self.text_c2("Lainergie",self.black,390,380)

        # Afficher pokemon Luxio
        self.img_pokemon("Luxio",r'images/images-add/add_pokemon4.png',90,109,150,483)
        self.text_c2("Luxio",self.black,390,500)

        # Bouton changer de page
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
        self.text_c2("Magicarpe",self.black,390,142)
        
        # Afficher pokemon Phanpy
        self.img_pokemon("Phanpy",r'images/images-add/add_pokemon6.png',70,89,150,255)
        self.text_c2("Phanpy",self.black,390,255)
        
        # Afficher pokemon Psykokwak
        self.img_pokemon("Psykokwak",r'images/images-add/add_pokemon7.png',85,89,150,373)
        self.text_c2("Psykokwak",self.black,390,380)
        
        # Afficher pokemon Roudoudou
        self.img_pokemon("Roudoudou",r'images/images-add/add_pokemon8.png',60,89,150,493)
        self.text_c2("Roudoudou",self.black,390,500) 

        # Bouton de gauche
        self.rect_radius(10,self.yellow,20, 380, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((30,410),(50,390),(50,430)), 7)
        
        pygame.display.update()
        pygame.display.flip()

    def draw_hover_rectangle(self, btn_rect):
        # Vérifier si la souris est au-dessus du rectangle
        if self.is_mouse_over_button(btn_rect):
            # Afficher le contour du rectangle en jaune au survol de la souris
            pygame.draw.rect(self.screen, self.yellow, btn_rect, 4, 5)
        else:
            # Effacer l'effet de survol si la souris n'est pas au-dessus du bouton
            pygame.draw.rect(self.screen, self.white, btn_rect, 4, 5)            

    # Créer le contour du rectangle en jaune au survol de la souris
    def rect_hover(self):
        self.draw_hover_rectangle(pygame.Rect(100, 130, 600, 100))  # Etourvol et Magicarpe
        self.draw_hover_rectangle(pygame.Rect(100, 250, 600, 100))  # Floravol et Phanpy
        self.draw_hover_rectangle(pygame.Rect(100, 370, 600, 100))  # Lainergie et Psykokwak
        self.draw_hover_rectangle(pygame.Rect(100, 490, 600, 100))  # Luxio et Roudoudou
        
    # Afficher le bouton QUIT
    def button_quit(self):
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)

    # Afficher le bouton BACK
    def button_menu(self):
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("MENU", self.black, 650, 13)

    # Vérifier si la souris est au-dessus du bouton
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)

    def add_pokemon_run(self):
        self.add_running = True
        self.run()

    # Boucle principale
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

                    # Clic sur la flèche gauche et droite
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
                        # Rectangles Page 1       
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
                        # Rectangles Page 2
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

            self.rect_hover()
            self.button_menu()
            self.button_quit()

            pygame.display.update()
            pygame.display.flip()
            self.clock.tick(30)

test_add_pokemon = Add_Pokemon()
test_add_pokemon.add_pokemon_run()