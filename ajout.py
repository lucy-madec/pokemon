from global_def import Global
from pikachu import Pikachu
import pygame

class Pokedex(Global):
    def __init__(self):
        Global.__init__(self)
        self.pikachu = Pikachu()

    def background(self):
        background = pygame.image.load('images/images-play/add_pokemon1.jpg')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def pokemon(self):
        
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c1("AJOUTER VOTRE POKÉMON",self.black,230,30)

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
        self.img_pokemon("pikachu",'images/images-play/Etourvol.png',110,119,45,245)
        self.text_c2("pikachu",self.black,60,345)

        #Afficher pokemon posipi
        self.img_pokemon("posipi",'images/images-play/Lainergie.png',115,119,45,440)
        self.text_c2("posipi",self.black,70,545)

        #Afficher pokemon pyroli
        self.img_pokemon("pyroli",'images/images-play/Floravol.png',120,129,245,242)
        self.text_c2("pyroli",self.black,270,345)

        #Afficher pokemon noctali
        self.img_pokemon("noctali",'images/images-play/Etourvol.png',150,159,425,422)
        self.text_c2("noctali",self.black,465,548)

        #Afficher pokemon salamèche
        self.img_pokemon("salamèche",'images/images-play/Magicarpe.png',120,129,255,422)
        self.text_c2("salamèche",self.black,245,545)
        
        #Afficher pokemon medhyena
        self.img_pokemon("medhyena",'images/images-play/Phanpy.png',290,299,570,300)
        self.text_c2("medhyena",self.black,655,545)
        
        #Afficher pokemon dracaufeu
        self.img_pokemon("dracaufeu",'images/images-play/Psykokwak.png',130,139,455,223)
        self.text_c2("dracaufeu",self.black,445,347)
        
        #Afficher pokemon caninos
        self.img_pokemon("caninos",'images/images-play/Rondoudou.png',110,119,640,235)
        self.text_c2("caninos",self.black,655,347)
        
        #boutton changer de page
        self.rect_radius(10,self.white,740, 375, 50, 70)
        pygame.draw.lines(self.screen,self.black,True, ((770,410),(750,390),(750,430)),5)
        
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

