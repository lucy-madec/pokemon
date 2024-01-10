from global_def import Global
import pygame

class Pokedex(Global):
    def __init__(self):
        Global.__init__(self)

        
    def background(self):
        background = pygame.image.load('images\images-pokedex\pokedex1020.png')
        background = background.convert()
        self.screen.blit(background, (0,0))


    def pokemon(self):
        self.rect_radius(10,self.white,200, 40, 440, 80)
        self.text_c1("POKEDEX",self.black,230,30)

        #Créer rectangles haut
        self.rect_radius(10,self.white,20, 250, 170, 120)
        self.rect_radius(10,self.white,220, 250, 170, 120)
        self.rect_radius(10,self.white,420, 250, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)
    
        #Créer rectangles bas
        self.rect_radius(10,self.white,20, 450, 170, 120)
        self.rect_radius(10,self.white,220, 450, 170, 120)
        self.rect_radius(10,self.white,420, 450, 170, 120)
        self.rect_radius(10,self.white,620, 250, 170, 120)
         
        self.rect_radius(10,self.white,20, 250, 170, 120)
        #Afficher pokemon pikachu
        self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',110,119,45,245)
        self.text_c2("pikachu",self.black,60,345)

        #Afficher pokemon posipi
        self.img_pokemon("posipi",'images\images-pokedex\pokedex3.png',115,119,45,440)
        self.text_c2("posipi",self.black,70,545)

        #Afficher pokemon pyroli
        self.img_pokemon("pyroli",'images\images-pokedex\pokedex4.png',120,129,245,242)
        self.text_c2("posipi",self.black,270,345)

        #Afficher pokemon noctali
        self.img_pokemon("noctali",'images\images-pokedex\pokedex6.png',150,159,425,422)
        self.text_c2("noctali",self.black,465,545)

        #Afficher pokemon salamèche
        self.img_pokemon("salamèche",'images\images-pokedex\pokedex5.png',120,129,255,422)
        self.text_c2("salamèche",self.black,245,545)

        pygame.display.update()
        pygame.display.flip()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.background()
            self.pokemon()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
            
pokedex1 = Pokedex()
pokedex1.run()
