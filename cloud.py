from global_def import Global
import pygame

class Cloud(Global):
    def __init__(self):
        Global.__init__(self)

    def cloud(self):
        pygame.init()

        image_path = r"images/images-play/play100.png"
        image1_path = r"images/images-play/play101.png"
        image = pygame.image.load(image_path)
        image1 = pygame.image.load(image1_path)
        image = pygame.transform.scale(image, (150, 159))
        image1 = pygame.transform.scale(image, (170, 179))
        image = image.convert_alpha()
        repetitions = 1

        for _ in range(repetitions):

            self.screen.blit(image, (55, 190))
            pygame.display.flip()
            pygame.time.delay(150)
            pygame.display.flip()            

            self.screen.blit(image, (60, 190))
            pygame.display.flip()            
            pygame.time.delay(150)        
            pygame.display.flip()
     
            self.screen.blit(image, (120, 210))
            pygame.display.flip()            
            pygame.time.delay(150)
            pygame.display.flip()
            
            self.screen.blit(image, (190, 250))
            pygame.display.flip()            
            pygame.time.delay(150)
            pygame.display.flip()

        repetition = 1
        for _ in range(repetition):
            for scale_factor in [1.0, 1.1, 1.2, 1.3]:
                scaled_image = pygame.transform.scale(image, (int(150 * scale_factor), int(159 * scale_factor)))
                self.screen.blit(scaled_image, (65, 200))
                pygame.display.flip()
                pygame.time.delay(100)

                pygame.display.flip()
                scaled_image = pygame.transform.scale(image, (int(150 * scale_factor), int(159 * scale_factor)))
                self.screen.blit(scaled_image, (95, 230))
                pygame.display.flip()
                pygame.time.delay(100)
                pygame.display.flip()

# test1 = Cloud()
# test1.cloud()
