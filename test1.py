from global_def import Global
import pygame
import sys

class Test1(Global):
    def __init__(self):
        Global.__init__(self)

    def affichage1(self):
        pygame.init()

        largeur, hauteur = 800, 600
        taille_fenetre = (largeur, hauteur)
        fenetre = pygame.display.set_mode(taille_fenetre)

        image_path = "images/images-play/play100.png"
        image1_path = "images/images-play/play101.png"
        image = pygame.image.load(image_path)
        image1 = pygame.image.load(image1_path)
        image = pygame.transform.scale(image, (150, 159))
        image1 = pygame.transform.scale(image, (170, 179))
        image = image.convert_alpha()
        repetitions = 1

        for _ in range(repetitions):
            self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',230,239,65,250)
            fenetre.blit(image, (65, 250))
            pygame.display.flip()
            pygame.time.delay(150)()
            fenetre.fill((0, 0, 0))
            pygame.display.flip()
            
            self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',230,239,65,250)
            fenetre.blit(image, (125, 250))
            pygame.display.flip()            
            pygame.time.delay(150)
            fenetre.fill((0, 0, 0))
            pygame.display.flip()
            
            self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',230,239,65,250)
            fenetre.blit(image, (80, 290))
            pygame.display.flip()            
            pygame.time.delay(150)
            fenetre.fill((0, 0, 0))
            pygame.display.flip()
            
            self.img_pokemon("pikachu",'images\images-pokedex\pokedex1.png',230,239,65,250)
            fenetre.blit(image, (100, 320))
            pygame.display.flip()            
            pygame.time.delay(150)
            fenetre.fill((0, 0, 0))
            pygame.display.flip()

        repetition = 1
        for _ in range(repetition):
            for scale_factor in [1.0, 1.1, 1.2, 1.3]:
                scaled_image = pygame.transform.scale(image, (int(150 * scale_factor), int(159 * scale_factor)))
                self.img_pokemon("pikachu", 'images\images-pokedex\pokedex1.png', 230, 239, 65, 250)
                fenetre.blit(scaled_image, (65, 250))
                pygame.display.flip()
                pygame.time.delay(100)
                fenetre.fill((0, 0, 0))
                pygame.display.flip()
                scaled_image = pygame.transform.scale(image, (int(150 * scale_factor), int(159 * scale_factor)))
                self.img_pokemon("pikachu", 'images\images-pokedex\pokedex1.png', 230, 239, 65, 250)
                fenetre.blit(scaled_image, (95, 260))
                pygame.display.flip()
                pygame.time.delay(100)
                fenetre.fill((0, 0, 0))
                pygame.display.flip()

        pygame.quit()
        sys.exit()

test1 = Test1()
test1.affichage1()
