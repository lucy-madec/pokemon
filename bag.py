# Test
from global_def import Global
import pygame
class Bag(Global):
    def __init__(self): 
            Global.__init__(self)
            self.bag_running = True
        
    # Initialisation de Pygame
    pygame.init()

    # Afficher background
    def background(self):
        self.img_back("background", r"images/images-play/Play13.png")

    # Afficher texte
    def text(self):
        self.text_c5("SORRY !",self.black, 470, 495)
        self.text_c6("There are no items available in the bag...", self.black, 315, 530)

    # Afficher zone texte
    def rect(self):
        self.rect_radius(10,self.white,300,475,430,95)
        
    # Afficher bouton QUIT
    def button_quit(self):
        button_rect = pygame.Rect(720, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):
            self.rect_radius(5, self.yellow, 720, 10, 70, 25)
            self.text_c1("QUIT", self.black, 733, 13)
        else:
            self.rect_radius(5, self.white, 720, 10, 70, 25)
            self.text_c1("QUIT", self.black, 733, 13)

    # Afficher bouton MENU
    def button_menu(self):  
        button_rect = pygame.Rect(640, 10, 70, 25)
        if self.is_mouse_over_button(button_rect):    
            self.rect_radius(5, self.yellow, 640, 10, 70, 25)
            self.text_c1("MENU", self.black, 650, 13)
        else:
            self.rect_radius(5, self.white, 640, 10, 70, 25)
            self.text_c1("MENU", self.black, 650, 13)
    
    # Vérifier si souris au-dessus du bouton
    def is_mouse_over_button(self, button_rect):
        mouse_pos = pygame.mouse.get_pos()
        return button_rect.collidepoint(mouse_pos) 
    
    def bag_run(self):
        self.bag_running = True
        self.run()

    
    def run(self):

        while self.bag_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bag_running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:                   
                    # Quit
                    if self.is_mouse_over_button(pygame.Rect(720, 10, 70, 25)):
                            pygame.quit() 

                    # Menu
                    elif self.is_mouse_over_button(pygame.Rect(640, 10, 70, 25)):
                        self.bag_running = False

            # Remplir la fenêtre avec la couleur gris
            self.background()
            self.rect()
            self.text()
            self.button_quit()
            self.button_menu()

            # Mettre à jour l'affichage
            pygame.display.flip()
            pygame.display.update()

        # Quand la boucle est terminée, quitter Pygame
    # pygame.quit()

# test = Bag()
# test.bag_run()