from global_def import Global
import pygame

class Pikachu(Global):
    def __init__(self):
        Global.__init__(self)

    def pikachu(self):
        background = pygame.image.load('images\images-pokedex\pokedex1020.png')
        background = background.convert()
        self.screen.blit(background, (0,0))

    def pikachu_run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.pikachu()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()

