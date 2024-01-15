from global_def import Global
import pygame

class Play_Fight(Global):

    # Appeller le constructeur de la classe parent Global
    def __init__(self):
  
        Global.__init__(self)

    # Afficher image de fond
    def background(self):    
        self.img_back("Background", "images/images-play/play1.jpg")

    # Afficher rectangle blanc texte
    def rectangle(self):     
        self.rect_radius(10,self.white,55,430,240,115)  
       
        # Rectangle texte
        self.img_pokemon("rectangle_texte",'images/images-play/play5.png', 250,129,50,420)    

        # Texte action à gauche
        self.text_c2("What will you do ? ", self.black, 70, 475)       

        # Rectangle 4actions
        self.rect_radius(10,self.white,335,430,430,115)  
        
        self.img_pokemon("rectangle_option",'images/images-play/play5.png',445,129,325,422)        
       
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
    
    # Afficher bouton d'attaque
    def fight_button(self):        
        self.rect_radius(5, self.pink, 350, 450, 95, 75)
        self.text_c1("FIGHT", self.black, 370, 475)

    # Afficher bouton bag
    def bag_button(self):
        self.rect_radius(5, self.brown, 450, 450, 95, 75)
        self.text_c1("BAG", self.white, 480, 475)     

    # Afficher bouton Pokémon
    def pokemon_button(self):       
        self.rect_radius(5, self.green, 550, 450, 95, 75)
        self.text_c1("POKEMON", self.white, 555, 475)

    # Affiche le bouton run
    def run_button(self):
        self.rect_radius(5, self.blue, 650, 450, 95, 75)
        self.text_c1("RUN", self.white, 680, 475)      

    # Afficher rectangle noir au survol de la souris
    def draw_hover_rectangle(self, btn_rect,  image_rect, image_path): 
        if self.is_mouse_over_button(btn_rect):
            pygame.draw.rect(self.screen, self.black, btn_rect, 4, 5)   

             # Image Pokeball pixeled
            self.img_pokemon("pokeball", image_path, image_rect[2], image_rect[3], image_rect[0], image_rect[1])
            
    # Afficher rectangle noir au survol de la souris
    def rect_hover(self):  

        # Fight
        self.draw_hover_rectangle(pygame.Rect(350, 450, 95, 75), (430, 445, 20, 20), 'images/images-play/play6.png') 

        # Bag   
        self.draw_hover_rectangle(pygame.Rect(450, 450, 95, 75),(530, 445, 20, 20),'images/images-play/play6.png' )  

        # Pokemon
        self.draw_hover_rectangle(pygame.Rect(550, 450, 95, 75), (630, 445, 20, 20), 'images/images-play/play6.png')  

        # Run
        self.draw_hover_rectangle(pygame.Rect(650, 450, 95, 75),(730, 445, 20, 20), 'images/images-play/play6.png')  
    
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

            # Afficher éléments écran
            self.background()
            self.rectangle()
            self.button_quit()
            self.button_menu()
            self.fight_button()
            self.pokemon_button()
            self.bag_button()
            self.run_button()
            self.rect_hover()    
            
            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()

# Créer instance Play_Fight exécute le jeu
game = Play_Fight()
game.run()