from global_def import Global
import pygame
import random

pygame.init()

class Lightning (Global):

    def __init__(self):
        Global.__init__(self)       

    def lightning(self):            
  
        eclair_image = pygame.image.load("images/images-play/Play10.png").convert_alpha()
        eclair_rect = eclair_image.get_rect()

        # Variables pour le mouvement de l'éclair
        deplacement_x = 0
        deplacement_y = 0

        background = self.screen.copy()

        # Boucle principale
        quitter = False
        horloge = pygame.time.Clock()

        while not quitter:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitter = True

            self.screen.blit(background, (0, 0))
            
            # Déplacement de l'éclair
            deplacement_x = random.randint(-10, 5)
            deplacement_y = random.randint(-10, 5)

            eclair_rect.x += deplacement_x
            eclair_rect.y += deplacement_y

            # Limiter déplacements de l'éclair
            if eclair_rect.x < 0:
                eclair_rect.x = 0
            elif eclair_rect.x > self.screen_width - eclair_rect.width:
                eclair_rect.x = self.screen_width - eclair_rect.width

            if eclair_rect.y < 0:
                eclair_rect.y = 0
            elif eclair_rect.y > self.screen_height - eclair_rect.height:
                eclair_rect.y = self.screen_height - eclair_rect.height

            # Afficher l'éclair
            self.screen.blit(eclair_image, eclair_rect)
            pygame.display.flip()

            # Limiter la vitesse de la boucle
            horloge.tick(30)

        # # Quitter Pygame
        # pygame.quit()


# test1 = Lightning()
# test1.lightning()