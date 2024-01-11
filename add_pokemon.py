from global_def import Global
from pikachu import Pikachu
import pygame

class Pokedex(Global):
    def __init__(self):
        Global.__init__(self)
        self.pikachu = Pikachu()

    def background(self):
        background = pygame.image.load('images/images-add/add_pokemon1a.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def logo(self):
        self.img_pokemon("Etourvol",'images/images-add/add_pokemon1.png',70,89,75,255)

        def img_pokemon(self,name,path,a,b,x,y,):
        name = pygame.image.load(path)
        name = name.convert_alpha()
        name = pygame.transform.scale(name,(a,b))        
        self.screen.blit(name,(x,y))

     


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
        self.img_pokemon("Lainergie",'images/images-add/add_pokemon3.png',85,89,45,430)
        self.text_c2("Lainergie",self.black,70,542)

        #Afficher pokemon Floravol
        self.img_pokemon("Floravol",'images/images-add/add_pokemon2.png',120,129,245,242)
        self.text_c2("Floravol",self.black,270,342)

        #Afficher pokemon Luxio
        self.img_pokemon("Luxio",'images/images-add/add_pokemon4.png',150,159,425,422)
        self.text_c2("Luxio",self.black,465,542)

        #Afficher pokemon Magicarpe
        self.img_pokemon("Magicarpe",'images/images-add/add_pokemon5.png',120,129,255,422)
        self.text_c2("Magicarpe",self.black,245,542)
        
        #Afficher pokemon Phanpy
        self.img_pokemon("Phanpy",'images/images-add/add_pokemon6.png',80,99,655,450)
        self.text_c2("Phanpy",self.black,655,542)
        
        #Afficher pokemon Psykokwak
        self.img_pokemon("Psykokwak",'images/images-add/add_pokemon7.png',130,139,455,223)
        self.text_c2("Psykokwak",self.black,445,342)
        
        #Afficher pokemon Rondoudou
        self.img_pokemon("Rondoudou",'images/images-add/add_pokemon8.png',110,119,640,235)
        self.text_c2("Rondoudou",self.black,655,342)       
        
        pygame.display.update()
        pygame.display.flip()

    def pokedex_run(self):
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #Test cliques sur les rect
                #Fleche
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(740, 375, 50, 70)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False

                #Rectangle du haut        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        self.pikachu.pikachu_run()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 250, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False

                #Rectangle du bas        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(20, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(220, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(420, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    button_rect = pygame.Rect(620, 450, 170, 120)
                    if button_rect.collidepoint(mouse_x, mouse_y):
                        running = False     
                                                                                    
            self.background()            
            self.pokemon()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

ajout = Pokedex()
ajout.pokedex_run()

