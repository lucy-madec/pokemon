import pygame,sys

class Pokemon:
    def __init__(self, width, height): 
        pygame.init()
        self.width = width
        self.height = height
        self.window_size = (self.width, self.height)

        # Initialisation de Pygame
        pygame.init()

        # Création de la fenêtre
        self.window = pygame = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Ma fenêtre Pygame")
    
    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()

            # Remplissage de la fenêtre avec un fond blanc
            self.window.fill((255, 255, 255))

            # Rafraîchissement de l'affichage
            pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()

# Utilisation de la classe
if __name__ == "__main__":
    pygame_window = Pokemon(800, 600)
    pygame_window.main_loop()