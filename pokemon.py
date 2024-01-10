import pygame,sys
class Pokemon:

    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pokémon")
        self.clock = pygame.time.Clock()
    
    def display_game(self):
        running = True
        background_image = pygame.image.load("images/images-partie/pokedex105.jpg").convert()

        # Couleurs
        white = (255, 255, 255)
        black = (0, 0, 0)

        # Rectangle et texte
        rect_width, rect_height = 200, 50
        rect_x = self.screen_width - rect_width - 10
        rect_y = 10
        
        option_radius = 10


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Récupération de la position de la souris
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    # Vérification si le clic de la souris est à l'intérieur du rectangle
                    if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                        running = False
            
            self.screen.blit(background_image, (0, 0))
            
            # Dessin du rectangle avec les coins arrondis
            pygame.draw.rect(self.screen, white, (rect_x, rect_y, rect_width, rect_height), border_radius=option_radius)

            # Vérification si la souris est sur le rectangle
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if rect_x < mouse_x < rect_x + rect_width and rect_y < mouse_y < rect_y + rect_height:
                pygame.draw.rect(self.screen, (200, 200, 200), (rect_x, rect_y, rect_width, rect_height), border_radius=option_radius)

            # Ajout du texte centré dans le rectangle
            font = pygame.font.Font(None, 30)
            text = font.render("QUIT", True, black)
            text_rect = text.get_rect(center=(rect_x + rect_width //2, rect_height //2))
            self.screen.blit(text, text_rect)


            pygame.display.flip()
            self.clock.tick(60)
    
    def run(self):
        self.display_game()

        pygame.quit()

if __name__ == "__main__":
    game = Pokemon()
    game.run()