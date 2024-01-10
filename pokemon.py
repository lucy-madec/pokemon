from global_def import Global
import pygame,sys

class Pokemon(Global):

    def __init__(self):
        Global.__init__(self)
    
    # Faire le Background
    def background(self):
        self.img_back("Background", "images/images-partie/pokedex105.jpg")

        rect_width, rect_height = 200, 50
        rect_x = self.screen_width - rect_width - 10
        rect_y = 10
        
        # Dessiner le rectangle avec les coins arrondis
        pygame.draw.rect(self.screen, self.white, (rect_x, rect_y, rect_width, rect_height), border_radius=10)

        # Ajouter du texte centré dans le rectangle
        font = pygame.font.Font(None, 30)
        text = font.render("QUIT", True, self.black)
        text_rect = text.get_rect(center=(rect_x + rect_width //2, rect_height //2))
        self.screen.blit(text, text_rect)

        # Récupérer de la position de la souris
        mouse_x, mouse_y, = pygame.mouse.get_pos()

        # Vérifier si le clic de la souris est à l'intérieur du rectangle
        if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
            pygame.draw.rect(self.screen, (200, 200, 200), (rect_x, rect_y, rect_width, rect_height), border_radius=10)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Si le bouton gauche de la souris est cliqué, quitter le programme
                    if event.button == 1:
                        pygame.quit()
                        sys.exit()
    
    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.background()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

if __name__ == "__main__":
    game = Pokemon()
    game.run()