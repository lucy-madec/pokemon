from global_def import Global
import pygame
import sys

class Play_Fight(Global):

    def __init__(self):
        # Appelle le constructeur de la classe parent Global
        Global.__init__(self)
        # Charge l'image pour l'attaque
        self.attack_image = pygame.image.load("images/images-partie/partie2.png")

    def background(self):
        # Affiche l'image de fond
        self.img_back("Background", "images/images-partie/partie1.jpg")

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
    
    def power_attack(self):
        # Affiche le bouton d'attaque
        self.rect_radius(5, self.orange, 550, 400, 90, 40)
        self.text_c1("ATTACK", self.black, 560, 410)
        self.screen.blit(self.attack_image, (560, 460))

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
            self.button_quit()
            self.button_back()
            self.power_attack()
            pygame.display.flip()
            self.clock.tick(30)
            
        pygame.quit()

# Crée une instance de la classe Play_Fight et exécute le jeu
game = Play_Fight()
game.run()
