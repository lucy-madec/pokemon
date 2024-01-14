from global_def import Global
import pygame
import sys

class Play_Fight(Global):

    def __init__(self):
        # Appelle le constructeur de la classe parent Global
        Global.__init__(self)
    
    def background(self):
        # Affiche l'image de fond
        self.img_back("Background", "images/images-play/play1.jpg")

    def rectangle(self): 

        # Rectangle blanc texte
        self.rect_radius(10,self.white,55,430,240,115)  
       

        # Rectangle texte
        self.img_pokemon("rectangle_texte",'images/images-play/play5.png', 250,129,50,422)    

        self.text_c2("What will you do ? ", self.black, 70, 475)       

        # Rectangle 4actions

        self.rect_radius(10,self.white,335,430,430,115)  
        
        self.img_pokemon("rectangle_option",'images/images-play/play5.png',445,129,325,422)        
       
    def button_quit(self):
        # Affiche le bouton QUIT
        self.rect_radius(5, self.white, 720, 10, 70, 25)
        self.text_c1("QUIT", self.black, 733, 13)
    
    def button_back(self):
        # Affiche le bouton BACK
        self.rect_radius(5, self.white, 640, 10, 70, 25)
        self.text_c1("BACK", self.black, 650, 13)

    def is_mouse_over_button(self, button_rect):
        # Vérifie si la souris est au-dessus du bouton
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos)    
    
    def fight_button(self):
        # Affiche le bouton d'attaque
        self.rect_radius(5, self.pink, 350, 450, 95, 75)
        self.text_c1("FIGHT", self.black, 370, 475)
    
    def bag_button(self):
        self.rect_radius(5, self.brown, 450, 450, 95, 75)
        self.text_c1("BAG", self.white, 480, 475)     

    def pokemon_button(self):
        # Affiche le bouton de défense
        self.rect_radius(5, self.green, 550, 450, 95, 75)
        self.text_c1("POKEMON", self.white, 555, 475)

    def run_button(self):
        self.rect_radius(5, self.blue, 650, 450, 95, 75)
        self.text_c1("RUN", self.white, 680, 475)      

    def draw_hover_rectangle(self, btn_rect,  image_rect, image_path): 
        # Afficher le rectangle noir au survol de la souris
        if self.is_mouse_over_button(btn_rect):
            pygame.draw.rect(self.screen, self.black, btn_rect, 4, 5)   
             # Pokeball pixeled
            self.img_pokemon("pokeball", image_path, image_rect[2], image_rect[3], image_rect[0], image_rect[1])
            
    
    def rect_hover(self):   

        self.draw_hover_rectangle(pygame.Rect(350, 450, 95, 75), (430, 445, 20, 20), 'images/images-play/play6.png')  # Fight
      
        self.draw_hover_rectangle(pygame.Rect(450, 450, 95, 75),(530, 445, 20, 20),'images/images-play/play6.png' )  # Bag   

        self.draw_hover_rectangle(pygame.Rect(550, 450, 95, 75), (630, 445, 20, 20), 'images/images-play/play6.png')  # Pokemon

        self.draw_hover_rectangle(pygame.Rect(650, 450, 95, 75),(730, 445, 20, 20), 'images/images-play/play6.png')  # Run
    
    def run(self):
        # La boucle principale du jeu
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quitte le programme lorsque la fenêtre est fermée
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Vérifie si le bouton gauche de la souris est cliqué
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                        # Quitte le jeu lors du clic sur le bouton QUIT
                        self.running = False
                    elif self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        pass

            # Affiche les éléments à l'écran
            self.background()
            self.rectangle()
            self.button_quit()
            self.button_back()
            self.fight_button()
            self.pokemon_button()
            self.bag_button()
            self.run_button()
            self.rect_hover()    
            
            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()

# Crée une instance de la classe Play_Fight et exécute le jeu
game = Play_Fight()
game.run()
