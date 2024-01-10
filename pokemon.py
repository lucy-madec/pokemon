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

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            self.screen.blit(background_image, (0, 0)) # Affiche l'image en position

            pygame.display.flip()
            self.clock.tick(60)
    
    def run(self):
        self.display_game()

        pygame.quit()

if __name__ == "__main__":
    game = Pokemon()
    game.run()