from global_def import Global
from info_pokemon import Info_pokemon
import pygame
# Test

class Pokedex(Global):
    def __init__(self):
        Global.__init__(self)
        self.info_pokemon = Info_pokemon()

    def background(self):
        background = pygame.image.load('images/images-add/add_pokemon1a.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def logo(self):
        self.img_pokemon("tagline",'images/images-add/add_pokemon9.png',175,100,340,110)     

    def pokemon(self):
        
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c5("ADD POKEMON",self.black,220,45)
        
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
        
        #Afficher pokemon Etourvol
        self.img_pokemon("Etourvol",'images/images-add/add_pokemon1.png',70,89,75,255)
        self.text_c2("Etourvol",self.black,60,342)

        #Afficher pokemon Lainergie
        self.img_pokemon("Lainergie",'images/images-add/add_pokemon3.png',85,89,65,455)
        self.text_c2("Lainergie",self.black,50,542)

        #Afficher pokemon Floravol
        self.img_pokemon("Floravol",'images/images-add/add_pokemon2.png',100,119,265,242)
        self.text_c2("Floravol",self.black,265,342)

        #Afficher pokemon Luxio
        self.img_pokemon("Luxio",'images/images-add/add_pokemon4.png',90,109,450,445)
        self.text_c2("Luxio",self.black,470,542)

        #Afficher pokemon Magicarpe
        self.img_pokemon("Magicarpe",'images/images-add/add_pokemon5.png',90,99,255,452)
        self.text_c2("Magicarpe",self.black,245,542)
        
        #Afficher pokemon Phanpy
        self.img_pokemon("Phanpy",'images/images-add/add_pokemon6.png',80,99,655,450)
        self.text_c2("Phanpy",self.black,670,542)
        
        #Afficher pokemon Psykokwak
        self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',70,89,465,253)
        self.text_c2("Psykokwak",self.black,440,342)
        
        #Afficher pokemon Rondoudou
        self.img_pokemon("Rondoudou",'images/images-add/add_pokemon8.png',70,79,670,258)
        self.text_c2("Rondoudou",self.black,642,342)       
        
        pygame.display.update()
        pygame.display.flip()

    def pokedex_run(self):
        self.run()

    def run(self):
        self.background()  
        self.logo()          
        self.pokemon()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #Test cliques sur les rect                    
        
                #Rectangle du haut        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.etourvol()
                        # self.lst_name("Etourvol")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.floravol()
                        #good
                        # self.lst_name("Lainergie")


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.floravol()
                        # self.lst_name("Floravol")


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.luxio()
                        # self.lst_name("Luxio")


                #Rectangle du bas        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.lainergie()
                        #good
                        # self.lst_name("Magicarpe")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.magicarpe()
                        # self.info_pokemon.phanpy()
                        # self.lst_name("Phanpy")


                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.psykokwak()
                        # self.lst_name("Psykokwak")

          
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.info_pokemon.rondoudou()
                        # self.lst_name("Rondoudou")

                                                                                

            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

ajout = Pokedex()
ajout.pokedex_run()

