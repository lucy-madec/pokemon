from global_def import Global
from info_pokemon import Info_pokemon
import pygame

class Pokedex(Global):
    def __init__(self):
        Global.__init__(self)
        self.pok_running = True
        self.info_pokemon = Info_pokemon()
                
    def background(self):
        background = pygame.image.load('images\images-pokedex\pokedex0.png')
        background = background.convert()
        self.screen.blit(background, (0,0))
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c3("POKEDEX",self.black,230,30)
        self.list = []

    def ajout_pokemon(self): 
        self.background()
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c3("POKEDEX",self.black,230,30)

        #Créer rectangles haut
        self.rect_radius(10,self.white,20, 250, 170, 120)
        self.rect_radius(10,self.white,220, 250, 170, 120)
        self.rect_radius(10,self.white,420, 250, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)

        #Créer rectangles bas
        self.rect_radius(10,self.white,20, 450, 170, 120)
        self.rect_radius(10,self.white,220, 450, 170, 120)
        self.rect_radius(10,self.white,420, 450, 170, 120)
        self.rect_radius(10,self.white,620, 450, 170, 120)

        #boutton de gauche
        self.rect_radius(10,self.yellow,20, 380, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((30,410),(50,390),(50,430)), 7)
        
        for name in self.add_name:
            self.list = self.add_name
            if name == "etourvol":
                self.img_pokemon("Etourvol",'images/images-add/add_pokemon1.png',70,89,75,255)
                self.text_c2("Etourvol",self.black,60,342)
                
            if name == "floravol":
                self.img_pokemon("Floravol",'images/images-add/add_pokemon2.png',100,119,265,242)
                self.text_c2("Floravol",self.black,265,342)

            if name == "lainergie":
                self.img_pokemon("Lainergie",'images/images-add/add_pokemon3.png',85,89,65,455)
                self.text_c2("Lainergie",self.black,50,542)
                
            if name == "luxio":
                self.img_pokemon("Luxio",'images/images-add/add_pokemon4.png',90,109,450,445)
                self.text_c2("Luxio",self.black,470,542)

            if name == "magicarpe":
                self.img_pokemon("Magicarpe",'images/images-add/add_pokemon5.png',90,99,255,452)
                self.text_c2("Magicarpe",self.black,245,542)

            if name == "phanpy":
                self.img_pokemon("Phanpy",'images/images-add/add_pokemon6.png',80,99,655,450)
                self.text_c2("Phanpy",self.black,670,542)
                
            if name == "psykokwak":
                self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',70,89,465,253)
                self.text_c2("Psykokwak",self.black,440,342)
                
            if name == "rondoudou":
                self.img_pokemon("Rondoudou",'images/images-add/add_pokemon8.png',70,79,670,258)
                self.text_c2("Rondoudou",self.black,642,342) 
            pygame.display.update()
            pygame.display.flip()
            
    def pokemon(self):
        #Créer rectangles haut
        self.rect_radius(10,self.white,20, 250, 170, 120)
        self.rect_radius(10,self.white,220, 250, 170, 120)
        self.rect_radius(10,self.white,420, 250, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)

        #Créer rectangles bas
        self.rect_radius(10,self.white,20, 450, 170, 120)
        self.rect_radius(10,self.white,220, 450, 170, 120)
        self.rect_radius(10,self.white,420, 450, 170, 120)
        self.rect_radius(10,self.white,620, 450, 170, 120)

        #Afficher pokemon pikachu
        self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',100,109,65,250)
        self.text_c2("pikachu",self.black,60,342)

        #Afficher pokemon capumain
        self.img_pokemon("capumain",'images\images-pokedex\pokedex2.png',115,119,45,440)
        self.text_c2("capumain",self.black,60,542)

        #Afficher pokemon evoli
        self.img_pokemon("evoli",'images\images-pokedex\pokedex3.png',90,99,265,252)
        self.text_c2("evoli",self.black,270,342)

        #Afficher pokemon marcacrin
        self.img_pokemon("marcacrin",'images\images-pokedex\pokedex4.png',130,129,437,420)
        self.text_c2("marcacrin",self.black,440,542)

        #Afficher pokemon salameche
        self.img_pokemon("salameche",'images\images-pokedex\pokedex5.png',110,119,255,430)
        self.text_c2("salameche",self.black,245,542)
        
        #Afficher pokemon medhyena
        self.img_pokemon("medhyena",'images\images-pokedex\pokedex6.png',260,269,585,320)
        self.text_c2("medhyena",self.black,655,542)
        
        #Afficher pokemon tiplouf
        self.img_pokemon("tiplouf",'images\images-pokedex\pokedex7.png',100,109,455,240)
        self.text_c2("tiplouf",self.black,460,342)
        
        #Afficher pokemon caninos
        self.img_pokemon("caninos",'images\images-pokedex\pokedex8.png',100,109,645,240)
        self.text_c2("caninos",self.black,655,342)
        
        #boutton changer de page
        self.rect_radius(10,self.yellow,740, 380, 50, 60)
        pygame.draw.polygon(self.screen, self.blue, ((770,410),(750,390),(750,430)), 7)
        pygame.display.update()
        pygame.display.flip()

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
        
    def pokedex_run(self):
        self.pok_running = True
        self.run()

    def run(self):
        poke2 = False
        self.background()
        self.pokemon()
        self.button_menu()

        while self.pok_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.pok_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    # # Vérifie si le bouton gauche de la souris est cliqué
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                    # Quitte le jeu lors du clic sur le bouton QUIT
                        pygame.quit() 
                        
                    if self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        print("menu")
                        self.running =  True
                        self.pok_running = False
                        

            #Test cliques sur les rectangles
                #Fleche droite           
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(740, 375, 50, 70)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        poke2 = True
                    if poke2 == True:
                        self.ajout_pokemon()
                
                #Fleche gauche
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 380, 50, 60)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        poke2 = False
                        self.pokemon()
                
                if poke2 == False:
                    #Rectangle du haut
                    self.button_menu() 
                    #Information pikachu         
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.pikachu()     
                                              
                    #Information evoli                            
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.evoli()

                    #Information tiplouf 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.tiplouf()

                    #Information caninos 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.caninos()

                    #Rectangle du bas        
                    #Information capumain                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.capumain()
                    #Information salameche 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.salameche()
                            
                    #Information Marcacrin 
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.marcacrin()

                    #Information Medhyena        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.medhyena()

                if poke2 == True:
                    self.button_menu()
                    self.button_quit() 
                    #Rectangle du haut
                    #Information etourvol           
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.etourvol()

                    #Information floravol                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.floravol()

                    #Information psykokwak
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.psykokwak()
                            
                    #Information roudoudou
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 250, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.rondoudou()


                    #Rectangle du bas    
                    #Information lainergie             
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(20, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.lainergie()
                            
                    #Information magicarpe
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(220, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.salameche()
                            
                    #Information Luxio
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(420, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.luxio()

                    #Information phanpy        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(620, 450, 170, 120)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            self.info_running = True
                            self.info_pokemon.phanpy()


            self.button_menu()
            self.button_quit()
            pygame.display.flip()
            self.clock.tick(30)

# test = Pokedex()
# test.pokedex_run()
